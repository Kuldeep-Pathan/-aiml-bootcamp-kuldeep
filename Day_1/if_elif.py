# ===== Version 1: if/elif =====

print("IF/ELIF VERSION:")

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# ===== Version 2: Comprehension =====

print("\nCOMPREHENSION VERSION:")

result = [
    "FizzBuzz" if i % 15 == 0
    else "Fizz" if i % 3 == 0
    else "Buzz" if i % 5 == 0
    else i
    for i in range(1, 101)
]

print(*result, sep="\n")

'''I would rather maintain the if/elif version in six months because it is clear, readable, and easy to understand.'''

