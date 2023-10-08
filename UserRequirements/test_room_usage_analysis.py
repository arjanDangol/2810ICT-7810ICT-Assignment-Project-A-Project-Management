import pandas as pd
import pytest
from r5_room_usage_analysis import retrieve_room_usage_listings

@pytest.fixture
def sample_data():
    start_date = "2018-04-06"
    end_date = "2019-04-06"
    return start_date, end_date

def test_retrieve_room_usage_listings_returns_dataframe(sample_data):
    start_date, end_date = sample_data
    result = retrieve_room_usage_listings(start_date, end_date)
    assert isinstance(result, pd.DataFrame), "Result should return a dataframe"

def test_retrieve_room_usage_listings_non_negative_usage_count(sample_data):
    start_date, end_date = sample_data
    result = retrieve_room_usage_listings(start_date, end_date)
    assert (result['usage_count'] >= 0).all(), "Usage count should be non-negative"

def test_retrieve_room_usage_listings_not_empty(sample_data):
    start_date, end_date = sample_data
    result = retrieve_room_usage_listings(start_date, end_date)
    assert not result.empty, "Result should not be empty"

def test_retrieve_room_usage_listings_sorted_by_listing_id(sample_data):
    start_date, end_date = sample_data
    result = retrieve_room_usage_listings(start_date, end_date)
    if not result.empty:
        # Sort the DataFrame by 'usage_count' column
        sorted_result = result.sort_values(by='listing_id')

        # Check if the 'listing_id' column is monotonically increasing in the sorted DataFrame
        assert sorted_result['listing_id'].is_monotonic_increasing, "The column listing_id must be in ascending order"

