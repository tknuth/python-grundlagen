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
