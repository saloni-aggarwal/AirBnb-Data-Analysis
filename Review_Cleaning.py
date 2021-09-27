import pandas as pd

data = pd.read_csv('Reviews_NewYork.csv')
df = pd.DataFrame(data)

df['listing_id'] = df['listing_id'].fillna(0)
df['id'] = df['id'].fillna(0)
df['date'] = df['date'].fillna("NA")
df['reviewer_id'] = df['reviewer_id'].fillna(0)
df['comments'] = df['comments'].fillna("NA")
df.to_csv("Reviews_NewYork_Preprocessed.csv")

data = pd.read_csv('Reviews_London.csv')
df = pd.DataFrame(data)

df['listing_id'] = df['listing_id'].fillna(0)
df['id'] = df['id'].fillna(0)
df['date'] = df['date'].fillna("NA")
df['reviewer_id'] = df['reviewer_id'].fillna(0)
df['comments'] = df['comments'].fillna("NA")
df.to_csv("Reviews_London_Preprocessed.csv")