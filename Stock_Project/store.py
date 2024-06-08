import pandas as pd

csv_file_path = "/home/kane/Code/Stock_Project/Stock_Project/stock.csv"


def build_dataframe(json_data):
    df = pd.json_normalize(json_data)
    return df


def dataframe_to_csv(df):
    df.to_csv(csv_file_path)
