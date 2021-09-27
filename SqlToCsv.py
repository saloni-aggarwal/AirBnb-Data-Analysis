import pandas as pd
import matplotlib.pyplot as plt
import pyodbc

# setting up connection with SMSS
conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=DESKTOP-1RMQQ1M;'
                      'Database=MyDatabase;'
                      'Trusted_Connection=yes;')

# query to arrange neighborhoods in london in descending order according to number of listings in each neighborhood
sql_query = pd.read_sql_query('''SELECT COUNT(MyDatabase.dbo.London_listings_cleaned$.id) AS TOTAL_IDS, MyDatabase.dbo.London_listings_cleaned$.neighbourhood_cleansed FROM MyDatabase.dbo.London_listings_cleaned$ GROUP BY MyDatabase.dbo.London_listings_cleaned$.neighbourhood_cleansed ORDER BY TOTAL_IDS DESC''', conn)
# saving the table made in csv file
df = pd.DataFrame(sql_query)
df.to_csv("Total neighbourhoods_London.csv")
# query to arrange neighborhoods in new york in descending order according to number of listings in each neighborhood
sql_query1 = pd.read_sql_query('''SELECT COUNT(MyDatabase.dbo.London_listings_cleaned$.property_type) AS Total_Count,  MyDatabase.dbo.London_listings_cleaned$.property_type FROM  MyDatabase.dbo.London_listings_cleaned$ GROUP BY MyDatabase.dbo.London_listings_cleaned$.property_type ORDER BY Total_Count DESC''', conn)
# saving the table made in csv file
df1 = pd.DataFrame(sql_query1)
df1.to_csv("PropertyVsAcceptanceRateLondon.csv")

# pie chart to plot top 15 neighborhoods in both the cities
explode = []

for i in range(5):
    explode.append(0.03)

file = pd.read_csv("Total neighbourhoods_NewYork.csv.csv")

plt.pie(file['TOTAL_IDS'], explode=explode, labels=file['neighbourhood_group_cleansed'], autopct='%1.1f%%')
plt.title("Percentage of Airbnbs in different neighbourhoods of New York")
plt.show()

explode = []

for i in range(15):
    explode.append(0.04)

file = pd.read_csv("Total neighbourhoods_London.csv")
plt.pie(file['TOTAL_IDS'], explode=explode, labels=file['neighbourhood_cleansed'], autopct='%1.1f%%')
plt.title("Percentage of Airbnbs in different neighbourhoods of London")
plt.show()

# query to find number of reviews in each listings for london and saving the table made in csv file
sql_query = pd.read_sql_query('''select MyDatabase.dbo.Reviews_London_Preprocessed$.listing_id, count(MyDatabase.dbo.Reviews_London_Preprocessed$.listing_id) 
as total_reviews from MyDatabase.dbo.Reviews_London_Preprocessed$ group by MyDatabase.dbo.Reviews_London_Preprocessed$.listing_id''', conn)
df = pd.DataFrame(sql_query)
df.to_csv("Total_Reviews_London.csv")

# query to find number of reviews in each listings for new york and saving the table made in csv file
sql_query = pd.read_sql_query('''select MyDatabase.dbo.NY_listings_cleaned$.neighbourhood_cleansed, count(MyDatabase.dbo.NY_listings_cleaned$.listing_id) as 
total_listings, sum(cast(MyDatabase.dbo.Total_Reviews_NewYork.total_reviews as int)) as total_reviews, min(MyDatabase.dbo.NY_listings_cleaned$.price) as 
minimum_price, max(MyDatabase.dbo.NY_listings_cleaned$.price) as maximum_price, avg(MyDatabase.dbo.NY_listings_cleaned$.price) as avg_price, 
avg(MyDatabase.dbo.NY_listings_cleaned$.review_scores_value) as avg_review_score, min(MyDatabase.dbo.NY_listings_cleaned$.review_scores_value) as 
min_review_score, max(MyDatabase.dbo.NY_listings_cleaned$.review_scores_value) as max_review_score from MyDatabase.dbo.NY_listings_cleaned$ left join 
MyDatabase.dbo.Total_Reviews_NewYork on MyDatabase.dbo.NY_listings_cleaned$.listing_id = MyDatabase.dbo.Total_Reviews_NewYork.listing_id group by 
MyDatabase.dbo.NY_listings_cleaned$.neighbourhood_cleansed''', conn)
df = pd.DataFrame(sql_query)
df.to_csv("Listings_Review_NewYork.csv")

