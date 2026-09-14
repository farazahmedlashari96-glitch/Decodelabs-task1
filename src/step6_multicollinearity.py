"""
STEP 6: CHECK MULTICOLLINEARITY
---------------------------------
What this file does:
  Looks for pairs of numeric columns that are more than 80%
  correlated with each other and drops the weaker one.
"""

import numpy as np
import pandas as pd

TARGET_COLUMN = "TotalPrice"


def find_high_correlation_pairs(df_model, threshold=0.80):
    """Return column pairs (excluding the target) correlated above threshold."""
    numeric_cols = df_model.select_dtypes(include=[np.number]).columns.tolist()
    numeric_cols = [c for c in numeric_cols if c != TARGET_COLUMN]

    corr_matrix = df_model[numeric_cols].corr().abs()
    upper_tri = corr_matrix.where(
        np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
    )

    pairs = [
        (row, col, upper_tri.loc[row, col])
        for col in upper_tri.columns
        for row in upper_tri.index
        if pd.notna(upper_tri.loc[row, col]) and upper_tri.loc[row, col] > threshold
    ]
    return pairs


def remove_multicollinearity(df_model):
    """Drop the weaker column from each highly-correlated pair."""
    pairs = find_high_correlation_pairs(df_model)
    print(f"High-correlation pairs found (>0.80): {pairs}")

    cols_to_drop = set()
    for col1, col2, corr_val in pairs:
        corr1 = abs(df_model[col1].corr(df_model[TARGET_COLUMN]))
        corr2 = abs(df_model[col2].corr(df_model[TARGET_COLUMN]))
        drop_col = col2 if corr1 >= corr2 else col1
        cols_to_drop.add(drop_col)
        print(f"  {col1} vs {col2} (corr={corr_val:.2f}) -> dropping '{drop_col}'")

    print(
        "\nReminder: Quantity and UnitPrice directly construct TotalPrice. "
        "If TotalPrice is your modeling target, exclude Quantity and "
        "UnitPrice from your feature set manually to avoid data leakage."
    )

    if cols_to_drop:
        df_model = df_model.drop(columns=list(cols_to_drop))

    print(f"Shape after collinearity cleanup: {df_model.shape}")
    return df_model


if __name__ == "__main__":
    from step1_load_inspect import load_data
    from step2_handle_missing import handle_missing_values
    from step3_handle_outliers import handle_outliers
    from step4_feature_engineering import engineer_features
    from step5_encode_categorical import encode_categorical

    df = load_data("data/raw/Dataset_for_Data_Analytics.xlsx")
    df = handle_missing_values(df)
    df = handle_outliers(df)
    df = engineer_features(df)
    df_model = encode_categorical(df)
    df_model = remove_multicollinearity(df_model)