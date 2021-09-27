import pandas as pd

# reading datasets
dt = pd.read_csv("London_listings_cleaned.csv")

# ensuring that there are no null values
dt['id'] = dt['id'].fillna(0)
dt['host_name'] = dt['host_name'].fillna('NA')
dt['host_since'] = dt['host_since'].fillna('NA')
dt['host_response_time'] = dt['host_response_time'].fillna("NA")
dt['host_response_rate'] = dt['host_response_rate'].fillna(0)
dt['host_acceptance_rate'] = dt['host_acceptance_rate'].fillna(0)
dt['host_is_superhost'] = dt['host_is_superhost'].fillna("NA")
dt['host_listings_count'] = dt['host_listings_count'].fillna(0)
dt['host_identity_verified'] = dt['host_identity_verified'].fillna("NA")
dt['bathrooms_text'] = dt['bathrooms_text'].fillna("NA")
dt['bedrooms'] = dt['bedrooms'].fillna(0)
dt['beds'] = dt['beds'].fillna(0)
dt['review_scores_value'] = dt['review_scores_value'].fillna(0)
dt['reviews_per_month'] = dt['reviews_per_month'].fillna(0)
print(dt.head())
no_of_amenities = []
# computing no. of amenities for each listing
for i in range(len(dt['amenities'])):
    l = dt['amenities'][i].split(',')
    no_of_amenities.append(len(l))
# adding no. of amenities to dataset
dt['no_of_amenities'] = no_of_amenities
dt.head()
# writing into excel sheet
dt.to_excel('Listings with amenities London.xlsx')
