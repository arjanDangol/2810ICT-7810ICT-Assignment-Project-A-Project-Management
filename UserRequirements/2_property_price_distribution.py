import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the calendar dataset
calendar_df = pd.read_csv("./dataset/calendar_dec18.csv")

# Prompt the user for input
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# Filter the calendar data for the specified date range
filtered_calendar = calendar_df[(calendar_df['date'] >= start_date) & (calendar_df['date'] <= end_date)]

# Remove rows where the price is NaN or not available
filtered_calendar = filtered_calendar.dropna(subset=['price'])

# Convert the 'price' column from a string to a numeric value (remove '$' and ',')
filtered_calendar['price'] = filtered_calendar['price'].str.replace('[\$,]', '', regex=True).astype(float)

# Group the data by 'listing_id' and calculate the average price for each listing
average_price_by_listing = filtered_calendar.groupby('listing_id')['price'].mean()
average_price_by_listing_df = average_price_by_listing.reset_index()
print("Average Pricing: ", average_price_by_listing_df)

# Create a scatter plot to show the distribution of average prices by listing
plt.figure(figsize=(10, 6))
plt.scatter(average_price_by_listing_df['listing_id'], average_price_by_listing_df['price'], alpha=0.5)
plt.xlabel('Listing ID')
plt.ylabel('Price')
plt.title('Distribution of Prices by Listing ID (Scatter Plot)')
plt.grid(True)

# Create a histogram to show the distribution of average prices by listing
plt.figure(figsize=(10, 6))
plt.hist(average_price_by_listing_df['price'], bins=30, edgecolor='k', alpha=0.7)
plt.xlabel('Average Price')
plt.ylabel('Frequency')
plt.title('Distribution of Prices by Listing ID (Histogram)')
plt.grid(True)

# Show the chart
plt.show()

