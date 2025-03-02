#!/usr/bin/env python
# coding: utf-8
# %%
type(True)


# %%
# Vergleiche ergeben Wahrheitswerte.
print(1 == 1)
print(1 != 0)
print(1 >= 0)


# %%
# Die beiden Varianten sind äquivalent.
print(2 > 1 > 0)
print(2 > 1 and 1 > 0)


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


# %%
# Vervollständigen Sie das Programm.
x = input("Nenne eine Zahl:")
print("Die Zahl ist gerade.")
print("Die Zahl ist ungerade.")


# %%
# Programmieren Sie einen Notenrechner.
# Die Noten 1,0 bis 4,0 werden linear auf die Punkte 100 bis 50 abgebildet.
# Ein Ergebnis mit weniger als 50 Punkten entspricht der Note 5,0.
x = input("Anzahl Punkte:")
print(f"{x} Punkte entsprechen der Note v")


# %%
# Programmieren Sie Schere, Stein, Papier.
import random

choices = ["Schere", "Stein", "Papier"]
player = input("Schere, Stein oder Papier?")
computer = random.choice(choices)
