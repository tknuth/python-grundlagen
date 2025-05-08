#!/usr/bin/env python
# coding: utf-8
# %%
d = {"a": 2, "b": 3, "c": 1, "d": 4}


# %%
# Gibt `None` als Standardwert zurück, wenn der Schlüssel nicht existiert.
d.get("e")


# %%
# Der Standardwert kann auch gesetzt werden.
d.get("e", 0)


# %%
# Entfernt das Schlüssel-Wert-Paar und gibt den Wert zurück.
# Wenn der Schlüssel nicht existiert, wird ein KeyError geworfen.
d.pop("d")


# %%
# Um einen KeyError zu verhindern, kann ein Standardwert gesetzt werden.
d.pop("e", 0)


# %%
# Alternativ kann auch `del` verwendet werden, um ein Schlüssel-Wert-Paar zu entfernen.
del d["a"]


# %%
# Setzt den Wert für einen Schlüssel, wenn dieser nicht existiert.
d.setdefault("f", 0)


# %%
d = {"a": 2, "b": 3, "c": 1, "d": 4}

for k in d:
    print(f"{k}: {d[k]}")


# %%
for k, v in d.items():
    print(f"{k}: {v}")


# %%
x = {"a": 1, "b": 2}
y = {"a": 3, "b": 4}

x == y


# %%
x = {"a": 1, "b": 2}
y = {"c": 3}

x.update(y)
x


# %%
x = {"a": 1, "b": 2}
y = {"c": 3}

print({**x, **y})
print(x | y)
print(1 | 2)


# %%
{["a", "b"]: 1}


# %%
{("a", "b"): 1}


# %%
d = {"a": 2, "b": 3}
values = d.values()
d["c"] = 4
values


# %%
# Erstellen Sie ein Dictionary,
# das die Zahlen von 1 bis 30 als Schlüssel
# und ihre Quadratzahlen als Werte enthält.
n = 30
squares = {}


# %%
# Schreiben Sie ein Programm, das die Häufigkeit der Wörter
# in einem Text berechnet und in einem Dictionary speichert.
frequencies = {}
text = " ".join(
    (
        "Dies ist ein kurzer Text.",
        "Der Text enthält einige Wörter.",
        "Einige Wörter sind mehrfach enthalten.",
    )
)


# %%
# Schreiben Sie ein Programm,
# das eine Einkaufsliste mit Artikelnamen und Anzahlen entgegennimmt
# und den Gesamtpreis berechnet.
# Erweitern Sie das Programm, sodass ab einer Bestellmenge von 2 Stück
# ein Preisnachlass von 10% gewährt wird.
fruits = [
    {
        "name": "apple",
        "price": 50,
    },
    {
        "name": "banana",
        "price": 90,
    },
    {
        "name": "cherry",
        "price": 290,
    },
    {
        "name": "grape",
        "price": 195,
    },
    {
        "name": "kiwi",
        "price": 100,
    },
    {
        "name": "lemon",
        "price": 150,
    },
    {
        "name": "mango",
        "price": 290,
    },
    {
        "name": "pomegranate",
        "price": 320,
    },
    {
        "name": "orange",
        "price": 80,
    },
    {
        "name": "peach",
        "price": 70,
    },
    {
        "name": "pear",
        "price": 80,
    },
]


# %%
# Erstellen Sie eine Funktion, welche ein Hobby als Argument entgegennimmt
# und eine Liste von Personen zurückgibt, die dieses Hobby teilen.
people = [
    {
        "name": "Anna",
        "age": 29,
        "hobbies": [
            "reading",
            "hiking",
        ],
    },
    {
        "name": "Tim",
        "age": 35,
        "hobbies": [
            "hiking",
            "swimming",
        ],
    },
    {
        "name": "Daniel",
        "age": 24,
        "hobbies": [
            "gaming",
            "reading",
        ],
    },
    {
        "name": "Jan",
        "age": 31,
        "hobbies": [
            "photography",
            "hiking",
        ],
    },
    {
        "name": "Sandra",
        "age": 28,
        "hobbies": [
            "cooking",
            "reading",
        ],
    },
    {
        "name": "Jana",
        "age": 25,
        "hobbies": [
            "swimming",
            "hiking",
        ],
    },
    {
        "name": "Tom",
        "age": 33,
        "hobbies": [
            "gaming",
            "photography",
        ],
    },
    {
        "name": "Lena",
        "age": 27,
        "hobbies": [
            "reading",
            "swimming",
        ],
    },
    {
        "name": "Max",
        "age": 30,
        "hobbies": [
            "cycling",
            "cooking",
        ],
    },
    {
        "name": "Lisa",
        "age": 26,
        "hobbies": [
            "reading",
            "hiking",
        ],
    },
]
