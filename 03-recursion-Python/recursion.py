"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    lambda position: position if position<=1 else get_fib(position-1) +get_fib(position-2)