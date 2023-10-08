# import pandas as pd
#
#
# # Prompt the user for input
# # keyword = input("Enter a keyword to search for (e.g., 'pool', 'pet'): ")
# # start_date = input("Enter the start date (YYYY-MM-DD): ")
# # end_date = input("Enter the end date (YYYY-MM-DD): ")
#
# def retrieve_keyword_specific_listing(keyword, start_date, end_date):
#     # Load the relevant datasets
#     calendar_df = pd.read_csv("./dataset/calendar_dec18.csv")
#     listings_df = pd.read_csv("./dataset/listings_dec18.csv")
#     reviews_df = pd.read_csv("./dataset/reviews_dec18.csv")
#
#     # Filter the calendar data for the specified date range and keyword
#     filtered_calendar = calendar_df[(calendar_df['date'] >= start_date) & (calendar_df['date'] <= end_date)]
#     # selected_filtered_listing = filtered_calendar[filtered_calendar['listing_id'].isin(listings_df['id'])]
#
#     # Merge filtered listings with available dates based on listing ID
#     selected_filtered_listing = pd.merge(
#         listings_df,
#         filtered_calendar[['listing_id']],
#         left_on='id',
#         right_on='listing_id',
#         how='inner'
#     )
#
#     # Filter the listing data to include only records containing the keyword
#     filtered_listings = selected_filtered_listing[
#         (listings_df['name'].str.contains(keyword, case=False, na=False)) |
#         (listings_df['summary'].str.contains(keyword, case=False, na=False)) |
#         (listings_df['space'].str.contains(keyword, case=False, na=False)) |
#         (listings_df['description'].str.contains(keyword, case=False, na=False)) |
#         (listings_df['notes'].str.contains(keyword, case=False, na=False)) |
#         (listings_df['house_rules'].str.contains(keyword, case=False, na=False)) |
#         (listings_df['amenities'].str.contains(keyword, case=False, na=False))
#         ]
#
#     # Select specific columns from the filtered listings data
#     selected_columns = ['id', 'name', 'summary', 'space', 'description', 'notes', 'house_rules', 'amenities']
#     filtered_listings = filtered_listings[selected_columns]
#
#     print("\nFiltered Listings Data:")
#     print(filtered_listings)
#     return filtered_listings
#
#
# # retrieve_keyword_specific_listing("pool", "2019-12-06", "2019-12-06")

import pandas as pd

def retrieve_keyword_specific_listing(keyword, start_date, end_date):
    # Load the relevant datasets as Pandas dataframes
    calendar_df = pd.read_csv("./dataset/calendar_dec18.csv", dtype=str)
    listings_df = pd.read_csv("./dataset/listings_dec18.csv", dtype=str)

    # Filter the listings data for the specified keyword
    filtered_listings = listings_df[
        (listings_df['name'].str.contains(keyword, case=False, na=False)) |
        (listings_df['summary'].str.contains(keyword, case=False, na=False)) |
        (listings_df['space'].str.contains(keyword, case=False, na=False)) |
        (listings_df['description'].str.contains(keyword, case=False, na=False)) |
        (listings_df['notes'].str.contains(keyword, case=False, na=False)) |
        (listings_df['house_rules'].str.contains(keyword, case=False, na=False)) |
        (listings_df['amenities'].str.contains(keyword, case=False, na=False))
    ]

    # Filter the calendar data for the specified date range using Pandas
    filtered_calendar = calendar_df[
        (calendar_df['date'] >= start_date) &
        (calendar_df['date'] <= end_date) &
        (calendar_df['listing_id'].isin(filtered_listings['id']))
    ]

    # Merge filtered listings with available dates based on listing ID
    selected_filtered_listing = pd.merge(
        filtered_listings,
        filtered_calendar[['listing_id']],
        left_on='id',
        right_on='listing_id',
        how='inner'
    )

    # Select specific columns from the merged dataframe
    selected_columns = ['id', 'name', 'summary', 'space', 'description', 'notes', 'house_rules', 'amenities']
    filtered_listings = selected_filtered_listing[selected_columns]

    return filtered_listings
