import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
data = pd.read_csv('../../data/investing/combined_graph.csv')

# Extract the columns we want to plot
years = data['Year']
returns = data['S&P 500 Avg. Return']
funds_rate = data['Federal Funds Rate']
inflation_rate = data['Avg. Inflation Rate']

# Plot the data as line charts
fig, ax = plt.subplots()
ax.plot(years, returns, label='S&P 500 Avg. Return')
ax.plot(years, funds_rate, label='Federal Funds Rate')
ax.plot(years, inflation_rate, label='Avg. Inflation Rate')

# Add a legend and title
ax.legend()
ax.set_title('S&P 500 Returns, Fed Funds Rate, and Inflation Rate (1973-2020)')

# Show the plot
plt.show()
