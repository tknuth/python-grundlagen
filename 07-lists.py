#!/usr/bin/env python
# coding: utf-8
# %%
values = [1, 2, 3, 4, 5]


# %%
values[0]


# %%
values[-1]


# %%
values[2:]


# %%
values + values

% ##
a, b = [1, 2]


# %%
[[1, 2], [3, 4]]


# %%
[*[1, 2], *[3, 4]]


# %%
list(zip([1, 2], [3, 4]))


# %%
values[0] = 2
values


# %%
values.append(6)
values


# %%
values.insert(0, 1)
values


# %%
print(values.pop())
values


# %%
print(values.pop(-1))
values


# %%
8 in values


# %%
values[:][0] = 9
values


# %%
values.extend([7, 8, 9])
values


# %%
values.reverse()
values


# %%
list(reversed(values))


# %%
sorted(values)
