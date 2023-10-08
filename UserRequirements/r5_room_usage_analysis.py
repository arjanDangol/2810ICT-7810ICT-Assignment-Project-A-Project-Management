import pandas as pd


def retrieve_room_usage_listings(start_date, end_date):
    # Load the calendar dataset
    calendar_df = pd.read_csv("./dataset/calendar_dec18.csv")

    # # Prompt the user for input
    # start_date = input("Enter the start date (YYYY-MM-DD): ")
    # end_date = input("Enter the end date (YYYY-MM-DD): ")

    # Convert date columns to datetime
    calendar_df['date'] = pd.to_datetime(calendar_df['date'])
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Filter the calendar data for the specified date range and available='t'
    filtered_calendar = calendar_df[
        (calendar_df['date'] >= start_date) &
        (calendar_df['date'] <= end_date) &
        (calendar_df['available'] == 't')
        ]

    # Count the number of times each room (listing) has been used within the date range
    room_usage_counts = filtered_calendar.groupby('listing_id').size().reset_index(name='usage_count')

    # Sort the DataFrame by 'usage_count' in ascending order
    room_usage_counts = room_usage_counts.sort_values(by='listing_id', ascending=True)

    # Display the resulting table data
    print(room_usage_counts.head(30))
    return room_usage_counts.head(30)


# retrieve_room_usage_listings("2018-04-06", "2019-04-06")
