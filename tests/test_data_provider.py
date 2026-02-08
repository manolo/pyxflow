"""Tests for DataProvider abstraction."""

import pytest

from vaadin.flow.data.provider import (
    CallbackDataProvider,
    DataProvider,
    ListDataProvider,
    Query,
    from_callbacks,
    items_provider,
)
from vaadin.flow.components.grid import Grid, Column, GridSortOrder, SortDirection
from vaadin.flow.components.combo_box import ComboBox
from vaadin.flow.core.state_tree import StateTree


class TestQuery:
    """Test Query construction and properties."""

    def test_defaults(self):
        q = Query()
        assert q.offset == 0
        assert q.limit == 50
        assert q.sort_orders == []
        assert q.filter is None

    def test_custom_values(self):
        q = Query(offset=10, limit=25, sort_orders=["s"], filter="abc")
        assert q.offset == 10
        assert q.limit == 25
        assert q.sort_orders == ["s"]
        assert q.filter == "abc"

    def test_filter_generic(self):
        q = Query(filter={"name": "test"})
        assert q.filter == {"name": "test"}


class TestListDataProvider:
    """Test ListDataProvider."""

    def test_create(self):
        dp = ListDataProvider([1, 2, 3])
        assert dp.items == [1, 2, 3]
        assert dp.is_in_memory is True

    def test_fetch_all(self):
        dp = ListDataProvider([10, 20, 30])
        result = dp.fetch(Query(offset=0, limit=50))
        assert result == [10, 20, 30]

    def test_fetch_with_offset_limit(self):
        dp = ListDataProvider(list(range(100)))
        result = dp.fetch(Query(offset=10, limit=5))
        assert result == [10, 11, 12, 13, 14]

    def test_size(self):
        dp = ListDataProvider([1, 2, 3, 4, 5])
        assert dp.size(Query()) == 5

    def test_filter(self):
        dp = ListDataProvider([1, 2, 3, 4, 5, 6])
        dp.set_filter(lambda x: x % 2 == 0)
        assert dp.size(Query()) == 3
        assert dp.fetch(Query(offset=0, limit=50)) == [2, 4, 6]

    def test_clear_filter(self):
        dp = ListDataProvider([1, 2, 3])
        dp.set_filter(lambda x: x > 2)
        assert dp.size(Query()) == 1
        dp.set_filter(None)
        assert dp.size(Query()) == 3

    def test_sort_via_query_dicts(self):
        """Sort dict items via query sort_orders."""
        items = [
            {"name": "Charlie", "age": 30},
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": 35},
        ]
        dp = ListDataProvider(items)

        col = Column("col0", "name", "Name")
        order = GridSortOrder(col, SortDirection.ASCENDING)
        result = dp.fetch(Query(offset=0, limit=50, sort_orders=[order]))
        assert [r["name"] for r in result] == ["Alice", "Bob", "Charlie"]

    def test_sort_descending(self):
        items = [{"v": 1}, {"v": 3}, {"v": 2}]
        dp = ListDataProvider(items)

        col = Column("col0", "v", "Value")
        order = GridSortOrder(col, SortDirection.DESCENDING)
        result = dp.fetch(Query(offset=0, limit=50, sort_orders=[order]))
        assert [r["v"] for r in result] == [3, 2, 1]

    def test_sort_comparator_overrides_query(self):
        items = [{"v": 3}, {"v": 1}, {"v": 2}]
        dp = ListDataProvider(items)
        dp.set_sort_comparator(lambda a, b: a["v"] - b["v"])

        col = Column("col0", "v", "Value")
        desc = GridSortOrder(col, SortDirection.DESCENDING)
        # Comparator should override the query's descending order
        result = dp.fetch(Query(offset=0, limit=50, sort_orders=[desc]))
        assert [r["v"] for r in result] == [1, 2, 3]

    def test_add_item(self):
        dp = ListDataProvider([1, 2])
        events = []
        dp.add_data_provider_listener(lambda e: events.append(e))

        dp.add_item(3)
        assert dp.items == [1, 2, 3]
        assert len(events) == 1
        assert events[0]["type"] == "refresh_all"

    def test_remove_item(self):
        dp = ListDataProvider([1, 2, 3])
        events = []
        dp.add_data_provider_listener(lambda e: events.append(e))

        dp.remove_item(2)
        assert dp.items == [1, 3]
        assert len(events) == 1
        assert events[0]["type"] == "refresh_all"

    def test_refresh_all_fires_listeners(self):
        dp = ListDataProvider([1, 2])
        events = []
        dp.add_data_provider_listener(lambda e: events.append(e))

        dp.refresh_all()
        assert len(events) == 1
        assert events[0] == {"type": "refresh_all"}

    def test_refresh_item_fires_listeners(self):
        dp = ListDataProvider(["a", "b"])
        events = []
        dp.add_data_provider_listener(lambda e: events.append(e))

        dp.refresh_item("a")
        assert len(events) == 1
        assert events[0] == {"type": "refresh_item", "item": "a"}

    def test_unsubscribe(self):
        dp = ListDataProvider([1])
        events = []
        unsub = dp.add_data_provider_listener(lambda e: events.append(e))

        dp.refresh_all()
        assert len(events) == 1

        unsub()
        dp.refresh_all()
        assert len(events) == 1  # no new event

    def test_filter_and_offset(self):
        dp = ListDataProvider(list(range(20)))
        dp.set_filter(lambda x: x >= 10)
        result = dp.fetch(Query(offset=2, limit=3))
        assert result == [12, 13, 14]

    def test_sort_objects_with_getattr(self):
        """Sort non-dict objects using getattr."""
        class Person:
            def __init__(self, name):
                self.name = name

        items = [Person("Charlie"), Person("Alice"), Person("Bob")]
        dp = ListDataProvider(items)

        col = Column("col0", "name", "Name")
        order = GridSortOrder(col, SortDirection.ASCENDING)
        result = dp.fetch(Query(offset=0, limit=50, sort_orders=[order]))
        assert [r.name for r in result] == ["Alice", "Bob", "Charlie"]


