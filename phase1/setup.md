# Submission Guide - Phase 1

This document explains how to create and submit your trading bot for Phase 1 of the hackathon.

## 📋 Required Structure

### `bot_trade.py` File

You must create a file named **`bot_trade.py`** at the root of the `phase_1/` folder. This file must contain a mandatory function with the exact following signature:

```python
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
    # Your trading logic here
    return {'Asset A': 0.3, 'Cash': 0.7}
```

### Return Format
The `make_decision` function must return a Python dictionary with the following characteristics:

- Mandatory Keys: `'Asset A'` and `'Cash'` (exactly these names).
- Values: Floats or integers between 0 and 1 (inclusive).
- Sum: The sum of the values must be exactly equal to 1.0.

**Valid Examples:**

```Python

{'Asset A': 0.3, 'Cash': 0.7}      # 30% in Asset A, 70% in Cash
{'Asset A': 1.0, 'Cash': 0.0}      # 100% in Asset A, 0% in Cash
{'Asset A': 0.0, 'Cash': 1.0}      # 0% in Asset A, 100% in Cash
{'Asset A': 0.5, 'Cash': 0.5}      # 50% in Asset A, 50% in Cash
Invalid Examples:
```

```Python

{'Asset A': 0.3, 'Cash': 0.6}      # ❌ Sum = 0.9 (must be 1.0)
{'Asset A': 0.3, 'Cash': 0.8}      # ❌ Sum = 1.1 (must be 1.0)
{'Asset': 0.5, 'Cash': 0.5}        # ❌ Incorrect key (must be 'Asset A')
{'Asset A': -0.1, 'Cash': 1.1}     # ❌ Values out of bounds [0, 1]
```

## 🧪 Testing Your Bot

### Test Command
To test your bot, use the test program provided by Ramify:

```Bash
python3 main.py data/asset_a_test.csv
```

**Arguments:**

- **First argument**: The main.py file (executed directly).
- **Second argument**: The path to the test dataset (e.g., `data/asset_a_test.csv`).

### Displaying the Performance Graph

To visualize a graph representing your bot's performance, add the `--show-graph` parameter:

```Bash
python3 main.py data/asset_a_test.csv --show-graph
```

The graph will display:
- The evolution of PnL (Profit and Loss) over time.
- Profit zones (green) and loss zones (red).
- The initial capital reference line.

### Displayed Results
Upon execution, the program will display:

1. **Scores**:
    -Sharpe Score
    -PnL Score
    -Max Drawdown Score
    -Base Score (overall score)

2. **Graph** (if `--show-graph` is used):
    - PnL evolution curve
    - Performance visualization

## 📦 Environment Setup
To configure the development environment with all necessary dependencies, simply run the provided shell script:

**Important**: Before running the script, you must make it executable using the `chmod` command:


```bash
chmod +x setup_env.sh
```
Then, run the script:

```bash
./setup_env.sh
```

This script will:
1. Create a Python virtual environment (if it doesn't already exist).
2. Automatically install all required libraries from `requirement.txt.`
3. Start a new shell with the virtual environment activated.


Once the new shell is launched, you will have access to all installed libraries:
- `matplotlib`: For displaying graphs.
- `pandas`: For data manipulation.
- `numpy: For` numerical calculations.
**Note**: To exit the shell with the activated environment, simply type `exit` to return to your previous shell.

## ⚠️ Validation
The test program automatically validates your make_decision function:

-✅ Verification of dictionary keys.
-✅ Verification that values are numeric.
-✅ Verification that values are between 0 and 1.
-✅ Verification that the sum of allocations equals 1.0.
If validation fails, an explicit error will be displayed with details of the problem.

##💡 Simple Bot Example
Here is a minimal example of bot_trade.py:

```Python
def make_decision(epoch: int, price: float):
    """
    Simple example: fixed 50/50 allocation
    """
    return {'Asset A': 0.5, 'Cash': 0.5}
```

## 📝 Important Notes

1. **File Name**: The file must be named exactly `bot_trade.py`.

2. **Function Name**: The function must be named exactly `make_decision (case sensitive)`.

3. **Signature**: The signature must be exactly `def make_decision(epoch: int, price: float):`.

4. **Return Format**: The dictionary must contain exactly the keys `'Asset A'` and `'Cash'`.

5. **Sum of Allocations**: The sum of values must be exactly 1.0 (tolerance of 0.00001).

6. **History**: You can maintain a price history within your file to implement history-based strategies.

## 🚀 Next Steps
Once your bot is tested locally and validated, you can submit it via the hackathon platform. The same validation system will be used during the official submission.