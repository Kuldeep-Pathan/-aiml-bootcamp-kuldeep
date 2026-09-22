# Take a list. Get an iterator from it with iter()

numbers = [1, 2, 3]

iterator = iter(numbers)

print(iterator)


# Call next() on it four times. The fourth one errors — that is expected. What is the error called?

numbers = [1, 2, 3]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))  # Error expected

'''The error is called StopIteration'''


# Now write a while True loop that reproduces exactly what for x in [1,2,3] does,
#  using only iter, next,try/except and break.

numbers = [1, 2, 3]

iterator = iter(numbers)

while True:
    try:
        x = next(iterator)
        print(x)
    except StopIteration:
        break

'''for loop'''
for x in [1, 2, 3]:
    print(x)


'''  Run both. Confirm identical output.
Answer:-Yes. Run both versions. They produce identical output
Observation: The while True version using iter(), next(), try/except,
             and break works the same as the for loop. '''


'''1. What exception does a finished iterator raise?

StopIteration. A for loop catches it automatically, so you don't see the error.

2. Iterable vs Iterator?
Iterable: Can be converted to an iterator using iter().
Iterator: Produces values using next().
3. Is a file object an iterator? Test it.

Yes, a file object is an iterator.'''