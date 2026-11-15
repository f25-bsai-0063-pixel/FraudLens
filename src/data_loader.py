import os
import pandas as pd

# Default location of the dataset, relative to the project root
DATA_PATH = os.path.join("data", "creditcard.csv")


def load_data(path=DATA_PATH):
    """Read the credit card CSV and return it as a DataFrame."""
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Dataset not found at '{path}'. "
            "Download creditcard.csv from Kaggle and put it in the data/ folder."
        )
    df = pd.read_csv(path)
    return df


def basic_info(df):
    """Print a quick summary so we know what we are working with."""
    print("Shape (rows, columns):", df.shape)
    print("\nColumn names:")
    print(list(df.columns))
    print("\nMissing values per column:")
    print(df.isnull().sum().sum(), "missing values in total")
    print("\nDuplicate rows:", df.duplicated().sum())


def class_balance(df):
    """Show how many transactions are legitimate (0) vs fraud (1)."""
    counts = df["Class"].value_counts()
    percent = df["Class"].value_counts(normalize=True) * 100
    print("\nClass distribution:")
    print("Legitimate (0):", counts[0], f"({percent[0]:.2f}%)")
    print("Fraud (1):     ", counts[1], f"({percent[1]:.3f}%)")


if __name__ == "__main__":
    data = load_data()
    print(data.head())
    basic_info(data)
    class_balance(data)