numbers = [23, 67, 12, 89, 45, 3, 90, 56]

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print(f"List: {numbers}")
print(f"Largest number: {largest}")