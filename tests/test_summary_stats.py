import pytest
import os
import sys
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.summary_stats import get_summary_stats

@pytest.fixture
def toy_df():
    return pd.DataFrame({
        "restaurant": ["Mekdi", "PizzaHut", "Ham Burger", "Chef Pin", "Subway", "Chef Tony", "Pho 67"],
        "star": [2.5, 3.2, 1.4, 4.8, 3.6, 4.5, 4.4],
        "city": ["Vancouver", "Toronto", "Montreal", "Richmond", "Brampton", "Richmond", "Calgary"],
        "category_1": ["American", "French", "American", "Chinese", "Western", "Chinese", "Vietnamese"],
        "price_range": ["$", "$", "$$", "$$$", "$", "$$$$", "$$$"],
        "category_2": ["burger", "pizza", "burger", "dry pot", "sandwich", "stir fry", "soup"],
    })

@pytest.fixture
def toy_df2():
    return pd.DataFrame({
        "restaurant": ["Mekdi", "PizzaHut", "Ham Burger"],
        "star": [2.5, 3.2, 1.4],
        "city": ["Vancouver", "Toronto", "Montreal"],
        "category_1": ["American", "French", "American"],
        "price_range": ["$", "$", "$$"],
        "category_2": ["burger", "pizza", "burger"],
    })


@pytest.fixture
def toy_df3():
    return pd.DataFrame({
        "restaurant": ["Ham Burger", "Chef Pin", "Subway", "Chef Tony", "Pho 67"],
        "star": [1.4, 4.8, 3.6, 4.5, 4.4],
        "city": ["Montreal", "Richmond", "Brampton", "Richmond", "Calgary"],
        "category_1": ["American", "Chinese", "Western", "Chinese", "Vietnamese"],
        "price_range": ["$$", "$$$", "$", "$$$$", "$$$"],
        "category_2": ["burger", "dry pot", "sandwich", "stir fry", "soup"],
    })


@pytest.fixture
def empty_df():
    return pd.DataFrame({
        "restaurant": [],
        "star": [],
        "city": [],
        "category_1": [],
        "price_range": [],
        "category_2": [],
    })


@pytest.fixture
def toy_df4():
    return pd.DataFrame({
        "restaurant": ["Pho 67"],
        "star": [4.4],
        "city": ["Calgary"],
        "category_1": ["Vietnamese"],
        "price_range": ["$$$"],
        "category_2": ["soup"],
    })

def test_output_right_structure(toy_df):
    """ 
    Test to verify that output is a dict type and it has two pair of keys and values
    (length of 2) which has "n_restaurants" and "avg_rating".
    """
    result = get_summary_stats(toy_df)
    assert isinstance(result, dict)
    assert len(result) == 2
    assert "n_restaurants" in result
    assert "avg_rating" in result


def test_aggregate_values(toy_df, toy_df2, toy_df3, toy_df4):
    """ 
    Test if the values of the results (total number of restaurants and average 
    rating) are accurate.
    """
    result = get_summary_stats(toy_df)
    result2 = get_summary_stats(toy_df2)
    result3 = get_summary_stats(toy_df3)
    result4 = get_summary_stats(toy_df4)
    assert result["n_restaurants"] == 7
    assert result["avg_rating"] == 24.4 / 7
    assert result2["n_restaurants"] == 3
    assert result2["avg_rating"] == 7.1 / 3
    assert result3["n_restaurants"] == 5
    assert result3["avg_rating"] == 18.7 / 5

    # test for one row only dataframe
    assert result4["n_restaurants"] == 1
    assert result4["avg_rating"] == 4.4


def test_empty_df(empty_df):
    """ 
    Test if the data frame is empty, it will give values of zeros.
    """
    result = get_summary_stats(empty_df)
    assert result["n_restaurants"] == 0.0
    assert result["avg_rating"] == 0.0
