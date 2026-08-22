# 04 - Functions

**Book chapter:** Automate the Boring Stuff with Python, 3rd Ed. — Chapter 4

## Notes
- `def function_name(parameters):` defines a function.
- `return` sends a value back to wherever the function was called; without it, a function returns `None`.
- Parameters are local to the function — they don't exist outside it (this is called **scope**).
- You can give parameters **default values**: `def greet(name="friend"):`
- Functions can call other functions, and even themselves (**recursion**) — useful for things like factorials.
- Keeping code inside small, reusable functions makes programs easier to read, test, and debug.
