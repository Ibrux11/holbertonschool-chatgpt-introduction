#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function to compute the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): The non-negative integer for which the factorial is to be computed.

    Returns:
    int: The factorial of the input integer `n`. If `n` is 0, returns 1 (since 0! = 1).
    For positive integers, it recursively multiplies `n` by the factorial of `n-1`.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Take input from the command line, compute the factorial, and print it
f = factorial(int(sys.argv[1]))
print(f)
