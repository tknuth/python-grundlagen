#!/usr/bin/env python
# coding: utf-8
# %%
[x**2 for x in range(5)]


# %%
inventory = {"Apfel": 2, "Banane": 3}


# %%
{v: len(v) for v in ["Apfel", "Banane", "Melone"]}


# %%
[f"{v}x {k}" for k, v in inventory.items()]
