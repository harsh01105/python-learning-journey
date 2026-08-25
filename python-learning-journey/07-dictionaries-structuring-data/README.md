# 07 - Dictionaries and Structuring Data

**Book chapter:** Automate the Boring Stuff with Python, 3rd Ed. — Chapter 7

## Notes
- A dictionary stores **key-value pairs**: `my_dict = {"name": "Harsh", "age": 22}`
- Access a value: `my_dict["name"]`. Safer option: `my_dict.get("name")` (returns `None` instead of an error if key doesn't exist).
- Add/update: `my_dict["city"] = "Delhi"`
- Common methods: `.keys()`, `.values()`, `.items()`, `.pop()`, `.get()`
- Check if a key exists: `"name" in my_dict`
- Loop through a dict: `for key, value in my_dict.items():`
- Dictionaries can be nested (a dict of dicts, or a dict containing lists) — useful for structuring real-world data like a student record or JSON-style data.
- Unlike lists, dictionaries are unordered by concept (though Python 3.7+ preserves insertion order).