# Submission Guide - Phase 1

This document explains how to submit your trading bot on the hackathon platform.

## 📦 Submission File Preparation

### Create a ZIP Archive

You must create a ZIP file containing your `bot_trade.py` file. Here are the commands to create the archive:

#### On Linux/macOS:

```bash
# From the phase_1 folder
zip submission.zip bot_trade.py
``` 

### Include Additional Files

If your `bot_trade.py` file depends on other Python files (custom modules, utilities, etc.), you can include them in the same ZIP:

#### Example with multiple files:

```bash
#On Linux/macOS – Include bot_trade.py and other files
zip submission.zip bot_trade.py utils.py models.py

#Or include all Python files from a folder
zip submission.zip bot_trade.py helpers/*.py

```

**Important:**
- ✅ The `bot_trade.py` file must be at the root of the ZIP (not in a subfolder)
- ✅ All additional Python files must be accessible from `bot_trade.py`
- ✅ Do **NOT** include data files (CSV), the venv, or local configuration files
- ✅ Do **NOT** include the `main.py` file or files from the `scoring/` folder (already present on the platform)

## 🌐 Platform Submission

### 1. Access the Platform

Go to the hackathon platform:

**URL:** [https://hackathon-x-poc.ramify.fr](https://hackathon-x-poc.ramify.fr)

### 2. Log In

- Log in with Discord SSO

### 3. Fill the Submission Form

Once logged in:

1. Go to the submission section
2. Fill in the submission form with the following information:
   - **Bot name**: Give your bot a name
   - **ZIP file**: Upload your `submission.zip` file
3. Submit the form

### 4. Confirmation

After submission, you should receive a confirmation that your bot has been received and is waiting to be executed.

## 📊 View Results

The dashboard displays:

- **📈 Performance Scores**:
  - Sharpe Score
  - PnL Score
  - Max Drawdown Score
  - Base Score (overall score)

- **📋 Execution Logs**:
  - Detailed logs of your bot's execution
  - Any errors (if the submission failed)
  - Validation messages

- **⏱️ Status**:
  - Submission status (pending, running, completed, error)
  - Submission date and time
  - Execution date and time

## ⚠️ Important Points

### Before Submitting

- ✅ Test your bot locally with `python3 main.py data/asset_a_test.csv`
- ✅ Check that your `make_decision` function matches the exact required signature
- ✅ Make sure the return format is correct (a dictionary with 'Asset A' and 'Cash')
- ✅ If you use additional files, test that they work correctly together

## 📞 Support

If you have any problem during submission or any questions, contact the hackathon team via Discord.