import pandas as pd

data = pd.read_csv('Calendar_NewYork.csv')
df = pd.DataFrame(data)

df['listing_id'] = df['listing_id'].fillna(0)
df['date'] = df['date'].fillna("NA")
df['available'] = df['available'].fillna("NA")
df['price'] = df['price'].fillna(0)
df['adjusted_price'] = df['adjusted_price'].fillna(0)
df['minimum_nights'] = df['minimum_nights'].fillna(0)
df['maximum_nights'] = df['maximum_nights'].fillna(0)
print(data.head)
df.to_csv("Calendar_NewYork_Preprocessed.csv")

data = pd.read_csv('Calendar_London.csv')
df = pd.DataFrame(data)

df['listing_id'] = df['listing_id'].fillna(0)
df['date'] = df['date'].fillna("NA")
df['available'] = df['available'].fillna("NA")
df['price'] = df['price'].fillna(0)
df['adjusted_price'] = df['adjusted_price'].fillna(0)
df['minimum_nights'] = df['minimum_nights'].fillna(0)
df['maximum_nights'] = df['maximum_nights'].fillna(0)
print(data.head)
df.to_csv("Calendar_London_Preprocessed.csv")