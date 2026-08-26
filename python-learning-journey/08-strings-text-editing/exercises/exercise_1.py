text = input("Enter a sentence: ")

print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Reversed: {text[::-1]}")

vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text if char in vowels)
print(f"Vowel count: {vowel_count}")