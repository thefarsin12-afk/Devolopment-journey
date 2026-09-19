"""
Write a Python program to print the
Fibonacci series up to n terms using a for loop.
"""

def fibanacci_series(n):

    first = 0

    second = 1

    for i in range (n):

        print(first)

        next = first + second

        first = second

        second = next

fibanacci_series(7)       

