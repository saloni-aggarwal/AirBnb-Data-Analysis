import pyodbc
server = "DESKTOP-1RMQQ1M"
database = "MyDatabase"

# setting up connection with SMSS
conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=DESKTOP-1RMQQ1M;'
                      'Database=MyDatabase;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

# executing some basic queries
cursor.execute('SELECT * FROM MyDatabase.dbo.[\'Calendar_London_Preprocessed - $\']')
cursor.execute('SELECT DISTINCT MyDatabase.dbo.London_listings_cleaned$.neighbourhood_cleansed FROM MyDatabase.dbo.London_listings_cleaned$')

cursor.execute('SELECT DISTINCT MyDatabase.dbo.NY_listings_cleaned$.neighbourhood_group_cleansed FROM MyDatabase.dbo.NY_listings_cleaned$')
cursor.execute('SELECT COUNT(MyDatabase.dbo.NY_listings_cleaned$.listing_id) AS TOTAL_IDS, MyDatabase.dbo.NY_listings_cleaned$.neighbourhood_group_cleansed FROM MyDatabase.dbo.NY_listings_cleaned$ GROUP BY MyDatabase.dbo.NY_listings_cleaned$.neighbourhood_group_cleansed ORDER BY TOTAL_IDS DESC')

cursor.execute('SELECT COUNT(MyDatabase.dbo.London_listings_cleaned$.id) AS TOTAL_IDS, MyDatabase.dbo.London_listings_cleaned$.neighbourhood_cleansed FROM MyDatabase.dbo.London_listings_cleaned$ GROUP BY MyDatabase.dbo.London_listings_cleaned$.neighbourhood_cleansed ORDER BY TOTAL_IDS DESC')









