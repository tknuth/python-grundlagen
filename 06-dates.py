#!/usr/bin/env python
# coding: utf-8
# %%
# Mit der `datetime`-Bibliothek können Datums- und Zeitangaben verarbeitet werden.
from datetime import date, datetime, timedelta

datetime.now()


# %%
datetime.now().timestamp()


# %%
datetime.now() - timedelta(days=1)


# %%
date.today() + timedelta(weeks=1)


# %%
datetime.now().isoformat()


# %%
date.fromisoformat("2024-01-01")
