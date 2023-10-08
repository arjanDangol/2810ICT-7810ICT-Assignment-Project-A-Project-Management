import pandas as pd

import matplotlib

matplotlib.use('WXAgg')

from matplotlib.figure import Figure


def show_plot(start_date, end_date):
    # Load the calendar dataset
    calendar_df = pd.read_csv("./dataset/calendar_dec18.csv")

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

    figure_score = Figure()
    ax = figure_score.add_subplot(111)
    ax.hist(average_price_by_listing_df['price'], bins=30, edgecolor='k', alpha=0.7)
    ax.set_xlabel('Average Price')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Prices by Listing ID (Histogram)')
    ax.grid(True)

    print("Figure Score", figure_score)
    return figure_score

# show_plot("2018-07-10", "2019-01-10")
