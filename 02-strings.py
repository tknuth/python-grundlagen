#!/usr/bin/env python
# coding: utf-8
# %%
'Das Wort "Wort" ist ein Substantiv'


# %%
'Das Wort "Wort" ist ein Substantiv'


# %%
greeting = "Guten Morgen"
name = "Anna"


# %%
s = "Hallo Welt!"


# %%
# Der Index beginnt bei 0.
s[0]


# %%
# Slicing bildet ein Intervall [a:b).
s[3:5]


# %%
# Beide Grenzen sind optional.
s[3:]


# %%
# Ein drittes Argument ist die Schrittweite.
s[::3]


# %%
# Prüfen Sie, ob das Wort ein Palindrom ist.
w = "Lagerregal"


# %%
long_text = (
    "Dies ist ein langer Text, "
    "der über mehrere Zeilen geht. "
    "Das ist praktisch. "
    "Und so weiter."
)


# %%
greeting + ", " + name


# %%
f"{greeting}, {name}"


# %%
new_greeting = greeting.replace("Morgen", "Abend")


# %%
# Der Aufruf gibt einen neuen String in Kleinbuchstaben zurück.
# Was passiert, wenn man die Klammern weglässt?
greeting.lower()


# %%
f"Die Grußformeln sind {greeting=} und {new_greeting=}."


# %%
help(str.replace)


# %%
3 * "ab" + "c"


# %%
print("Alle drei Wörter\n folgt eine neue\n Zeile.")


# %%
message = " HiER ist eTwAS schieFgegangen."
message.strip().lower().capitalize().replace("etwas", "nichts")


# %%
# Lesen Sie die Hilfen von `str.split` und `str.join`.
# Mit welchen Argumenten können die Funktionen verwendet werden?
", ".join("a, b, c".split(", "))


# %%
# Passen Sie den Code an, sodass die Elemente alphabetisch sortiert ausgegeben werden.
# Das Ergebnis sollte wieder ein String aus Komma-getrennten Wörtern sein.
l = "Apfel, Kiwi, Banane, Avocado, Kirsche, Pflaume"
sorted(l)


# %%
# Prüfen Sie, ob die beiden Wörter ein Anagramm bilden.
# Beachten Sie dabei, dass die Groß- und Kleinschreibung keine Rolle spielt.
a = "Lehm"
b = "Mehl"


# %%
# Berechnen Sie die Zeitdifferenz zwischen a und b in Minuten.
a = "17:45"
b = "19:15"
