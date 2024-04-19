#!/usr/bin/env python
# coding: utf-8
# %%
type(True)


# %%
# Vergleiche ergeben Wahrheitswerte.
print(f"{1 == 1}")
print(f"{1 != 0}")
print(f"{1 >= 0}")


# %%
# Die beiden Varianten sind äquivalent.
print(f"{2 > 1 > 0}")
print(f"{2 > 1 and 1 > 0}")


# %%
# Mit `in`-Operator wird geprüft,
# ob ein Element in einer Liste enthalten ist.
"a" in ["a", "b", "c"]


# %%
# Die korrekte Einrückung ist wichtig,
# damit der Code der Bedingung zugeordnet wird.
# Es kann beliebig viele elif-Blöcke geben.
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
# if-else als Ausdruck
a = 1
b = 2

c = 3 if a > b else 4

# %%
# Truthy/Falsy und Short-Circuiting
# https://docs.python.org/3/library/stdtypes.html#truth-value-testing
a or b
a and b
