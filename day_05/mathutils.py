"""Provide basic mathematical utility functions."""

# These imports are intentionally unused so Ruff can detect them.
# import os
# import random
# import sys
# Ruff --fix automatically removes unused imports that it can safely fix.


def average(nums: list[int]) -> float:
    """Return the mean of a list of numbers.

    Args:
        nums: A list of integers. May be empty.

    Returns:
        The mean as a float, or 0.0 if the list is empty.
    """
    if not nums:
        return 0.0
        # print(total_sum)
        # Ruff detected F821 because total_sum was used without being defined.

    return sum(nums) / len(nums)


def biggest(nums: list[int]) -> int | None:
    """Return the largest number in a list.

    Args:
        nums: A list of integers. May be empty.

    Returns:
        The largest integer, or None if the list is empty.
    """
    if not nums:
        return None
    return max(nums)


def is_prime(number: int) -> bool:
    """Return whether a number is prime.

    Args:
        n: The integer to check.

    Returns:
        True if the number is prime, otherwise False.
        Numbers less than 2 return False.
    """
    if number < 2:
        return False

    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False

    return True


# Black automatically formats the code by fixing spacing and extra blank lines.


# ------------------Task-2--------------------

# """Provide basic mathematical utility functions."""

# from typing import Optional

# def average(nums: list[float]) -> float:
#     """Return the mean of a list of numbers.

#     Args:
#         nums: A list of numbers. May be empty.

#     Returns:
#         The mean as a float, or 0.0 if the list is empty.
#     """
#     if not nums:
#         return 0.0
#     return sum(nums) / len(nums)


# def biggest(nums: list[float]) -> float:
#     """Return the largest number in a list.

#     Args:
#         nums: A list of numbers. May be empty.

#     Returns:
#         The largest number, or 0.0 if the list is empty.
#     """
#     if not nums:
#         return 0.0
#     return max(nums)


# def is_prime(n: int) -> bool:
#     """Return whether a number is prime.

#     Args:
#         n: The integer to check.

#     Returns:
#         True if the number is prime, otherwise False.
#         Numbers less than 2 return False.
#     """
#     if n < 2:
#         return False

#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False

#     return True


# ---------------Task-1----------------

# def average(nums):
#     if len(nums) == 0:
#         return 0
#     return sum(nums) / len(nums)


# def biggest(nums):
#     if len(nums) == 0:
#         return 0
#     return max(nums)


# def is_prime(n):
#     if n < 2:
#         return False

#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False

#     return True


"""Q1. Why does the file have to be named test_*.py and the functions test_*?
Ans: Pytest uses the test_ naming convention to automatically discover test files and test functions.

Q2. Is 1 prime? Is 2? Is 0?
Ans: 1 → No, 2 → Yes, 0 → No.

Q3. What does pytest -v show that plain pytest does not?
Ans: -v shows each test name and its PASSED/FAILED status in detail."""


""" Q1. What is the difference between a docstring and a `#` comment? When do you use each?**
 **Ans:** A docstring documents a function, class, or module and can be viewed using `help()`. A `#` comment explains specific code details.

    Q2. Why write the summary in the imperative (`Return`) not the descriptive (`Returns`)?**
 **Ans:** Imperative style clearly describes what the function does or should do.

    Q3. What is the difference between Google style and NumPy style docstrings?**
 **Ans:** Both document Python code, but they use different formatting. Google style uses sections like `Args:` and `Returns:`, while NumPy style uses underlined section headings like `Parameters` and `Returns`"""