class TestCallbackDataProvider:
    """Test CallbackDataProvider."""

    def test_delegates_to_callbacks(self):
        data = list(range(100))

        def fetch(query):
            return data[query.offset : query.offset + query.limit]

        def count(query):
            return len(data)

        dp = CallbackDataProvider(fetch, count)
        assert dp.is_in_memory is False

        result = dp.fetch(Query(offset=5, limit=3))
        assert result == [5, 6, 7]
        assert dp.size(Query()) == 100

    def test_refresh_fires_listeners(self):
        dp = CallbackDataProvider(lambda q: [], lambda q: 0)
        events = []
        dp.add_data_provider_listener(lambda e: events.append(e))

        dp.refresh_all()
        assert len(events) == 1


class TestFactoryFunctions:
    """Test items_provider and from_callbacks."""

    def test_items_provider(self):
        dp = items_provider([10, 20, 30])
        assert isinstance(dp, ListDataProvider)
        assert dp.items == [10, 20, 30]

    def test_from_callbacks(self):
        dp = from_callbacks(lambda q: [1, 2], lambda q: 2)
        assert isinstance(dp, CallbackDataProvider)
        assert dp.fetch(Query()) == [1, 2]
        assert dp.size(Query()) == 2


class TestGridIntegration:
    """Test Grid with DataProvider."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_set_items_with_list_data_provider(self, tree):
        grid = Grid()
        grid.add_column("name")

        dp = ListDataProvider([{"name": "Alice"}, {"name": "Bob"}])
        grid.set_items(dp)

        # Should have set the data provider obj
        assert grid._data_provider_obj is dp
        assert grid._data_provider is None

    def test_set_data_provider_with_dp_object(self, tree):
        grid = Grid()
        grid.add_column("name")

        dp = ListDataProvider([{"name": "X"}])
        grid.set_data_provider(dp)
        assert grid._data_provider_obj is dp
        assert grid._data_provider is None

    def test_set_data_provider_with_callable(self, tree):
        grid = Grid()
        grid.add_column("name")

        fn = lambda offset, limit, sorts: ([{"name": "Y"}], 1)
        grid.set_data_provider(fn)
        assert grid._data_provider is fn
        assert grid._data_provider_obj is None

    def test_callback_data_provider_on_grid(self, tree):
        data = [{"name": f"Item {i}"} for i in range(200)]

        def fetch(query):
            return data[query.offset : query.offset + query.limit]

        def count(query):
            return len(data)

        dp = CallbackDataProvider(fetch, count)
        grid = Grid()
        grid.add_column("name")
        grid.set_data_provider(dp)
        grid._attach(tree)

        # Collect changes — should have execute commands for data push
        changes = tree.collect_changes()
        executes = tree._pending_execute
        # The grid should have pushed data via execute commands
        assert grid._data_provider_obj is dp

    def test_refresh_all_triggers_repush(self, tree):
        dp = ListDataProvider([{"name": "A"}])
        grid = Grid()
        grid.add_column("name")
        grid.set_data_provider(dp)
        grid._attach(tree)
        tree.collect_changes()
        tree._pending_execute.clear()

        # Now add an item and refresh
        dp._items.append({"name": "B"})
        dp.refresh_all()

        # Should have queued new execute commands for the updated data
        assert len(tree._pending_execute) > 0

    def test_set_items_clears_data_provider(self, tree):
        grid = Grid()
        grid.add_column("name")

        dp = ListDataProvider([{"name": "A"}])
        grid.set_data_provider(dp)
        assert grid._data_provider_obj is dp

        grid.set_items([{"name": "B"}])
        assert grid._data_provider_obj is None
        assert grid._items == [{"name": "B"}]

    def test_unsubscribes_on_new_provider(self):
        grid = Grid()
        grid.add_column("name")

        dp1 = ListDataProvider([{"name": "A"}])
        grid.set_data_provider(dp1)
        assert len(dp1._listeners) == 1

        dp2 = ListDataProvider([{"name": "B"}])
        grid.set_data_provider(dp2)
        assert len(dp1._listeners) == 0
        assert len(dp2._listeners) == 1


class TestComboBoxIntegration:
    """Test ComboBox with DataProvider."""

    @pytest.fixture
    def tree(self):
        return StateTree()

    def test_set_data_provider(self, tree):
        cb = ComboBox("Test")
        dp = ListDataProvider(["A", "B", "C"])
        cb.set_data_provider(dp)
        assert cb._provider is dp

    def test_set_data_provider_push_on_attach(self, tree):
        cb = ComboBox("Test")
        dp = ListDataProvider(["X", "Y"])
        cb.set_data_provider(dp)
        cb._attach(tree)

        # Should have pushed data via execute commands
        executes = tree._pending_execute
        assert len(executes) > 0

    def test_refresh_triggers_push(self, tree):
        cb = ComboBox("Test")
        dp = ListDataProvider(["A"])
        cb.set_data_provider(dp)
        cb._attach(tree)
        tree.collect_changes()
        tree._pending_execute.clear()

        dp.add_item("B")
        # Should have queued new execute commands
        assert len(tree._pending_execute) > 0

    def test_set_items_clears_provider(self):
        cb = ComboBox("Test")
        dp = ListDataProvider(["A"])
        cb.set_data_provider(dp)
        assert cb._provider is dp

        cb.set_items("X", "Y")
        assert cb._provider is None
        assert cb.get_items() == ["X", "Y"]
