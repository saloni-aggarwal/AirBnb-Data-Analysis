import pandas as pd

listings_NY = "C:\\Users\\Prajakta\\PycharmProjects\\Big Data\\Project\\listingsNY_preprocessed.csv"
listings_london = "C:\\Users\\Prajakta\\PycharmProjects\\Big Data\\Project\\listings_london_preprocessed.csv"

df_listings_NY = pd.read_csv(listings_NY)
df_listings_london = pd.read_csv(listings_london)

df_listings_NY['name'] = df_listings_NY['name'].fillna("NA")
df_listings_NY['host_name'] = df_listings_NY['host_name'].fillna("NA")
df_listings_NY['host_since'] = df_listings_NY['host_since'].fillna("NA")
df_listings_NY['host_response_time'] = df_listings_NY['host_response_time'].fillna("NA")
df_listings_NY['host_response_rate'] = df_listings_NY['host_response_rate'].fillna(0)
df_listings_NY['host_acceptance_rate'] = df_listings_NY['host_acceptance_rate'].fillna(0)
df_listings_NY['host_is_superhost'] = df_listings_NY['host_is_superhost'].fillna("NA")
df_listings_NY['host_listings_count'] = df_listings_NY['host_listings_count'].fillna(0)
df_listings_NY['host_identity_verified'] = df_listings_NY['host_identity_verified'].fillna("NA")
df_listings_NY['bathrooms_text'] = df_listings_NY['bathrooms_text'].fillna("NA")
df_listings_NY['bedrooms'] = df_listings_NY['bedrooms'].fillna(0)
df_listings_NY['beds'] = df_listings_NY['beds'].fillna(0)
df_listings_NY['review_scores_value'] = df_listings_NY['review_scores_value'].fillna(0)
df_listings_NY['reviews_per_month'] = df_listings_NY['reviews_per_month'].fillna(0)


del df_listings_NY['name']

df_listings_london['host_name'] = df_listings_london['host_name'].fillna("NA")
df_listings_london['host_since'] = df_listings_london['host_since'].fillna("NA")
df_listings_london['host_response_time'] = df_listings_london['host_response_time'].fillna("NA")
df_listings_london['host_response_rate'] = df_listings_london['host_response_rate'].fillna(0)
df_listings_london['host_acceptance_rate'] = df_listings_london['host_acceptance_rate'].fillna(0)
df_listings_london['host_is_superhost'] = df_listings_london['host_is_superhost'].fillna("NA")
df_listings_london['host_listings_count'] = df_listings_london['host_listings_count'].fillna(0)

df_listings_london['host_identity_verified'] = df_listings_london['host_identity_verified'].fillna("NA")
df_listings_london['neighbourhood'] = df_listings_london['neighbourhood'].fillna("NA")
df_listings_london['bathrooms_text'] = df_listings_london['bathrooms_text'].fillna("NA")
df_listings_london['bedrooms'] = df_listings_london['bedrooms'].fillna(0)
df_listings_london['beds'] = df_listings_london['beds'].fillna(0)
df_listings_london['review_scores_value'] = df_listings_london['review_scores_value'].fillna(0)
df_listings_london['reviews_per_month'] = df_listings_london['reviews_per_month'].fillna(0)
del df_listings_london['name']

df_listings_NY.to_csv("NY_listings_cleaned.csv", index=False)

df_listings_london.to_csv("London_listings_cleaned.csv", index=False)

print("Done!")
