# Grundlagen der Programmierung mit Python

Dieses Repository enthält Beispiele zu den Grundlagen der Programmierung mit Python.

## Glossar

### Assignment Expression

Assignment Expressions ([PEP 572](https://peps.python.org/pep-0572/)) ermöglichen, einer Variable innerhalb eines Ausdrucks einen Wert zuzuweisen. An der entsprechenden Stelle wird ein Doppelpunkt mit einem Gleichheitszeichen kombiniert. Daher nennt man den Operator auch _Walross-Operator_. Dies kann beispielsweise Redundanz in Kontrollstrukturen verringern.

```python
if (n := 7) > 5:
    print(f"Die Zahl {n} ist größer als 5.")

while line := file.readline():
    process_line(line)
```

### Ausdruck

Ein Ausdruck ist eine Kombination von Werten, Variablen, Operatoren und Funktionsaufrufen, die zu einem Wert ausgewertet werden kann. Eine einzelne Konstante ist ebenso ein Ausdruck wie ein komplizierter Funktionsaufruf. Im Gegensatz zu einer Zuweisung gibt ein Ausdruck einen Wert zurück.

```python
>>> 1 + 2
3

>>> sum([1, 2, 3])
6

>>> "Hallo" + " " + "Welt!"
'Hallo Welt!'
```

### Datentyp

Ein Datentyp definiert, welche Art von Wert eine Variable speichert. Der Datentyp gibt Auskunft darüber, welche Operationen in Verbindung mit der Variable unterstützt werden. Python ist dynamisch typisiert. Das bedeutet, dass der Datentyp weder deklariert werden noch konstant sein muss. Die Verwendung von Typ-Annotationen zur expliziten Angabe des Datentyps ist für die leichtere Entwicklung und Wartbarkeit empfehlenswert.

```python
>>> type(1)
int

>>> type(1.0)
float

>>> type({})
dict

>>> type(True)
bool

>>> type(None)
NoneType
```

### Dictionary

Dictionaries ([Video](https://www.youtube.com/watch?v=daefaLgNkw0)) speichern Paare aus Schlüsseln und Werten. Sie sind in Python als Hash-Tabellen implementiert ([FAQ](https://docs.python.org/3/faq/design.html#how-are-dictionaries-implemented-in-cpython)), sodass der Zugriff auf Schlüssel und Werte unabhängig von der Größe des Dictionaries ist.

```python
d = {"name": "Max", "is_student": True}

# Setzen einzelner Werte
d["age"] = 42

# Abrufen einzelner Werte
d["name"] # "Max"

# Abrufen eines Werts mit Standardwert
d.get("is_student", False) # True

# Entfernen und Ausgeben eines Werts
d.pop("is_student") # True

# Setzen mehrerer Werte
d.update({"name": "Peter", "age": 38})
```

### Funktion

Funktionen ([Video](https://www.youtube.com/watch?v=u-OmVr_fT4s)) erlauben die Strukturierung von Code in wiederverwendbare, modulare Einheiten. Sie erlauben, Probleme in kleinere Teile zu zerlegen und diese unabhängig voneinander zu bearbeiten. Python bietet zahlreiche Standardfunktionen ([Docs](https://docs.python.org/3/library/functions.html)).

```python
def greet(name):
    return f"Hallo {name}!"

greet("Anna") # 'Hallo Anna!'
```

### Iteration

Bei der Iteration ([Video](https://www.youtube.com/watch?v=94UHCEmprCY)) wird eine Gruppe von Anweisungen wiederholt ausgeführt. In Python können iterierbare Objekte mithilfe von `for` und `while` in Schleifen durchlaufen werden. Bei Dictionaries werden die Schlüssel iteriert, mithilfe von `dict.items()` Schlüssel und Werte paarweise. `continue` springt zum nächsten Iterationsschritt, `break` beendet die komplette Schleife.

```python
# Die beiden Schleifen sind äquivalent
# Output: 0, 1, 2, 3, ... n-1

for i in range(n):
    print(i)

i = 0
while i < n:
    print(i)
    i += 1
```

### Liste

In Python sind Listen [(Video)(https://www.youtube.com/watch?v=9OeznAkyQz4)] als Arrays mit variabler Länge implementiert ([FAQ](https://docs.python.org/3/faq/design.html#how-are-lists-implemented-in-cpython)). Die Liste speichert Pointer auf die Elemente der Liste. Dadurch erlaubt die Liste den Zugriff auf Elemente über den Index in konstanter Zeit, aber gleichzeitig auch die Speicherung von Elementen unterschiedlicher Datentypen.

```python
l = ["my", "list"]

l[0] # 'my'

# am Ende einfügen
l.append("has") # None

# an zweiter Stelle einfügen
l.insert(1, "new") # None

# mehrere Elemente einfügen
l.extend(["many", "elements"]) # None

# letztes Element entfernen
l.pop()
```

### Klammern

In Python haben runde, eckige und geschweifte Klammern verschiedene Bedeutungen, abhängig vom Kontext. Runde Klammern werden für Funktionsaufrufe und zur Erstellung von Tupeln verwendet. Eckige Klammern dienen zur Erstellung von Listen und zum Slicing. Mit geschweiften Klammern werden Dictionaries und Sets erstellt.

```python
# Liste erstellen
l = ["my", "list"]

# Tupel erstellen
t = ("my", "tuple")

# Slicing
l[0] # 'my'

# Funktion aufrufen
len(l) # 2

# Dictionary erstellen
d = {"key": "value"}

# Set erstellen
s = {"my", "set"}
```

### None

In Python bezeichnet `None` ein spezielles Objekt, um darzustellen, dass eine Variable keinen Wert hat. Funktionen geben zudem `None` zurück, wenn kein expliziter Rückgabewert definiert wurde.

### Typ-Annotationen

Typ-Annotationen sind in Python optional. Sie helfen, den Code durch durch explizite Angabe von Typen robuster zu machen. Werkzeuge wie VSCode können die Typ-Annotationen zur Autovervollständigung nutzen und Bibliotheken zur statischen Codeanalyse können Typfehler frühzeitig erkennen.

```python
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hallo, {name}!"
```

### Set

Mengen sind Zusammenfassungen von Objekten ohne Wiederholungen. Mengen verhalten sich ähnlich wie Schlüssel von Dictionaries, allerdings ohne dazugehörige Werte.

```python
# Erstellen einer leeren Menge
>>> s = set()

# Hinzufügen von Elementen
>>> s.add("a")
>>> s.add("b")

# alternative Erstellung einer nichtleeren Menge
>>> s = {"a", "b"}

# Prüfung der Zugehörigkeit
>>> "a" in s
True
```

### Zahl

Zahlen gehören zu den primitiven Datentypen in Python. Es gibt verschiedene Zahlentypen, darunter die am häufigsten verwendeten, `int` für ganze Zahlen und `float` für Fließkommazahlen. Python bietet zudem weitere Module wie `decimal` für die präzise Verarbeitung von Dezimalzahlen an.

```python
>>> 3 + 7 # int
10

>>> 7 / 3 # float
3.5

>>> 0.1 + 0.2 == 0.3 # Fließkommazahlen sind nicht immer genau
False
```

### Zuweisung

Bei einer Zuweisung wird einem Variablennamen ein Wert zugeordnet. Auf der linken Seite der Zuweisung steht der Variablenname, auf der rechten ein Ausdruck.

```python
x = 1

y = a > b

z = "Hallo"
```
