#!/usr/bin/env python
# coding: utf-8
# %%
inventory = {"apple": 2, "banana": 3}


# %%
inventory["pineapple"] = 1


# %%
sorted(inventory)


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

