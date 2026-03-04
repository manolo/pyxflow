# Data Providers

Data providers supply data to Grid and other data-bound components.

## In-Memory Items

```python
from pyxflow.components import Grid

grid = Grid()
grid.add_column("name", header="Name")
grid.add_column("email", header="Email")

items = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
]
grid.set_items(items)
```

## Lazy Data Provider (Callback)

For large datasets, use a callback that fetches pages on demand:

```python
grid = Grid()
grid.add_column("name", header="Name").set_sortable(True)
grid.set_page_size(20)

def fetch(offset, limit, sort_orders):
    # sort_orders: list of GridSortOrder with .column.property_name and .direction
    items = db.query_page(offset, limit)
    total = db.count()
    return items, total

grid.set_data_provider(fetch)
```

## Sort Orders in Data Provider

```python
from pyxflow.components import SortDirection

def fetch(offset, limit, sort_orders):
    query = db.session.query(Person)
    for order in sort_orders:
        col_name = order.column.property_name
        if order.direction == SortDirection.DESCENDING:
            query = query.order_by(desc(col_name))
        else:
            query = query.order_by(asc(col_name))
    return query.offset(offset).limit(limit).all(), query.count()
```

## Refresh Data

```python
# After data changes, refresh the grid
grid.set_items(new_items)  # In-memory
# or
grid.get_data_provider().refresh_all()  # Lazy provider
```

## ListDataProvider

```python
from pyxflow.data import ListDataProvider

provider = ListDataProvider(items)
grid.set_data_provider(provider)

# Later, update items
provider.refresh_all()
```

## ComboBox Items

```python
combo = ComboBox("Country")
combo.set_items("USA", "Canada", "Mexico", "UK")
```

## Select Items

```python
select = Select("Role")
select.set_items("Admin", "User", "Guest")
select.set_value("User")
```
