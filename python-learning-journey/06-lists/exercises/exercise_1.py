fruits = ["apple", "banana", "cherry", "mango"]

print("Original list:", fruits)

fruits.append("orange")
print("After append:", fruits)

fruits.remove("banana")
print("After removing banana:", fruits)

fruits.sort()
print("Sorted list:", fruits)

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Total fruits:", len(fruits))