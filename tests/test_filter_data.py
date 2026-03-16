import pytest
import os
import sys
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.filter_data import filter_data

@pytest.fixture
def toy_df():
    return pd.DataFrame({
        "restaurant": ["Mekdi", "PizzaHut", "Ham Burger", "Chef Pin"],
        "city": ["Vancouver", "Toronto", "Montreal", "Richmond"],
        "category_1": ["American", "French", "American", "Chinese"],
        "price_range": ["$", "$", "$$", "$$$"],
        "category_2": ["burger", "pizza", "burger", "dry pot"],
    })

def test_one_filter(toy_df):
    """ 
    Test to verify that a single filter correctly returns only matching rows, 
    ensuring filters work independently.
    """
    result = filter_data(toy_df, cities=["Toronto"])
    result2 = filter_data(toy_df, price_ranges=["$"] )
    result3 = filter_data(toy_df, categories_2=["burger", "dry pot"])
    assert len(result) == 1
    assert len(result2) == 2
    assert len(result3) == 3

def test_multiple_filter(toy_df):
    """ 
    Test if applying multiple filter categories work as expected, 
    ensuring filter works with multiple random filters.
    """
    result = filter_data(toy_df, cities=["Toronto", "Montreal"], price_ranges=["$", "$$$"])
    result2 = filter_data(toy_df, 
                          cities=["Toronto", "Vancouver", "Montreal"], 
                          price_ranges=["$", "$$"], 
                          categories_2=["burger", "pizza"],
                          cuisines=["American", "French"])
    assert len(result) == 1
    assert len(result2) == 3

def test_no_filter(toy_df):
    """ 
    Test if applying no filter category will include all values in the original data set,
    ensuring default function works as expected.
    """
    result = filter_data(toy_df)
    assert len(result) == len(toy_df)