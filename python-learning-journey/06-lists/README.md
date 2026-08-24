# 06 - Lists

**Book chapter:** Automate the Boring Stuff with Python, 3rd Ed. — Chapter 6

## Notes
- A list is an ordered, mutable collection: `my_list = [1, 2, 3]`
- **Indexing:** `my_list[0]` (first item), `my_list[-1]` (last item).
- **Slicing:** `my_list[1:3]` returns a sub-list (start included, end excluded).
- Common methods: `.append()`, `.insert()`, `.remove()`, `.pop()`, `.index()`, `.sort()`, `.reverse()`.
- `len(my_list)` gives the number of items.
- `in` checks membership: `3 in my_list`
- **List of lists**: a list can contain other lists — useful for grids/tables (e.g. `grid[row][col]`).
- Lists are mutable — changing them inside a function affects the original list too (unlike numbers/strings).