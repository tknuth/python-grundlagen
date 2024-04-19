#!/usr/bin/env python
# coding: utf-8
# %%
values = [1, 2, 3, 4, 5]


# %%
# Der Index beginnt bei 0.
values[0]


# %%
# Man kann Werte auch mit negativen Indizes abrufen.
values[-1]


# %%
# Dies gibt alle Werte ab dem dritten Wert zurück.
values[2:]


# %%
# `sorted` gibt eine sortierte Kopie der Liste zurück.
sorted(values)

# %%
# Man kann einen Wert am Ende der Liste anhängen.
# Es gibt keinen Rückgabewert, weil die ursprüngliche Liste verändert wurde.
values.append(6)
values


# %%
# Listen unterstützen viele verschiedene Methoden.
values.insert(0, 1)
values.pop()
values.extend([1, 2, 3])
values.reverse()


# %%
# Listen lassen sich zusammenfügen.
# Hierdurch entsteht eine neue Liste.
values + values

# %%
# Listen können entpackt werden.
a, b, *rest = values
print(a, b, rest)

# %%
# Listen können verschiedene Objekte beinhalten.
values = [1, "zwei", 3.0, True, None, [1, 2, 3]]


# %%
# Werte in Listen können ausgetauscht werden.
values[1] = 2
values

# %%
# Listen können auch verschachtelt sein.
[[1, 2], [3, 4]]

# %%
# Manche Funktionen werden nicht sofort ausgeführt,
# sondern geben ein Objekt zurück, das iteriert werden kann.
# Mit `list` wird das Objekt in eine Liste umgewandelt.
list(reversed(values))

# %%
# Mit `zip` können zwei Listen paarweise zusammengeführt werden.
list(zip([1, 2], [3, 4]))


# %%
# `[:]` erstellt eine Kopie der Liste.
# Wichtig: Es werden nur die Referenzen kopiert.
values[:][0] = 9
values
