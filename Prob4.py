import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def clean_and_preprocess(df):
    for column in df.columns:
        if df[column].dtype == "object":
            df[column].fillna(df[column].mode()[0], inplace=True)
        else:
            df[column].fillna(df[column].median(), inplace=True)

    numerical_cols = df.select_dtypes(include=["float64", "int64"]).columns
    scaler = MinMaxScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    categorical_cols = df.select_dtypes(include=["object"]).columns
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    return df


data = {
    "A": [1, 2, None, 4, 5],
    "B": [None, "Y", "N", "Y", None],
    "C": [10, 20, 30, None, 50],
    "D": ["cat", "dog", "cat", None, "dog"],
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

cleaned_df = clean_and_preprocess(df)
print("\nCleaned and Preprocessed DataFrame:")
print(cleaned_df)
