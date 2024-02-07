#!/usr/bin/env python
# coding: utf-8
# %%
def fib(n):
    """Gib die Fibonacci-Zahlen kleiner n aus."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
    
fib(50)

