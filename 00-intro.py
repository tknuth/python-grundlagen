#!/usr/bin/env python
# coding: utf-8
# %%
3 * 5 / 2  # Python als Taschenrechner

# %%
s = "Hallo Welt!"  # Zuweisung von Variablen

# %%
s[0] # Der Index beginnt bei 0

# %%
s[3:5] # Slicing bildet ein Intervall [a:b)

# %%
s[3:] # Beide Grenzen sind optional

# %%
3 + 5  # Addition von Zahlen

# %%
"3" + "5"  # Konkatenation von Strings

# %%
3 * 5  # Multiplikation von Zahlen

# %%
"3" * 5  # Multiplikation von Strings

# %%
str(3)  # explizite Konvertierung

# %%
l = [1, 2, 3]  # Liste
l.append(4)  # Methode

# %%
# Iteration
for i in l:
    print(i)

# %%
for i in l:
    # Bedingungen
    if i % 2 == 0:
        print(i)


# %%
# Funktion
def f(x):
    return x**2
