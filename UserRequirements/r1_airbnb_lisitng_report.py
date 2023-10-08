import pandas as pd
import dask.dataframe as dd

# Define the problematic rows to skip
skip_rows = [17514] # Add more line numbers if there are multiple problematic rows

# Specify a larger block_size and sample size to ensure enough data for processing
block_size = 256 * 1024 * 1024 # Adjust this value based on your system's memory and dataset size, 256 MiB in bytes
sample_size = 256 * 1024 * 1024 # Align sample size with block size, 256 MiB in bytes


def list_airbnb_listing(suburb, start_date, end_date):

    # Read dataframes as Dask dataframes for parallel processing
    listings_ddf = dd.read_csv("./dataset/listings_dec18.csv", skiprows=skip_rows, assume_missing=True, dtype=str,
                               blocksize=block_size, sample=sample_size)
    calendar_ddf = dd.read_csv("./dataset/calendar_dec18.csv", skiprows=skip_rows, assume_missing=True, dtype=str,
                               blocksize=block_size, sample=sample_size)

    # Filter listings based on suburb using Dask
    filtered_listings_ddf = listings_ddf[listings_ddf['city'] == suburb]
    filtered_listings_ddf = filtered_listings_ddf.rename(columns={'city': 'suburb'})

    # Filter calendar data for the specified date range and availability using Dask
    availability_ddf = calendar_ddf[
        (calendar_ddf['date'] >= start_date) &
        (calendar_ddf['date'] <= end_date) &
        (calendar_ddf['available'].str.lower() == 't')
        ]

    # Compute the Dask dataframes to pandas dataframes
    filtered_listings_df = filtered_listings_ddf.compute()
    availability_df = availability_ddf.compute()

    # Merge filtered listings with available dates based on listing ID
    selected_listings_df = pd.merge(
        filtered_listings_df,
        availability_df[['listing_id']],
        left_on='id',
        right_on='listing_id',
        how='inner'
    )
    selected_columns = ['id', 'suburb', 'description', 'name', 'street', 'state', 'zipcode']
    selected_listings_df = selected_listings_df[selected_columns]

    # Display the selected listings
    if not selected_listings_df.empty:
        print(f"Listings in {suburb} available between {start_date} and {end_date}:")
        return selected_listings_df[['id', 'suburb', 'description', 'name', 'street', 'state', 'zipcode']]
    else:
        print(f"No listings available in {suburb} between {start_date} and {end_date}.")


# Call the function to list Airbnb listings
# list_airbnb_listing()
