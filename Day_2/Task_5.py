#  Write fib_list(n) that returns the first n Fibonacci numbers as a list

def fib_list(n):
    numbers = []
    a, b = 0, 1

    for i in range(n):
        numbers.append(a)
        a, b = b, a + b

    return numbers


print(fib_list(7))

#  Write fib_gen(n) that does the same with yield

def fib_gen(n):
    a, b = 0, 1

    for i in range(n):
        yield a
        a, b = b, a + b


print(list(fib_gen(7)))


# Print the first 10 from each. Confirm the output matches.

print(fib_list(10))
print(list(fib_gen(10)))

'''Confirmed: Both produce the same first 10 Fibonacci numbers'''


#  Now: print the type of what each function returns. They are not the same. Note the difference.

print(type(fib_list(10)))
print(type(fib_gen(10)))

'''Observation: fib_list() returns a list, while fib_gen() returns a generator. 
                A generator produces values one at a time using yield'''


#  Loop over the same generator object twice. 
#  The second loop prints nothing. Explain why in a comment.

gen = fib_gen(5)

for x in gen:
    print(x)

for x in gen:
    print(x)  # Prints nothing because the generator is already exhausted.

'''A generator can be used only once. After the first loop consumes all its values, 
   it is exhausted, so the second loop has nothing to print.'''



#  Add a print statement before the yield. Run it and watch when it fires —  that tells you exactly when the code runs.


def fib_gen(n):
    a, b = 0, 1

    for i in range(n):
        print("Before yield:", a)
        yield a
        a, b = b, a + b


gen = fib_gen(3)

print("Generator created")

print(next(gen))
print(next(gen))
print(next(gen))


'''? What does yield do that return does not?
  -> yield gives values one at a time and pauses; return gives a value and ends the function.

? Why does looping over a generator twice give you nothing the second time?
-> A generator is an iterator, and once all its values are consumed, it cannot be restarted.

? Search: python generator memory. Compare sys.getsizeof on your list vs your generator.
->List → stores all values in memory.
Generator → produces values one at a time, so it usually uses much less memory.'''
