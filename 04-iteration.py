#!/usr/bin/env python
# coding: utf-8
# %%
languages = ["C", "C++", "Python", "Java", "Ruby", "JavaScript"]

for language in languages:
    print(language)


# %%
# Das Schlüsselwort `break` beendet die Schleife vollständig.
for language in languages:
    print(language)
    if language == "Python":
        print("Python gefunden!")
        break


# %%
# `enumerate` gibt den Index und das Element zurück.
# Dies ist nützlich, wenn das Element sowie dessen Position benötigt werden.
for i, language in enumerate(languages):
    print(f"{i+1}. {language}")


# %%
# `range` erzeugt eine Sequenz von 0 bis n-1.
for i in range(10):
    # Gib eine Zahl aus, wenn sie gerade ist
    if i % 2 == 0:
        print(i)


# %%
# `continue` fährt sofort mit der nächsten Iteration fort.
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)


# %%
# Mit `while True` kann eine Endlosschleife erstellt werden,
# die durch `break` beendet wird.
i = 2
n = 100
while True:
    print(f"2^{i} = {2**i}")
    if input("Fortfahren (j/n)?") != "j":
        break
    i += 1


# %%
# In diesem Fall kann die Bedingung allerdings
# auch direkt zu Beginn geprüft werden.
i = 2
n = 100
while input("Fortfahren (j/n)?") == "j":
    print(f"2^{i} = {2**i}")
    i += 1


# %%
# Der Code berechnet die Primzahlen bis n.
# Eine effizientere Implementierung ist das Sieb des Eratosthenes.
# `break` beendet nur die innere Schleife.
n = 100
primes = []

for i in range(2, n):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        primes.append(i)

primes


# %%
# Schreiben Sie ein Programm, das die Fakultät einer Zahl berechnet.
n = 5


# %%
# Schreiben Sie ein Programm,
# das alle ganzen Zahlen im Bereich von a und b ausgibt,
# die durch x teilbar sind, aber nicht durch y.
a = 1
b = 100
x = 3
y = 5


# %%
# Schreiben Sie ein Programm,
# mit dem Sie die Quersumme einer Zahl berechnen können.
n = 199


# %%
# Erstellen Sie ein Quiz mit fünf Fragen.
# Die nächste Frage soll erst gestellt werden,
# wenn die aktuelle Frage korrekt beantwortet wurde.
l = [
    ("Wie heißt die Hauptstadt von Griechenland?", "Athen"),
    ("Wie heißt die Hauptstadt von Frankreich?", "Paris"),
    ("Wie heißt die Hauptstadt von Norwegen?", "Oslo"),
]


# %%
# Schreiben Sie ein Programm,
# das einen Text mit der Cäsar-Verschlüsselung kodiert.
# Aus "Hallo" wird "Kdoor" mit einem Versatz von n = 3.
# Vgl. https://www.w3schools.com/charsets/ref_html_ascii.asp
n = 3
s = "Hallo"
print(ord("d"))
print(chr(100))
