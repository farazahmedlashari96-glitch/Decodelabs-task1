"""
MAIN.PY -- RUNS THE WHOLE PROJECT
-----------------------------------
This is the only file you actually need to run. It calls each
step file in order (1 -> 2 -> 3 -> 4 -> 5 -> 6).
"""

from step1_load_inspect import load_data, inspect_data
from step2_handle_missing import handle_missing_values
from step3_handle_outliers import handle_outliers
from step4_feature_engineering import engineer_features
from step5_encode_categorical import encode_categorical
from step6_multicollinearity import remove_multicollinearity

RAW_PATH = "data/raw/Dataset_for_Data_Analytics.xlsx"
MODEL_OUTPUT_PATH = "data/processed/cleaned_dataset_for_modeling.xlsx"
READABLE_OUTPUT_PATH = "data/processed/cleaned_dataset_readable.xlsx"


def run_pipeline():
    print("STEP 1: LOAD & INSPECT")
    df = load_data(RAW_PATH)
    df = inspect_data(df)

    print("STEP 2: HANDLE MISSING VALUES")
    df = handle_missing_values(df)

    print("STEP 3: HANDLE OUTLIERS")
    df = handle_outliers(df)

    print("STEP 4: FEATURE ENGINEERING")
    df = engineer_features(df)

    df.to_excel(READABLE_OUTPUT_PATH, index=False)

    print("STEP 5: ENCODE CATEGORICAL COLUMNS")
    df_model = encode_categorical(df)

    print("STEP 6: CHECK MULTICOLLINEARITY")
    df_model = remove_multicollinearity(df_model)

    df_model.to_excel(MODEL_OUTPUT_PATH, index=False)

    print("DONE")
    print(f"Model-ready file saved to  : {MODEL_OUTPUT_PATH}")
    print(f"Readable file saved to     : {READABLE_OUTPUT_PATH}")


if __name__ == "__main__":
    run_pipeline()