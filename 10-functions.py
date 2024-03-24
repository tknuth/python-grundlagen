#!/usr/bin/env python
# coding: utf-8
# %%
def greet(*names):
    print("Hallo " + ", ".join(names) + "!")


greet("Max", "Moritz", "Anna")


# %%
def greet(*names):
    c = 0
    formatted_names = ""
    for name in reversed(names):
        if c == 0:
            formatted_names = name
        elif c == 1:
            formatted_names = name + " und " + formatted_names
        else:
            formatted_names = name + ", " + formatted_names
        c += 1

    print("Hallo " + formatted_names + "!")


greet("Max", "Moritz", "Anna")


def repeat(s, n=1):
    return s * n


print(repeat("a", 3))
print(repeat(n=1, s="a"))


# %%
def g(l=[]):
    l.append(1)
    return l


print(g())
print(g())


# %%
def create_record(name, age, hobby=None):
    return {"name": name, "age": age, "hobby": hobby}


create_record("Max", 30)


# %%
def fib(n):
    """Gib die Fibonacci-Zahlen kleiner n aus."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b


fib(50)
