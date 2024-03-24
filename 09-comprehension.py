#!/usr/bin/env python
# coding: utf-8
# %%
[x**2 for x in range(5)]


# %%
{v: len(v) for v in ["Apfel", "Banane", "Melone"]}


# %%
inventory = {"Apfel": 2, "Banane": 3}
[f"{v}x {k}" for k, v in inventory.items()]


# %%
[k for k, v in inventory.items() if v > 2]

# %%
[-x - 1 if x % 2 == 0 else x for x in range(10)]
