# returns the min, max, mean, and count — as a dict

def calculate_stats(numbers):
    stats = {
        "min": min(numbers),
        "max": max(numbers),
        "mean": sum(numbers) / len(numbers),
        "count": len(numbers)
    }

    return stats


numbers = [10, 20, 30, 40, 50]

result = calculate_stats(numbers)

print(result)



# default or a clear error when handed an empty list

def calculate_stats(numbers):
    if len(numbers) == 0:
        return {"error": "The list is empty"}

    stats = {
        "min": min(numbers),
        "max": max(numbers),
        "mean": sum(numbers) / len(numbers),
        "count": len(numbers)
    }

    return stats


numbers = []

result = calculate_stats(numbers)

print(result)



# handles division by zero gracefully with try/except

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


print(safe_divide(10, 2))
print(safe_divide(10, 0))


#Add type hints to all your functions
 

def calculate_stats(numbers: list[int]) -> dict:
    stats = {
        "min": min(numbers),
        "max": max(numbers),
        "mean": sum(numbers) / len(numbers),
        "count": len(numbers)
    }

    return stats


numbers = [10, 20, 30, 40, 50]

result = calculate_stats(numbers)

print(result)



# short docstring for each function explaining what it does


def calculate_stats(numbers: list[int]) -> dict:
    """Calculate min, max, mean, and count of a list of numbers."""
    
    stats = {
        "min": min(numbers),
        "max": max(numbers),
        "mean": sum(numbers) / len(numbers),
        "count": len(numbers)
    }

    return stats


numbers = [10, 20, 30, 40, 50]

result = calculate_stats(numbers)

print(result)

''' Why return a dict rather than four separate values here?

Ans:-A dict keeps all four results together with clear names (min, max, mean, count),
     making the output more organized, readable, and easier to use.'''



'''What specific error should safe_divide catch, and why not catch everything?

Ans:-safe_divide should catch ZeroDivisionError because it specifically occurs 
     when dividing by zero.

     We should not catch everything with except Exception because it can hide unexpected programming errors 
     and make debugging difficult.'''


'''How do type hints and docstrings help the next person (including future you)?
Ans:-Type hints show what data a function expects and returns, while docstrings explain what the function does. 
     Together, they make code easier to understand, use, and maintain.'''
