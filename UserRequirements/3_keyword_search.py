import pandas as pd

# Load the relevant datasets
calendar_df = pd.read_csv("./dataset/calendar_dec18.csv")
listings_df = pd.read_csv("./dataset/listings_dec18.csv")
reviews_df = pd.read_csv("./dataset/reviews_dec18.csv")

# Prompt the user for input
keyword = input("Enter a keyword to search for (e.g., 'pool', 'pet'): ")
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# Filter the calendar data for the specified date range and keyword
filtered_calendar = calendar_df[(calendar_df['date'] >= start_date) & (calendar_df['date'] <= end_date)]
filtered_calendar = filtered_calendar[filtered_calendar['listing_id'].isin(listings_df['id'])]

# Filter the listing data to include only records containing the keyword
filtered_listings = listings_df[
    (listings_df['name'].str.contains(keyword, case=False, na=False)) |
    (listings_df['summary'].str.contains(keyword, case=False, na=False)) |
    (listings_df['space'].str.contains(keyword, case=False, na=False)) |
    (listings_df['description'].str.contains(keyword, case=False, na=False)) |
    (listings_df['notes'].str.contains(keyword, case=False, na=False)) |
    (listings_df['house_rules'].str.contains(keyword, case=False, na=False)) |
    (listings_df['amenities'].str.contains(keyword, case=False, na=False))
]

# Select specific columns from the filtered listings data
selected_columns = ['id', 'name', 'summary', 'space', 'description', 'notes', 'house_rules', 'amenities']
filtered_listings = filtered_listings[selected_columns]

print("\nFiltered Listings Data:")
print(filtered_listings.head(10))
