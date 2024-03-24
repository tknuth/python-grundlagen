#!/usr/bin/env python
# coding: utf-8
# %%
languages = ["C", "C++", "Python", "Java", "Ruby", "JavaScript"]

for language in languages:
    print(language)


# %%
for language in languages:
    print(language)
    if language == "Python":
        print("Python gefunden!")
        break


# %%
for i, language in enumerate(languages):
    print(f"{i+1}. {language}")

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
