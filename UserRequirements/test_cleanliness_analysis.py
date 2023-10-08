import pandas as pd
import pytest
from r4_cleanliness_analysis import retrieve_reviews_listing

@pytest.fixture
def sample_data():
    start_date = "2018-04-06"
    end_date = "2018-04-07"
    return start_date, end_date

def test_retrieve_reviews_listing_returns_dataframe(sample_data):
    start_date, end_date = sample_data
    result = retrieve_reviews_listing(start_date, end_date)
    assert isinstance(result, pd.DataFrame), "Result should return dataframe"

def test_retrieve_reviews_listing_contains_cleanliness_mentions(sample_data):
    start_date, end_date = sample_data
    result = retrieve_reviews_listing(start_date, end_date)
    if not result.empty:
        assert all(row['mentions_cleanliness'] for _, row in result.iterrows()), "Result should have cleanliness mentions"

def test_retrieve_reviews_listing_within_date_range(sample_data):
    start_date, end_date = sample_data

    # Convert start_date and end_date to Timestamp objects
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    result = retrieve_reviews_listing(start_date, end_date)
    if not result.empty:
        # Convert the 'date' column in the result DataFrame to Timestamp objects
        result['date'] = pd.to_datetime(result['date'])

        # Check if the dates are within the specified range
        assert all(start_date <= date <= end_date for date in result['date']), "The dates should be within the date range in result"

def test_retrieve_reviews_listing_empty_result(sample_data):
    start_date, end_date = sample_data
    # Assuming there are no reviews within the specified date range
    empty_result = retrieve_reviews_listing("2020-01-01", "2020-01-02")
    assert empty_result.empty, "Result should be empty if there is no data found"
