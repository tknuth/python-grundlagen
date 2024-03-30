#!/usr/bin/env python
# coding: utf-8
# %%
type(True)


# %%
print(f"{1 == 1}")
print(f"{1 != 0}")
print(f"{1 >= 0}")


# %%
# paarweise Vergleiche
print(f"{2 >  1 > 0}")


# %%
"a" in ["a", "b", "c"]


# %%
weather = "Regen"

if weather == "Regen":
    print("Nimm einen Regenschirm mit.")
elif weather == "Sonne":
    print("Nimm eine Sonnenbrille mit.")
elif weather == "Schnee":
    print("Nimm Handschuhe mit.")
else:
    print("Nimm nichts mit.")


# %%
a = 1
b = 2

3 if a > b else 4

# %%
# Truthy/Falsy und Short-Circuiting
# https://docs.python.org/3/library/stdtypes.html#truth-value-testing
a or b
a and b
