#!/usr/bin/env python
# coding: utf-8
# %%
'Das Wort "Wort" ist ein Substantiv'

# %%
'Das Wort "Wort" ist ein Substantiv'

# %%
greeting = "Guten Morgen"
name = "Anna"

# %%
long_text = (
    "Dies ist ein langer Text, "
    "der über mehrere Zeilen geht. "
    "Das ist praktisch. "
    "Und so weiter."
)

# %%
greeting + ", " + name

# %%
f"{greeting}, {name}"

# %%
new_greeting = greeting.replace("Morgen", "Abend")

# %%
help(str.replace)

# %%
3 * "ab" + "c"

# %%
", ".join(["a", "b", "c"])

# %%
"Dies ist ein Satz, der auch ein Komma enthält.".split()

# %%
print("Alle drei Wörter\n folgt eine neue\n Zeile.")

# %%
message = " HiER ist eTwAS schieFgegangen."
message.strip().lower().capitalize().replace("etwas", "nichts")

# %%
f"Die Grußformeln sind {greeting=} und {new_greeting=}."
