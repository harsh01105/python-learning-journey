def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: cannot divide by zero"
    except ValueError:
        return "Error: invalid input"
    else:
        return result

x = input("Enter numerator: ")
y = input("Enter denominator: ")

try:
    x = float(x)
    y = float(y)
    print(safe_divide(x, y))
except ValueError:
    print("Error: please enter valid numbers")