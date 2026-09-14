"""
STEP 5: ENCODE CATEGORICAL COLUMNS
------------------------------------
What this file does:
  Turns text categories into 0/1 columns using One-Hot Encoding.
  Drops identifier columns that don't help prediction.
"""

import pandas as pd

COLUMNS_TO_ENCODE = [
    "Product", "PaymentMethod", "OrderStatus",
    "ReferralSource", "CouponCode", "OrderDayOfWeek",
]

COLUMNS_TO_DROP = [
    "OrderID", "CustomerID", "ShippingAddress", "TrackingNumber", "Date",
]


def encode_categorical(df):
    """Drop identifier columns, then one-hot encode the rest."""
    df_model = df.drop(columns=COLUMNS_TO_DROP)
    df_model = pd.get_dummies(df_model, columns=COLUMNS_TO_ENCODE, drop_first=True)

    print(f"Dropped identifier columns: {COLUMNS_TO_DROP}")
    print(f"One-hot encoded: {COLUMNS_TO_ENCODE}")
    print(f"Shape after encoding: {df_model.shape}")
    return df_model


if __name__ == "__main__":
    from step1_load_inspect import load_data
    from step2_handle_missing import handle_missing_values
    from step3_handle_outliers import handle_outliers
    from step4_feature_engineering import engineer_features

    df = load_data("data/raw/Dataset_for_Data_Analytics.xlsx")
    df = handle_missing_values(df)
    df = handle_outliers(df)
    df = engineer_features(df)
    df_model = encode_categorical(df)
    print(df_model.head())