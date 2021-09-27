import pandas as pd
from kmodes.kprototypes import KPrototypes as kp

# reading datasets
df = pd.read_csv('/content/Listings_Review_(join)NewYork.csv')
df['neighbourhood_cleansed'] = df['neighbourhood_cleansed'].fillna('NA')
df['total_listings'] = df['total_listings'].fillna('0')
df['total_reviews'] = df['total_reviews'].fillna('0')
df['minimum_price'] = df['minimum_price'].fillna('0')
df['maximum_price'] = df['maximum_price'].fillna('0')
df['avg_price'] = df['avg_price'].fillna('0')
df['avg_review_score'] = df['avg_review_score'].fillna('0')
df['min_review_score'] = df['min_review_score'].fillna('0')
df['max_review_score'] = df['max_review_score'].fillna('0')
df.head()

# KPrtotypes requires values to be used as array
df_array = df.values
print(df_array)

# specify numerical attributes
for i in range(1, 9):
    df_array[:, i] = df_array[:, i].astype(float)
    reviews_per_listing = []

# dividing dataset into clusters
kproto = kp(n_clusters=3, verbose=2)
clusters = kproto.fit_predict(df_array, categorical=[0])

# adding cluster as a column to dataset
df['cluster'] = clusters
df.to_excel('neighbhorhood cluster NYC.xlsx')
print(df.head())

# creating excel sheets cluster-wise
neighbhorhood_cluster0 = df[df['cluster'] == 0]
neighbhorhood_cluster0.head()
neighbhorhood_cluster0.to_excel('neighbhorhood_NYC_cluster0.xlsx')

neighbhorhood_cluster1 = df[df['cluster'] == 1]
neighbhorhood_cluster1.head()
neighbhorhood_cluster1.to_excel('neighbhorhood_NYC_cluster1.xlsx')

neighbhorhood_cluster1 = df[df['cluster'] == 2]
neighbhorhood_cluster1.head()
neighbhorhood_cluster1.to_excel('neighbhorhood_NYC_cluster2.xlsx')
