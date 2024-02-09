#!/usr/bin/env python
# coding: utf-8
# %%
for i in range(10):
    # Gib eine Zahl aus, wenn sie gerade ist
    if i % 2 == 0:
        print(i)


# %%
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

