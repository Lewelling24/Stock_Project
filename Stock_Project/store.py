import pandas as pd

csv_file_path = ""


def build_dataframe(json_data):
    df = pd.json_normalize(json_data, sep="\n")
    return df


def dataframe_to_csv(df):
    df.to_csv(csv_file_path)
