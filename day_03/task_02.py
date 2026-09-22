from collections import Counter
import string


# TASK 02 - Word Frequency with Counter

# Read the text file
with open("text.txt") as f:
    text = f.read()


# -------------------------------
# 1. Hard way: dictionary + loop + get()
# -------------------------------

words = text.lower().split()

counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

print("Word frequency using dictionary and loop:")
print(counts)


# -------------------------------
# 2. Right way: Counter
# -------------------------------

counts = Counter(words)

print("\nWord frequency using Counter:")
print(counts)


# -------------------------------
# 3. Print 10 most common words
# -------------------------------

print("\n10 most common words:")
print(counts.most_common(10))


# -------------------------------
# 4. Normalize punctuation
# -------------------------------

text = text.lower()

for punctuation in string.punctuation:
    text = text.replace(punctuation, "")

words = text.split()

counts = Counter(words)

print("\nWord frequency after removing punctuation:")
print(counts)


# -------------------------------
# 5. Remove stopwords
# -------------------------------

stopwords = {
    "the",
    "a",
    "an",
    "and",
    "is",
    "to",
    "of",
    "for",
    "in",
    "on",
    "has",
    "are"
}

filtered_words = [
    word for word in words
    if word not in stopwords
]

counts = Counter(filtered_words)

print("\n10 most common words after removing stopwords:")
print(counts.most_common(10))


# -------------------------------
# 6. Why is 'the.' different from 'the'?
# -------------------------------

print("\n'the' and 'the.' are counted separately before punctuation is removed.")
print("After removing punctuation, both are counted as 'the'.")