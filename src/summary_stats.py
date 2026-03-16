import pandas as pd

def get_summary_stats(df: pd.DataFrame) -> dict:
    """
    Summarizes a given filtered pandas Data Frame into 
    a dict of the total number of restaurants and 
    average rating

    Note: It is assummed and expected that the dataframe 
    contains the 'star' column which has restaurant rating
    values.

    Parameters
    ----------
    df : pd.DataFrame
        The original restaurant data set.

    Returns
    -------
    dict
        dict of two values: total # of restaurants &
        average rating.
    
    Examples
    --------
    >>> toy_df = pd.DataFrame({
        "restaurant": ["Mekdi", "PizzaHut", "Ham Burger", "Chef Pin"],
        "ratings": [2.5, 3.2, 1.4, 4.8]
        "city": ["Vancouver", "Toronto", "Montreal", "Richmond"],
        "category_1": ["American", "French", "American", "Chinese"],
        "price_range": ["$", "$", "$$", "$$$"],
        "category_2": ["burger", "pizza", "burger", "dry pot"],
        })
    >>> summary_stats(df)
    {"n_restaurants": 4, "avg_rating": 3.0}
    """
    n = len(df)
    avg = df["star"].mean() if n else 0.0
    return {"n_restaurants": n, "avg_rating": avg}