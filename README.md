# Project 1: Advanced EDA & Feature Engineering

DecodeLabs Data Science Internship — Industrial Training Kit (Batch 2026)

## What this project does

Takes a raw, messy e-commerce orders dataset (1,200 rows) and turns it
into a clean, machine-learning-ready dataset by:

1. Filling in missing values sensibly
2. Detecting and capping outliers
3. Engineering 8 new predictive features
4. Encoding text categories into numbers
5. Removing redundant (highly correlated) features

## Folder structure

```
DataScience_Project1/
├── README.md                      <- you are here
├── requirements.txt                <- Python packages needed
├── data/
│   ├── raw/
│   │   └── Dataset_for_Data_Analytics.xlsx      <- original, untouched file
│   └── processed/
│       ├── cleaned_dataset_readable.xlsx        <- cleaned, human-readable
│       └── cleaned_dataset_for_modeling.xlsx    <- cleaned, fully numeric
├── src/
│   ├── step1_load_inspect.py       <- loads data, checks for problems
│   ├── step2_handle_missing.py     <- fixes missing CouponCode values
│   ├── step3_handle_outliers.py    <- caps extreme numeric values
│   ├── step4_feature_engineering.py<- creates 8 new columns
│   ├── step5_encode_categorical.py <- turns text into numbers
│   ├── step6_multicollinearity.py  <- removes redundant features
│   └── main.py                     <- runs all 6 steps in order
└── outputs/                        <- (empty; for your own charts/report)
```

## How to run it

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
2. From the project's root folder, run:
   ```
   python src/main.py
   ```
3. Watch the terminal — it prints what's happening at every step.
4. Check `data/processed/` for your two output files.

## File-by-file explanation (plain English)

| File | What it does |
|---|---|
| `step1_load_inspect.py` | Opens the Excel file and prints a health check: how many rows, what type each column is, and where values are missing. |
| `step2_handle_missing.py` | The only column with gaps is `CouponCode` (25.75% missing). A blank here means "no coupon used," not "data lost" — so it's filled with the label `"NoCoupon"` instead of a guessed number. |
| `step3_handle_outliers.py` | Uses the IQR (Interquartile Range) rule to find unusually high/low values in the numeric columns, then "caps" them at a sensible boundary instead of deleting rows. |
| `step4_feature_engineering.py` | Builds 8 new columns from existing ones — e.g., which day of the week an order happened, whether a coupon was used, average price per item in the cart. |
| `step5_encode_categorical.py` | Machine learning models only understand numbers. This turns columns like `Product` ("Laptop", "Phone"...) into 0/1 columns (One-Hot Encoding), and drops ID-like columns that don't help prediction. |
| `step6_multicollinearity.py` | Checks whether any two numeric columns are basically saying the same thing (>80% correlated) and drops the weaker one to keep the model's math stable. |
| `main.py` | The conductor — runs all six steps above in the correct order and saves the two final files. |

## Key findings from this dataset

- Only one column had missing data: `CouponCode` (25.75%)
- 8 outliers were found in `TotalPrice` — interesting because the two
  columns that build it (`Quantity`, `UnitPrice`) had **zero** outliers
  individually. Multiplying two "normal" numbers can still produce an
  extreme result.
- No pairs of features were more than 80% correlated after encoding,
  so no columns needed to be dropped for multicollinearity.
- `Quantity` and `UnitPrice` directly construct `TotalPrice`
  (`TotalPrice = Quantity × UnitPrice`). If `TotalPrice` becomes your
  prediction target in a later project, exclude `Quantity` and
  `UnitPrice` from your model's inputs to avoid data leakage.

## Contact

DecodeLabs — decodelabs.tech@gmail.com — Greater Lucknow, India