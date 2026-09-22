from functools import reduce


# TASK 01
# Given a list of numbers, return the squares of only the odd ones.

nums = [1, 2, 3, 4, 5, 6, 7]

# Loop version
out = []
for n in nums:
    if n % 2 == 1:
        out.append(n * n)

print("Task 1 - Loop:", out)

# Functional version
out = [n * n for n in nums if n % 2 == 1]

print("Task 1 - Functional:", out)

# I prefer the functional version because it is shorter and easy to read.


# TASK 02
# Given a list of names, return them uppercased and stripped of whitespace.

names = [" Rahul ", " Priya", " Amit ", "Sneha"]

# Loop version
out = []
for name in names:
    out.append(name.strip().upper())

print("Task 2 - Loop:", out)

# Functional version
out = [name.strip().upper() for name in names]

print("Task 2 - Functional:", out)

# I prefer the functional version because it is concise and clear.


# TASK 03
# Given two lists of equal length, return a list of their pairwise products.

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

# Loop version
out = []
for i in range(len(list1)):
    out.append(list1[i] * list2[i])

print("Task 3 - Loop:", out)

# Functional version
out = [a * b for a, b in zip(list1, list2)]

print("Task 3 - Functional:", out)

# I prefer the functional version because zip makes pairwise operations simple.


# TASK 04
# Given a list of words, return only those longer than 4 characters.

words = ["apple", "cat", "banana", "dog", "orange"]

# Loop version
out = []
for word in words:
    if len(word) > 4:
        out.append(word)

print("Task 4 - Loop:", out)

# Functional version
out = [word for word in words if len(word) > 4]

print("Task 4 - Functional:", out)

# I prefer the functional version because the filtering condition is easy to see.


# TASK 05
# Given a list of numbers, find the product of all of them.

numbers = [1, 2, 3, 4, 5]

# Loop version
product = 1
for n in numbers:
    product *= n

print("Task 5 - Loop:", product)

# Functional version
product = reduce(lambda a, b: a * b, numbers)

print("Task 5 - Functional:", product)

# I prefer the functional version because reduce directly represents multiplication of all values.


# TASK 06
# Given a list of dicts with a "price" key, return the total price.

items = [
    {"price": 100},
    {"price": 200},
    {"price": 150}
]

# Loop version
total = 0
for item in items:
    total += item["price"]

print("Task 6 - Loop:", total)

# Functional version
total = sum(item["price"] for item in items)

print("Task 6 - Functional:", total)

# I prefer the functional version because sum makes the total calculation simple.


# TASK 07
# Given a nested list, flatten it.

nested = [[1, 2], [3, 4], [5]]

# Loop version
out = []
for sublist in nested:
    for item in sublist:
        out.append(item)

print("Task 7 - Loop:", out)

# Functional version
out = [item for sublist in nested for item in sublist]

print("Task 7 - Functional:", out)

# I prefer the functional version because it is shorter while remaining readable.


# TASK 08
# Given a list of strings, return a dict mapping each to its length.

strings = ["apple", "cat", "banana"]

# Loop version
out = {}
for text in strings:
    out[text] = len(text)

print("Task 8 - Loop:", out)

# Functional version
out = {text: len(text) for text in strings}

print("Task 8 - Functional:", out)

# I prefer the functional version because the dictionary is created in one clear expression.


# TASK 09
# Given a list of mixed values, drop everything falsy.

values = [0, "hello", "", None, 5, [], "Python", False]

# Loop version
out = []
for value in values:
    if value:
        out.append(value)

print("Task 9 - Loop:", out)

# Functional version
out = list(filter(None, values))

print("Task 9 - Functional:", out)

# I prefer the functional version because filter(None, values) clearly removes falsy values.


# TASK 10
# Given a list of numbers, return the running total.

numbers = [1, 2, 3]

# Loop version
out = []
total = 0

for n in numbers:
    total += n
    out.append(total)

print("Task 10 - Loop:", out)

# Functional version

from itertools import accumulate

out = list(accumulate(numbers))

print("Task 10 - Functional:", out)

# I prefer the loop version because a running total is easier to understand with a loop.`1`