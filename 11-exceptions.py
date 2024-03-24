#!/usr/bin/env python
# coding: utf-8
# %%
a = 1
b = 0

a / b

# %%
try:
    a / b
except Exception:
    print("Fehler!")

# %%
try:
    a / b
except ZeroDivisionError:
    print("Division durch 0 nicht möglich.")

# %%
a = 1
b = None
try:
    a / b
except ZeroDivisionError:
    print("Division durch 0 nicht möglich.")

# %%
a = 1
b = None
try:
    a / b
except ZeroDivisionError:
    print("Division durch 0 nicht möglich.")
except TypeError:
    print(
        f"Division für '{type(a).__name__}' und '{type(b).__name__}' nicht definiert."
    )

# %%
