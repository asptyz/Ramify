

import random

history = []

def get_delta(history: list[dict[str, int]]) -> float:
    return history[-1]["price"] - history[-2]["price"]

def make_decision(epoch: int, price: float):
    """
    Main function that determines the portfolio allocation at each epoch.
    
    Parameters
    ----------
    epoch : int
        The current epoch (time index) in the data series.
    price : float
        The current price of 'Asset A'.
    
    Returns
    -------
    dict
        A dictionary containing the portfolio distribution between assets.
        The keys must be exactly 'Asset A' and 'Cash'.
        The values must be numbers between 0 and 1, and their sum must equal 1.0.
        
    Example
    -------
    >>> make_decision(0, 100.5)
    {'Asset A': 0.3, 'Cash': 0.7}
    """

    history.append({"epoch": epoch, "price": price})
    if (len(history) < 2):
        return {'Asset A':0.5, 'Cash': 0.5}
    if get_delta(history) > 0:
        return {'Asset A':0.7, 'Cash': 0.3}
    else:
        return {'Asset A':0.3, 'Cash': 0.7}