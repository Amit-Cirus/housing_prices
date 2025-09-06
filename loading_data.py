import argparse
import pandas as pd

def load_to_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def main():

    default_path = "C:/code_projects/housing_prices/train.csv"

    df = load_to_csv(default_path)
    print(df.head())

if __name__ == "__main__":
    main()
