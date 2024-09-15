#!/usr/bin/env python
# coding: utf-8
# %%
print("Willkommen zu Python!")

# %%
# Ganzzahl
1

# %%
# Fließkommazahl
1.3

# %%
# Addition
2 + 2

# %%
# Potenzierung
5**2

# %%
# Beachten Sie die Operatorpräzedenz nach PEMDAS.
(50 - 5 * 6) / 4

# %%
# Ganzzahldivision
17 // 3

# %%
# Modulus/Rest
17 % 3

# %%
import math

math.sqrt(2)

# %%
# Vorsicht, Fließkommazahlen können zu unerwarteten Ergebnissen führen.
0.1 + 0.2 == 0.3

# %%
price = 19.99
discount = 0.25
round(price * (1 - discount), 2)

# %%
# Vertauschen Sie die Werte von a und b.
a = 1
b = 2

# %%
name = input("Wie heißt du?")
"Hallo " + name

# %%
# Konkatenation von Strings
"3" + "4"

# %%
# Vervielfachung von Strings
"3" * 4

# %%
# Hilfe zu Objekten/Funktionen
help(print)

# %%
# Die Funktion `type` gibt den Datentyp an.
type(3.1)

# %%
# Was passiert hier?
a = input("Nenne eine ganze Zahl für a:")
b = input("Nenne eine ganze Zahl für b:")
a + b

# %%
# Korrigieren Sie den Fehler.
birth_year = input("In welchem Jahr wurdest du geboren?")
age = 2024 - birth_year
"Du bist " + age + " Jahre alt."

# %%
# Korrigieren Sie den Fehler.
x = input("Gib eine ganze Zahl an:")
"Das doppelte deiner Zahl lautet " + 2 * x
