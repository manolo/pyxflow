"""DataProvider abstraction for data-bound components."""

from abc import ABC, abstractmethod
from functools import cmp_to_key
from typing import Callable, Generic, TypeVar

T = TypeVar("T")
F = TypeVar("F")


class Query(Generic[T, F]):
    """Encapsulates a data request: offset, limit, sort orders, filter."""

    def __init__(
        self,
        offset: int = 0,
        limit: int = 50,
        sort_orders: list | None = None,
        filter: F | None = None,
    ):
        self._offset = offset
        self._limit = limit
        self._sort_orders = sort_orders or []
        self._filter = filter

    @property
    def offset(self) -> int:
        return self._offset

    @property
    def limit(self) -> int:
        return self._limit

    @property
    def sort_orders(self) -> list:
        return self._sort_orders

    @property
    def filter(self) -> F | None:
        return self._filter


class DataProvider(ABC, Generic[T, F]):
    """Abstract base class for data providers."""

    def __init__(self):
        self._listeners: list[Callable] = []

    @abstractmethod
    def fetch(self, query: Query[T, F]) -> list[T]:
        """Fetch items matching the query."""

    @abstractmethod
    def size(self, query: Query[T, F]) -> int:
        """Return the total number of items matching the query filter."""

    @property
    @abstractmethod
    def is_in_memory(self) -> bool:
        """Whether this provider holds all data in memory."""

    def refresh_item(self, item: T) -> None:
        """Notify listeners that a single item has changed."""
        event = {"type": "refresh_item", "item": item}
        for listener in self._listeners:
            listener(event)

    def refresh_all(self) -> None:
        """Notify listeners that all data may have changed."""
        event = {"type": "refresh_all"}
        for listener in self._listeners:
            listener(event)

    def add_data_provider_listener(self, listener: Callable) -> Callable:
        """Add a listener notified on data changes. Returns an unsubscribe callable."""
        self._listeners.append(listener)

        def unsubscribe():
            if listener in self._listeners:
                self._listeners.remove(listener)

        return unsubscribe


class ListDataProvider(DataProvider[T, None]):
    """In-memory data provider wrapping a list."""

    def __init__(self, items: list[T]):
        super().__init__()
        self._items = list(items)
        self._filter: Callable[[T], bool] | None = None
        self._comparator: Callable[[T, T], int] | None = None

    @property
    def items(self) -> list[T]:
        """The backing list."""
        return self._items

    @property
    def is_in_memory(self) -> bool:
        return True

    def set_filter(self, predicate: Callable[[T], bool] | None) -> None:
        """Set a filter predicate. Pass None to clear."""
        self._filter = predicate
        self.refresh_all()

    def set_sort_comparator(self, comparator: Callable[[T, T], int] | None) -> None:
        """Set a sort comparator. Pass None to clear."""
        self._comparator = comparator
        self.refresh_all()

    def add_item(self, item: T) -> None:
        """Add an item and notify listeners."""
        self._items.append(item)
        self.refresh_all()

    def remove_item(self, item: T) -> None:
        """Remove an item and notify listeners."""
        self._items.remove(item)
        self.refresh_all()

    def fetch(self, query: Query[T, None]) -> list[T]:
        """Fetch items: filter, sort, then slice."""
        result = self._items

        # Apply provider-level filter
        if self._filter:
            result = [item for item in result if self._filter(item)]

        # Apply query sort orders (from Grid columns)
        if query.sort_orders and not self._comparator:
            # Import here to avoid circular imports
            from vaadin.flow.components.grid import SortDirection

            for order in reversed(query.sort_orders):
                prop = order.column.property_name
                reverse = order.direction == SortDirection.DESCENDING
                if result and isinstance(result[0], dict):
                    result = sorted(result, key=lambda x, p=prop: x.get(p, ""), reverse=reverse)
                else:
                    result = sorted(result, key=lambda x, p=prop: getattr(x, p, ""), reverse=reverse)

        # Apply provider-level comparator (overrides sort_orders)
        if self._comparator:
            result = sorted(result, key=cmp_to_key(self._comparator))

        # Slice
        return result[query.offset : query.offset + query.limit]

    def size(self, query: Query[T, None]) -> int:
        """Total items after filtering."""
        if self._filter:
            return sum(1 for item in self._items if self._filter(item))
        return len(self._items)


class CallbackDataProvider(DataProvider[T, F]):
    """Lazy data provider wrapping fetch/count callbacks."""

    def __init__(
        self,
        fetch_callback: Callable[["Query[T, F]"], list[T]],
        count_callback: Callable[["Query[T, F]"], int],
    ):
        super().__init__()
        self._fetch_callback = fetch_callback
        self._count_callback = count_callback

    @property
    def is_in_memory(self) -> bool:
        return False

    def fetch(self, query: Query[T, F]) -> list[T]:
        return self._fetch_callback(query)

    def size(self, query: Query[T, F]) -> int:
        return self._count_callback(query)


def items_provider(items: list[T]) -> ListDataProvider[T]:
    """Create a ListDataProvider from a list."""
    return ListDataProvider(items)


def from_callbacks(
    fetch: Callable[["Query[T, F]"], list[T]],
    count: Callable[["Query[T, F]"], int],
) -> CallbackDataProvider[T, F]:
    """Create a CallbackDataProvider from fetch/count callables."""
    return CallbackDataProvider(fetch, count)
