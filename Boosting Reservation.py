import statistics

import pandas as pd
import math
from sklearn import linear_model
import sklearn
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np


def mape(actual, predicted):
    return np.mean(np.abs((actual - predicted) / actual)) * 100


# reading datasets
london = pd.read_csv('London_Reservations_Final.csv')
nyc = pd.read_csv("NewYork_Reservations_Final.csv")

# preparing regression model
reg = linear_model.LinearRegression()
reg1 = linear_model.LinearRegression()

# dividing datasets into training and test sets
lx_train, lx_test, ly_train, ly_test = train_test_split(london[['no_of_amenities', 'price']], london.reservations,
                                                        test_size=0.3, random_state=0)
nx_train, nx_test, ny_train, ny_test = train_test_split(nyc[['no_of_amenities', 'price']], nyc.reservations,
                                                        test_size=0.3, random_state=0)
# building regression model with training set
reg.fit(lx_train, ly_train)
reg1.fit(nx_train, ny_train)

print(len(ly_test))
# predicting values of test set
l_pred = reg.predict(lx_test)
print("l_pred", l_pred)
n_pred = reg1.predict(nx_test)
print(len(l_pred))
# computing r^2 score for regression model
print('london', reg.score(lx_test, ly_test))
print('nyc', reg.score(nx_test, ny_test))
# computing MSE for regression model
mse = sklearn.metrics.mean_squared_error(ly_test, l_pred)
math.sqrt(mse)
print("mse: ", math.sqrt(mse))

variancel = statistics.variance(ly_test)
variancen = statistics.variance(ny_test)
print("variancel", variancel)
print('print(variancen)',variancen)

msel = variancel * (1 - 0.6132)
msen = variancen * (1 - 0.6476)
print("london msel = ", msel)
print("new york msen =", msen)

result = mape(ly_test, l_pred)
result1 = mape(ny_test, n_pred)
print("MAPE: London ", result)
print("MAPE: New York ", result1)
