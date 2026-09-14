"""
STEP 2: HANDLE MISSING VALUES
-----------------------------
What this file does:
  Fixes the only column with missing data: CouponCode (25.75%
  missing). A missing CouponCode doesn't mean "data got lost" --
  it means the customer didn't use one. So instead of guessing
  a fake value (mean/median/KNN), we give it its own category:
  "NoCoupon". This keeps the meaning of the data intact.
"""


def handle_missing_values(df):
    """Fill missing CouponCode entries with a clear 'NoCoupon' label."""
    before = df.isnull().sum().sum()

    df["CouponCode"] = df["CouponCode"].fillna("NoCoupon")

    after = df.isnull().sum().sum()
    print(f"Missing values before: {before} | after: {after}")
    return df


if __name__ == "__main__":
    from step1_load_inspect import load_data

    df = load_data("data/raw/Dataset_for_Data_Analytics.xlsx")
    df = handle_missing_values(df)
    print(df["CouponCode"].value_counts())