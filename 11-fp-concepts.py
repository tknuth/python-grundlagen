#!/usr/bin/env python
# coding: utf-8
# %%
l = []


def push(x):
    l.append(x)


push(1)
l

# %%
l = []


def push(x):
    l.append(x)
    return l


push(1)

# %%
l = []


def push(lst, x):
    lst.append(x)
    return lst


push(l, 1)

# %%
l = []


def push(lst, x):
    new_lst = lst[:]
    new_lst.append(x)
    return new_lst


push(l, 1)

# %%
l = []


def push(lst, x):
    return lst + [x]


push(l, 1)


# %%
def apply(f, x):
    return f(x)


def square(x):
    return x * x


def double(x):
    return x * 2


apply(double, 5)
apply(square, 5)


# %%
values = [1, 2, 3, 4, 5]

list(map(square, values))

# %%
list(map(lambda x: x**2, values))

# %%
list(filter(lambda x: x % 2 == 0, values))

# %%
from functools import reduce

reduce(lambda x, y: x + y, values)

# %%
from toolz.curried import *

pipe(values, map(double), map(square), list)

# %%
list(
    map(
        compose(square, double),
        values,
    )
)
