"""
STEP 1: LOAD & INSPECT
----------------------
What this file does:
  Reads the raw Excel file and prints a quick health check --
  shape, column types, and how many values are missing in each
  column. This is always the first thing you do with a new
  dataset, before changing anything.
"""

import pandas as pd


def load_data(path):
    """Read the raw Excel file into a DataFrame."""
    df = pd.read_excel(path)
    return df


def inspect_data(df):
    """Print a quick summary so we know what we're working with."""
    print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns")
    print(f"\nColumn types:\n{df.dtypes}")
    print(f"\nMissing values per column:\n{df.isnull().sum()}")
    print(f"\nDuplicate OrderIDs: {df['OrderID'].duplicated().sum()}")
    return df


if __name__ == "__main__":
    df = load_data("data/raw/Dataset_for_Data_Analytics.xlsx")
    inspect_data(df)