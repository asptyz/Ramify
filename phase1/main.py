#! /usr/bin/env python3

import csv
import json
import os
import sys

# Prevent creation of __pycache__
sys.dont_write_bytecode = True


from scoring.scoring import get_local_score, show_result
import pandas as pd
from bot_trade import make_decision as decision_generator
import matplotlib.pyplot as plt


def find_csv_file(path_csv: str) -> pd.DataFrame:
    if not os.path.exists(path_csv):
        raise FileNotFoundError(f"The CSV file {path_csv} does not exist")
    prices_list = [
        pd.read_csv(path_csv, index_col=0)
    ]
    prices = pd.concat(prices_list, axis=1)
    prices["Cash"] = 1
    return prices

def validate_decision(decision: dict) -> bool:
    expected_keys = {'Asset A', 'Cash'}
    if set(decision.keys()) != expected_keys:
        print(f"ERROR: Expected keys are {expected_keys}, but received {set(decision.keys())}")
        return False

    for key, value in decision.items():
        if not isinstance(value, (int, float)):
            print(f"ERROR: The value for '{key}' is not numeric: {value}")
            return False
        if value < 0 or value > 1:
            print(f"ERROR: The value for '{key}' must be between 0 and 1, received: {value}")
            return False
    
    total = sum(decision.values())
    if abs(total - 1.0) > 0.00001:
        print(f"ERROR: The sum of allocations must be equal to 1, but is {total}")
        return False
    
    return True

def main():
    output = []

    if (len(sys.argv) > 1):
        path_csv = sys.argv[1]
        prices = find_csv_file(path_csv=path_csv)
    else:
        raise ValueError("No path to the csv file provided, ./main.py <path_to_csv>")

    for index, row in prices.iterrows():
        decision = decision_generator(int(index), float(row['Asset A']))
        if not validate_decision(decision):
            raise ValueError(f"Invalid decision: {decision}")
        decision['epoch'] = int(index)
        output.append(decision)
    positions = pd.DataFrame(output).set_index("epoch")
    local_score = get_local_score(prices=prices, positions=positions)
    if len(sys.argv) > 2 and sys.argv[2] == "--show-graph":
        show_result(local_score, is_show_graph=True)
    else:
        show_result(local_score, is_show_graph=False)
        print("\033[91mTo display the graph, use the --show-graph option: ./main.py <path_to_csv> --show-graph\033[0m")

if __name__ == "__main__":
    main()
