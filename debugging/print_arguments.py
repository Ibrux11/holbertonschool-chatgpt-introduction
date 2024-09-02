#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  
    return result

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        f = factorial(int(arg))
        print(f)