import pytest
import pandas as pd
from r1_airbnb_lisitng_report import list_airbnb_listing


# Fixture to set up test data
@pytest.fixture
def sample_data():
    suburb = "Bondi Beach"
    start_date = "2019-10-01"
    end_date = "2019-10-06"
    return suburb, start_date, end_date


def test_list_airbnb_listing_with_valid_data(sample_data):
    suburb, start_date, end_date = sample_data
    result = list_airbnb_listing(suburb, start_date, end_date)
    assert isinstance(result, pd.DataFrame)
    assert not result.empty, "The data entered for the retrieval must be valid"


def test_list_airbnb_listing_with_invalid_suburb(sample_data):
    suburb, start_date, end_date = sample_data
    suburb = "Invalid Suburb"
    result = list_airbnb_listing(suburb, start_date, end_date)
    assert isinstance(result, pd.DataFrame)
    assert result.empty, "The invalid suburb must give out empty dataframe"


def test_list_airbnb_listing_with_invalid_date(sample_data):
    suburb, start_date, end_date = sample_data
    start_date = "2022-01-01"
    end_date = "2022-01-10"
    result = list_airbnb_listing(suburb, start_date, end_date)
    assert isinstance(result, pd.DataFrame)
    assert result.empty, "The invalid date must give out empty dataframe"

def test_list_airbnb_listing_with_invalid_date_range(sample_data):
    suburb, start_date, end_date = sample_data
    start_date = "2019-01-11"
    end_date = "2019-01-10"
    result = list_airbnb_listing(suburb, start_date, end_date)
    assert isinstance(result, pd.DataFrame)
    assert result.empty, "The invalid date range must give out empty dataframe"


# Add more test cases as needed
