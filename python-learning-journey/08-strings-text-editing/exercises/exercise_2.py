sentence = input("Enter a sentence: ")

words = sentence.split()
print(f"Number of words: {len(words)}")

title_case = " ".join(word.capitalize() for word in words)
print(f"Title case: {title_case}")

cleaned = sentence.strip().replace("  ", " ")
print(f"Cleaned: '{cleaned}'")