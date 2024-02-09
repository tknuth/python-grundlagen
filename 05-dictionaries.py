#!/usr/bin/env python
# coding: utf-8
# %%
inventory = {"Apfel": 2, "Banane": 3}

# %%
inventory["Apfel"] = 1

# %%
inventory["Erdbeere"] = 5

# %%
del inventory["Banane"]

# %%
inventory["Ananas"] = 1

# %%
sorted(inventory)

# %%
values = inventory.values()

# %%
sum(values)

# %%
inventory["Erdbeere"] = 4
sum(values)

# %%
inventory["Pfirsich"]

# %%
inventory.get("Pfirsich")

# %%
inventory.get("Pfirsich", 0)

# %%
inventory.pop("Apfel")

# %%
inventory.pop("Pfirsich")

# %%
print(inventory.pop("Pfirsich", 0))
inventory

# %%
print(inventory.setdefault("Heidelbeere", 0))
inventory

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
