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


# %%
def greet(type="Hallo", name="du"):
    print(f"{type} {name}!")


# %%
# Der lokale Namensraum hat Vorrang
c = 1


def add(a, b):
    return a + b + c


add(3, 4)


# %%
# Variablen bleiben im lokalen Kontext
# c hat am Ende immer noch den Wert 1
def add(a, b):
    c = 2
    return a + b + c


print(add(3, 4))
print(c)
