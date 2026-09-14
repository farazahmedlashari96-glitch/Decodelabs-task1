"""
STEP 3: HANDLE OUTLIERS (IQR METHOD)
-------------------------------------
What this file does:
  Checks every numeric column (Quantity, UnitPrice, ItemsInCart,
  TotalPrice) for extreme values using the Interquartile Range
  (IQR) rule. Any value outside the normal range gets "capped"
  (pulled back to the boundary) instead of deleted -- this way we
  never lose a single row of data.

  Extra care: TotalPrice = Quantity x UnitPrice by definition, so
  after capping we recompute TotalPrice to make sure that
  relationship still holds true.
"""

import numpy as np

NUMERIC_COLUMNS = ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]


def get_iqr_bounds(series):
    """Return the (lower, upper) acceptable range for a column."""
    q1, q3 = series.quantile(0.25), series.quantile(0.75)
    iqr = q3 - q1
    return q1 - 1.5 * iqr, q3 + 1.5 * iqr


def handle_outliers(df):
    """Cap outliers in each numeric column, then fix TotalPrice."""
    for col in NUMERIC_COLUMNS:
        lower, upper = get_iqr_bounds(df[col])
        n_outliers = ((df[col] < lower) | (df[col] > upper)).sum()
        print(f"{col}: bounds=({lower:.2f}, {upper:.2f}) -> {n_outliers} outliers capped")
        df[col] = np.clip(df[col], lower, upper)

    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
    return df


if __name__ == "__main__":
    from step1_load_inspect import load_data
    from step2_handle_missing import handle_missing_values

    df = load_data("data/raw/Dataset_for_Data_Analytics.xlsx")
    df = handle_missing_values(df)
    df = handle_outliers(df)
    print(df[NUMERIC_COLUMNS].describe())