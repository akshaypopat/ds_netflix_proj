#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Netflix data science project

Data cleaning in Spyder

Dataset from https://www.kaggle.com/datasets/shivamb/netflix-shows

@author: akshaypopat
"""

import pandas as pd

df = pd.read_csv("~/Documents/Data Science/netflix_proj/netflix_titles.csv")

True in df.type.isnull().values
True in df.title.isnull().values

df["type_clean"] = df.type.apply(lambda x: x.strip().lower())

df["director_filled"] = df.director.fillna("unknown")
df["director_filled"] = df.director_filled.apply(lambda x: x.strip().lower())

df["cast_filled"] = df.cast.fillna("unknown")
df["cast_filled"] = df.cast_filled.apply(lambda x: x.strip().lower())

df["country_filled"] = df.country.fillna("unknown")
df["country_filled"] = df.country_filled.apply(lambda x: x.strip().lower())

True in df.date_added.isnull().values

df["dates_filled"] = df.date_added.fillna("unknown")

df["month_added"] = df.dates_filled.apply(lambda x: x.strip().partition(" ")[0].lower() if x != "unknown" else x)
df["year_added"] = df.dates_filled.apply(lambda x: int(x.strip().partition(",")[-1].strip()) if x != "unknown" else 2023)
df["netflix_age"] = df.year_added.apply(lambda x: 2022 - x)

df["release_year_filled"] = df.release_year.fillna(2023)
df["age"] = df.release_year.apply(lambda x: 2022 - x)

df["rating_filled"] = df.rating.fillna("nr")

for i in range(len(df.rating_filled)):
    if df.rating_filled[i][-3::] == "min":
        df["duration"][i] = df.rating_filled[i]
        df["rating_filled"][i] = "nr"
        
df["rating_filled"] = df.rating_filled.apply(lambda x: x.strip().lower())

df["dur"] = df.duration.apply(lambda x: int(x.partition(" ")[0]))

df["genre"] = df.listed_in.apply(lambda x: x.strip().lower())

df["desc"] = df.description.apply(lambda x: x.strip().lower())

df.to_csv("~/Documents/Data Science/netflix_proj/data.csv")
