import pandas as pd

def retrieve_reviews_listing(start_date, end_date):
    # Load the reviews dataset
    reviews_df = pd.read_csv("./dataset/reviews_dec18.csv")

    # # Prompt the user for input
    # start_date = input("Enter the start date (YYYY-MM-DD): ")
    # end_date = input("Enter the end date (YYYY-MM-DD): ")

    # Define a list of keywords associated with cleanliness
    cleanliness_keywords = ['clean', 'cleanliness', 'tidy', 'neat', 'spotless', 'hygienic']

    # Function to check if a review comment contains cleanliness keywords
    def contains_cleanliness_keywords(comment):
        if isinstance(comment, str):
            comment = comment.lower()
            return any(keyword in comment for keyword in cleanliness_keywords)
        return False  # Return False for non-string values

    # Apply the function to the 'comments' column and create a new column 'mentions_cleanliness'
    reviews_df['mentions_cleanliness'] = reviews_df['comments'].apply(contains_cleanliness_keywords)

    # Convert date columns to datetime
    reviews_df['date'] = pd.to_datetime(reviews_df['date'])

    # Filter reviews within the user-selected date range
    reviews_df = reviews_df[(reviews_df['date'] >= start_date) & (reviews_df['date'] <= end_date)]
    print("Reviews: ", reviews_df)

    # Filter reviews_df where mentions_cleanliness is True
    cleanliness_reviews_df = reviews_df[reviews_df['mentions_cleanliness']]
    print("Cleanliness included:", cleanliness_reviews_df)

    # Count the number of comments mentioning cleanliness
    cleanliness_mentions_count = reviews_df['mentions_cleanliness'].sum()

    # Display the results
    print(f"Total comments mentioning cleanliness within the selected period: {cleanliness_mentions_count}")
    return cleanliness_reviews_df

# retrieve_reviews_listing("2018-04-06", "2018-04-07")