# queries to join tables and saving in csv file accordingly
sql_query = pd.read_sql_query('''SELECT MyDatabase.dbo.Listings_with_amenities_NYC$.*, MyDatabase.dbo.Neighborhood_NYC_Cluster.cluster from 
MyDatabase.dbo.Listings_with_amenities_NYC$ left join MyDatabase.dbo.Neighborhood_NYC_Cluster on MyDatabase.dbo.Listings_with_amenities_NYC$.neighbourhood
_cleansed = MyDatabase.dbo.Neighborhood_NYC_Cluster.neighbourhood_cleansed''', conn)
df = pd.DataFrame(sql_query)
df.to_csv("Final_NY_Dataset.csv")

sql_query = pd.read_sql_query('''SELECT MyDatabase.dbo.Listings_with_amenities_London$.*, MyDatabase.dbo.Neighborhood_London_Cluster$.cluster from 
MyDatabase.dbo.Listings_with_amenities_London$ left join MyDatabase.dbo.Neighborhood_London_Cluster$ on MyDatabase.dbo.Listings_with_amenities_
London$.neighbourhood_cleansed = MyDatabase.dbo.Neighborhood_London_Cluster$.neighbourhood_cleansed''', conn)
df = pd.DataFrame(sql_query)
df.to_csv("Final_London_Dataset.csv")

# sql query to extract month and year from date, select listing_id, number of reservations etc to prepare table for Boosting Reservation application
sql_query = pd.read_sql_query('''select MyDatabase.dbo.Calendar_NewYork_Preprocessed$.listing_id, (DATENAME(MONTH from MyDatabase.dbo.Calendar_NewYork_
Preprocessed$.date) + '-'+ DATENAME(YEAR from MyDatabase.dbo.Calendar_NewYork_Preprocessed$.date)) as Month_Year_Combination, 
count(MyDatabase.dbo.Calendar_NewYork_Preprocessed$.listing_id) as reservations from MyDatabase.dbo.Calendar_NewYork_Preprocessed$ group by 
MyDatabase.dbo.Calendar_NewYork_Preprocessed$.listing_id, (DATENAME(MONTH from MyDatabase.dbo.Calendar_NewYork_Preprocessed$.date) + '-'+ 
DATENAME(YEAR from MyDatabase.dbo.Calendar_NewYork_Preprocessed$.date))''', conn)
df = pd.DataFrame(sql_query)
df.to_csv("NewYork_Reservations.csv")

sql_query = pd.read_sql_query('''select MyDatabase.dbo.Listings_with_amenities_London$.id, MyDatabase.dbo.Listings_with_amenities_London$.no_of_amenities, 
MyDatabase.dbo.Listings_with_amenities_London$.price, MyDatabase.dbo.London_Reservations.Month_Year_Combination, MyDatabase.dbo.London_
Reservations.reservations from MyDatabase.dbo.London_Reservations left join  MyDatabase.dbo.Listings_with_amenities_London$ on 
MyDatabase.dbo.London_Reservations.listing_id = MyDatabase.dbo.Listings_with_amenities_London$.id''', conn)
df = pd.DataFrame(sql_query)
df.to_csv("London_Reservations_Final.csv")

sql_query = pd.read_sql_query('''select MyDatabase.dbo.Listings_with_amenities_NYC$.id, MyDatabase.dbo.Listings_with_amenities_NYC$.no_of_amenities, 
MyDatabase.dbo.Listings_with_amenities_NYC$.price, MyDatabase.dbo.NewYork_Reservations.Month_Year_Combination, MyDatabase.dbo.NewYork_
Reservations.reservations from MyDatabase.dbo.NewYork_Reservations left join  MyDatabase.dbo.Listings_with_amenities_NYC$ on MyDatabase.dbo.NewYork_
Reservations.listing_id = MyDatabase.dbo.Listings_with_amenities_NYC$.id''', conn)
df = pd.DataFrame(sql_query)
df.to_csv("NewYork_Reservations_Final.csv")
