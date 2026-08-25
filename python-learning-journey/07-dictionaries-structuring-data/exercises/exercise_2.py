text = "the quick brown fox jumps over the lazy dog the fox runs"
words = text.split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

for word, count in frequency.items():
    print(f"{word}: {count}")