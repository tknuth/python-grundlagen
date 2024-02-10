#!/usr/bin/env python
# coding: utf-8
# %%
class Article:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category


# %%
class ShoppingCart:
    def __init__(self):
        self.records = []

    def add_item(self, item, count=1):
        self.records.append((item, count))

    @property
    def total(self):
        return sum([record[0].price * record[1] for record in self.records])

    def __len__(self):
        return len(self.records)


# %%
cart = ShoppingCart()
cart.add_item(Article("Banane", 199, "Obst"), 2)
cart.add_item(Article("Ananas", 299, "Obst"), 1)
cart.total
