# AirBnb-Data-Analysis

In this project, we developed two applications using Airbnb dataset for both hosts and travellers or we can say for producer and consumer. 

- The first application is called as Boosting Reservation which helps hosts to boost or increase their reservations. This was done by looking at the most and least
reservations in the listed AriBnb and by studying various factors that affect the reservations of an Aribnb. For training the model multivariate regression model
was used build.

- The second application was called as Price Prediction. This application is more benficial to the travellers that plan on booking an AirBnb to a city. When they 
provide up with the minimum requirements they need in an Airbnb, the application is able to predict the prices according to their needs. It depends on many factors like
type of neighborhood or city, number of bedrooms and bathrooms, etc. For this a clustering model was first built to find famous neighborhoods in a city and then this model 
along with other factors was given as input to a Linear Regression model with multiple factors.

For both the application Airbnb dataset was used which is openly available on AirBnb site. London and New York City data was downloaded which included three tables namely
Listings, Reviews and Calendar. For training the model 70% of the data was used and 30% of data was used for testing the model.
