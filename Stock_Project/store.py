import pandas as pd


class StoreData:
    csv_file_path = ""
    data_frame = any

    def __init__(self, file_path=""):
        self.csv_file_path = file_path

    def build_dataframe(self, json_data):
        self.data_frame = pd.json_normalize(json_data)

    # store data in a csv
    def dataframe_to_csv(self):
        self.data_frame.to_csv(self.csv_file_path)
