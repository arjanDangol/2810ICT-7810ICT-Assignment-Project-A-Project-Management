import pandas as pd

# Load the listings dataset
listings_df = pd.read_csv("./dataset/listings_dec18.csv")

# Prompt the user for input
suburb = input("Enter the suburb (e.g., 'Bondi Beach'): ")
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# Filter the listings based on suburb and select specific columns
filtered_listings = listings_df[listings_df['city'] == suburb][[
    'id', 'name', 'description', 'street', 'city', 'state', 'zipcode'
]]

# Create an empty DataFrame to store the selected listings
selected_listings = []

# Loop through the filtered listings and check availability in the specified period
for index, row in filtered_listings.iterrows():
    listing_id = row['id']
    listing_calendar = pd.read_csv(f"./dataset/calendar_dec18.csv")
    listing_calendar['date'] = pd.to_datetime(listing_calendar['date'])

    # Filter calendar data for the specified date range and availability
    availability = listing_calendar[(listing_calendar['date'] >= start_date) & (listing_calendar['date'] <= end_date)]

    if availability['available'].str.lower().eq('t').any():
        # Append the selected listing data to the selected_listings DataFrame
        selected_data = row.to_dict()
        selected_listings.append(selected_data)

# Convert the list of dictionaries to a DataFrame
selected_listings_df = pd.DataFrame(selected_listings)

# Display the selected listings
if not selected_listings_df.empty:
    selected_listings_df.to_csv("selected_listings.csv", index=False)
    print(f"Listings in {suburb} available between {start_date} and {end_date}:")
    print(selected_listings_df)
else:
    print(f"No listings available in {suburb} between {start_date} and {end_date}.")
