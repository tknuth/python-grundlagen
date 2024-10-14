#!/usr/bin/env python
# coding: utf-8
# %%
inventory = {"Apfel": 2, "Banane": 3}


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
inventory.pop("Pfirsich", 0)


# %%
del inventory["Banane"]


# %%
print(inventory.setdefault("Heidelbeere", 0))
inventory


# %%
inventory = {"Apfel": 2, "Banane": 3}

for k in inventory:
    print(f"{k}: {inventory[k]}")


# %%
for k, v in inventory.items():
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
values = inventory.values()
inventory["Erdbeere"] = 4
values
