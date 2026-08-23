def check_age(age):
    assert age >= 0, "Age cannot be negative"
    assert age <= 120, "Age seems unrealistic"
    return f"Age {age} is valid."

try:
    user_age = int(input("Enter your age: "))
    print(check_age(user_age))
except AssertionError as e:
    print(f"Invalid input: {e}")