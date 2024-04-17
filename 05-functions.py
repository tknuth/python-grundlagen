#!/usr/bin/env python
# coding: utf-8
# %%
def f():
    pass


# %%
def f(): ...


# %%
def add(x, y):
    return x + y


# %%
def square(x):
    return x**2


# %%
def add_one(x):
    return add(x, 1)


# %%
def multiply(*args):
    n = 1
    for arg in args:
        n *= arg
    return n


multiply(2, 3)


# %%
def greet(name):
    print(f"Hallo {name}!")


greet("Max")


# %%
def greet(name="du"):
    print(f"Hallo {name}!")


greet()
