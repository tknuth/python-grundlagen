#!/usr/bin/env python
# coding: utf-8
# %%
# Diese Funktion tut nichts.
def f():
    pass


# %%
# Diese Funktion tut ebenfalls nichts.
def f(): ...


# %%
# `x` ist der Parameter
def square(x):
    return x**2


square(3)  # 3 ist das Argument


# %%
# Hier sind `x` und `y` die Parameter.
def add(x, y):
    return x + y


add(3, 4)  # 3 und 4 sind die Argumente


# %%
# Diese Funktion erwartet exakt zwei Argumente.
def multiply(x, y):
    return x * y


multiply(2, 3)


# %%
# Funktionen können in anderen Funktionen verwendet werden.
# So lassen sich komplexe Operationen in kleinere Teile zerlegen.
def double(x):
    return multiply(x, 2)


# %%
# Um eine variable Anzahl Werte zu multiplizieren,
# könnte man eine Liste übergeben.
def multiply(values):
    n = 1
    for x in values:
        n *= x
    return n


multiply([2, 3, 4])


# %%
def greet(name):
    print(f"Hallo {name}!")


greet("Max")


# %%
# Wenn man kein Argument übergibt,
# wird der Standardwert verwendet.
def greet(name="du"):
    print(f"Hallo {name}!")


greet()


# %%
def greet(type="Hallo", name="du"):
    print(f"{type} {name}!")


# %%
# Der lokale Geltungsbereich hat Vorrang.
c = 1


def add(a, b):
    return a + b + c


add(3, 4)


# %%
# Lokale Variablen bleiben im lokalen Geltungsbereich.
# `c` hat am Ende immer noch den Wert 1.
def add(a, b):
    c = 2
    return a + b + c


print(add(3, 4))
print(c)


# %%
# Vervollständigen Sie den Code.
def faculty(n):
    pass


faculty(5)  # 120


# %%
# Vervollständigen Sie den Code.
# Vgl. https://de.wikipedia.org/wiki/Fibonacci-Folge
def fibonacci(n):
    pass


fibonacci(7)  # 13


# %%
# Entwickeln Sie eine Funktion,
# welche die Anzahl der Wörter in einem Text zählt.
def count(text):
    pass
    

count("Das Buch hat über 400 Seiten.")  # 6


# %%
# Entwickeln Sie eine Funktion,
# die ein Wort entgegennimmt und ggf. mit Punkten abkürzt,
# wenn eine definierte Länge überschritten wird.
def abbreviate(word, n):
    pass


abbreviate("Programmiersprache", 10)  # Programmie...
