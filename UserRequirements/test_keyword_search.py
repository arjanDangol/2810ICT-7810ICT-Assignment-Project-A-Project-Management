import pandas as pd
import pytest
from r3_keyword_search import retrieve_keyword_specific_listing


@pytest.fixture
def sample_data():
    keyword = "pool"
    start_date = "2019-12-06"
    end_date = "2019-12-06"
    return keyword, start_date, end_date


def test_retrieve_keyword_specific_listing_returns_dataframe(sample_data):
    keyword, start_date, end_date = sample_data
    result = retrieve_keyword_specific_listing(keyword, start_date, end_date)
    assert isinstance(result, pd.DataFrame), "The result should return dataframe"


def test_retrieve_keyword_specific_listing_contains_keyword(sample_data):
    keyword, start_date, end_date = sample_data
    result = retrieve_keyword_specific_listing(keyword, start_date, end_date)
    if not result.empty:
        assert any(keyword.lower() in str(row).lower() for row in
                   result.itertuples(index=False)), "The result should contain the keyword"


def test_retrieve_keyword_specific_listing_at_least_one_column(sample_data):
    keyword, start_date, end_date = sample_data
    result = retrieve_keyword_specific_listing(keyword, start_date, end_date)
    # Check if the result DataFrame is not empty
    assert not result.empty

    # Check if the keyword appears in any of the relevant columns
    relevant_columns = ['name', 'summary', 'space', 'description', 'notes', 'house_rules', 'amenities']
    keyword_found = any(result[col].str.contains(keyword, case=False, na=False).any() for col in relevant_columns)

    # Assert that the keyword appears in at least one relevant column
    assert keyword_found, "The keyword should be found in at least one column of dataframe"


def test_retrieve_keyword_specific_listing_empty_result(sample_data):
    keyword, start_date, end_date = sample_data
    # Assuming there are no listings with the keyword "nonexistentkeyword" in the dataset
    nonexistent_keyword_result = retrieve_keyword_specific_listing("nonexistentkeyword", start_date, end_date)
    assert nonexistent_keyword_result.empty, "The result should be empty if the keyword does not exist"
