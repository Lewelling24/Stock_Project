import requests


# This class is set up to make use of 12 data api
# class designed for easy calls to the 12 data api

class StockData:
    apiKey = ""
    stock_symbol = ""
    time_interval = ""
    request_data_format = ""

    def __init__(self, apikey="", symbol="", interval="", dataformat=""):
        self.apiKey = apikey
        self.stock_symbol = symbol
        self.time_interval = interval
        self.request_data_format = dataformat

    def set_api_key(self, api_key):
        self.apiKey = api_key

    def set_stock_symbol(self, stocksymbol):
        self.stock_symbol = stocksymbol

    def set_time_interval(self, timeinterval):
        self.time_interval = timeinterval

    def set_request_data_format(self, data_format):
        self.request_data_format = data_format

    def get_data(self):
        response = requests.get(
            "https://api.twelvedata.com/time_series?apikey=" + self.apiKey + "&interval=" + self.time_interval
            + "&symbol=" + self.stock_symbol
            + "&start_date=2024-06-06 19:25:00&end_date=2024-06-07 19:25:00&format="
            + self.request_data_format)
        return response.json()
