import pandas as pd
import matplotlib
import numpy as np
import pytest
from r2_property_price_distribution import show_plot

@pytest.fixture
def sample_data():
    start_date = "2018-07-10"
    end_date = "2019-01-10"
    return start_date, end_date

def test_show_plot_returns_figure(sample_data):
    start_date, end_date = sample_data
    figure = show_plot(start_date, end_date)
    assert isinstance(figure, matplotlib.figure.Figure), "Result should return figure"

def test_show_plot_has_correct_xlabel(sample_data):
    start_date, end_date = sample_data
    figure = show_plot(start_date, end_date)
    ax = figure.get_axes()[0]
    assert ax.get_xlabel() == 'Average Price', "The xlabel of plot should be Average Price"

def test_show_plot_has_correct_ylabel(sample_data):
    start_date, end_date = sample_data
    figure = show_plot(start_date, end_date)
    ax = figure.get_axes()[0]
    assert ax.get_ylabel() == 'Frequency', "The xlabel of plot should be Frequency"

def test_show_plot_has_non_negative_prices(sample_data):
    start_date, end_date = sample_data
    figure = show_plot(start_date, end_date)
    ax = figure.get_axes()[0]
    prices = [rect.get_height() for rect in ax.patches]
    assert all(price >= 0 for price in prices), "The value for the price should not be negative"

