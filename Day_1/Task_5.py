# Reverse Words

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

print(reverse_words("the cat sat"))



# Count Words

def count_words(sentence):
    words = sentence.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1

    return word_count


sentence = "the cat sat the cat"
result = count_words(sentence)
print(result)


# Return only the even ones, each doubled

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = [number * 2 for number in numbers if number % 2 == 0]

print(result)


# Return the unique items, sorted

numbers = [5, 2, 8, 2, 5, 1, 8, 3, 1]

unique_numbers = list(set(numbers))

unique_numbers.sort()

print(unique_numbers)



# Word is a palindrome or not


word = input("Enter a word: ")

reversed_word = word[::-1]

if word == reversed_word:
    print("It is a palindrome")
else:
    print("It is not a palindrome")


 
'''What does word[::-1] do, and why?
Ans:- word[::-1] reverses a string by using Python slicing with a step of -1,
      which means it reads the characters from right to left'''

'''How does a dict make word-counting so much easier than a list?
Ans:- A dictionary makes word-counting easier because it stores each word as a key and
      its count as the value.
      With a list, you would have to search for each word and manually track its count.
      A dictionary does this much more efficiently and clearly.
'''

'''When would you reach for a set in these problems?
Ans:-I would use a set when I only need unique items and don't care about duplicates or their order.'''
