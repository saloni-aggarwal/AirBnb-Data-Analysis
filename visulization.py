import pandas as pd
import matplotlib.pyplot as plt

# performing visualizations
file = pd.read_csv("PropertyVsAcceptanceRateLondon.csv")

# preparing a bar graph
plt.bar(file['property_type'], file['Total_Count'])
plt.xlabel("Property type")
plt.ylabel("Number of properties")
plt.title("Top 10 properties in London")
plt.show()

file = pd.read_csv("PropertyVsAcceptanceRateNY.csv")

plt.bar(file['property_type'], file['Total_Count'])
plt.xlabel("Property type")
plt.ylabel("Number of properties")
plt.title("Top 10 properties in New York")
plt.show()