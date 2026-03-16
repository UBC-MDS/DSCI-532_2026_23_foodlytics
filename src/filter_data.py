import pandas as pd

def filter_data(df: pd.DataFrame, cities: list = None, cuisines: list = None, 
                price_ranges: list = None, categories_2: list = None) -> pd.DataFrame:
    """
    Filter restaurant data set by cities, cuisines, price range, or food types (category 2).

    Note: If any ofthe filter parameter is not specified (=None), that filter will not be applied
    and all values are included.

    Parameters
    ----------
    df : pd.DataFrame
        The original restaurant data set.
    city : list, optional
        List of city names to filter.
    category_1 : list, optional
        List of cuisine types to filter.
    price_range : list, optional
        List of price range to filet (e.g. [$, $$, $$$]).
    category_2 : list, optional
        List of food type/other categories to filter

    Returns
    -------
    pd.DataFrame
        Filtered Data Frame.
    
    Examples
    --------
    >>> df = pd.DataFrame(toy_df)
    >>> len(filter_data(df, city=["Toronto"]))
    813
    >>> len(filter_data(df, category_1=["Italian"], price_range=["$"]))
    3
    """
    data = df.copy()
    if cities:
        data = data[data["city"].isin(cities)]
    if cuisines:
        data = data[data["category_1"].isin(cuisines)]
    if price_ranges:
        data = data[data["price_range"].isin(price_ranges)]
    if categories_2:
        data = data[data["category_2"].isin(categories_2)]
    return data

