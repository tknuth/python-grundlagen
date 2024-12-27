# Grundlagen der Programmierung mit Python

Dieses Repository enthält Beispiele zu den Grundlagen der Programmierung mit Python.

## Glossar

### Typ-Annotationen

Typ-Annotationen sind in Python optional. Sie helfen, den Code durch durch explizite Angabe von Typen robuster zu machen. Werkzeuge wie VSCode können die Typ-Annotationen zur Autovervollständigung nutzen und Bibliotheken zur statischen Codeanalyse können Typfehler frühzeitig erkennen.

```python
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hallo, {name}!"
```

### Assignment Expression

Assignment Expressions ([PEP 572](https://peps.python.org/pep-0572/)) ermöglichen, einer Variable innerhalb eines Ausdrucks einen Wert zuzuweisen. An der entsprechenden Stelle wird ein Doppelpunkt mit einem Gleichheitszeichen kombiniert. Daher nennt man den Operator auch _Walross-Operator_. Dies kann beispielsweise Redundanz in Kontrollstrukturen verringern.

```python
if (n := 7) > 5:
    print(f"Die Zahl {n} ist größer als 5.")

while line := file.readline():
    process_line(line)
```

### Zuweisung

Bei einer Zuweisung wird einem Variablennamen ein Wert zugeordnet. Auf der linken Seite der Zuweisung steht der Variablenname, auf der rechten ein Ausdruck.

```python
x = 1

y = a > b

z = "Hallo"
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
