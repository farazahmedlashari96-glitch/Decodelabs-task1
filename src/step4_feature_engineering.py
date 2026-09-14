"""
STEP 4: FEATURE ENGINEERING
----------------------------
What this file does:
  Creates 8 brand-new columns from the existing data -- things
  that aren't in the raw file but can help a model make better
  predictions.
"""


def engineer_features(df):
    """Add new predictive columns to the DataFrame."""
    df["OrderYear"] = df["Date"].dt.year
    df["OrderMonth"] = df["Date"].dt.month
    df["OrderDayOfWeek"] = df["Date"].dt.day_name()
    df["IsWeekendOrder"] = df["Date"].dt.dayofweek.isin([5, 6]).astype(int)

    df["HasCoupon"] = (df["CouponCode"] != "NoCoupon").astype(int)

    df["AvgItemPrice"] = (df["TotalPrice"] / df["ItemsInCart"]).round(2)

    df["IsReturnedOrCancelled"] = df["OrderStatus"].isin(
        ["Returned", "Cancelled"]
    ).astype(int)

    df["QuantityToCartRatio"] = (df["Quantity"] / df["ItemsInCart"]).round(3)

    new_cols = [
        "OrderYear", "OrderMonth", "OrderDayOfWeek", "IsWeekendOrder",
        "HasCoupon", "AvgItemPrice", "IsReturnedOrCancelled",
        "QuantityToCartRatio",
    ]
    print(f"Added {len(new_cols)} new features: {new_cols}")
    return df


if __name__ == "__main__":
    from step1_load_inspect import load_data
    from step2_handle_missing import handle_missing_values
    from step3_handle_outliers import handle_outliers

    df = load_data("data/raw/Dataset_for_Data_Analytics.xlsx")
    df = handle_missing_values(df)
    df = handle_outliers(df)
    df = engineer_features(df)
    print(df.head())