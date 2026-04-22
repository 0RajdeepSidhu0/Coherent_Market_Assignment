import pandas as pd


def load_data(path="data/startups_raw.csv"):
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Drop duplicates
    df = df.drop_duplicates(subset=["link"])

    # Remove missing values
    df = df.dropna(subset=["name", "link"])

    # Standardize text
    df["name"] = df["name"].str.strip()
    df["link"] = df["link"].str.strip()

    # Optional: extract slug (useful for API/search)
    df["slug"] = df["link"].apply(lambda x: x.split("/")[-1])

    # Add metadata (good for "production feel")
    df["source"] = "ycombinator"

    return df


def save_clean_data(df: pd.DataFrame, path="data/startups_clean.csv"):
    df.to_csv(path, index=False)


def main():
    df = load_data()
    df_clean = clean_data(df)
    save_clean_data(df_clean)

    print(f"Cleaned data saved: {len(df_clean)} records")


if __name__ == "__main__":
    main()