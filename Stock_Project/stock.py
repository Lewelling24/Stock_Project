import requests

# This class is set up to make use of 12 data api
apiKey = ""
stock_symbol = "VOO"
time_interval = "1day"
request_data_format = "JSON"


def get_data(api_key, interval, symbol, data_format):
    response = requests.get(
        "https://api.twelvedata.com/time_series?apikey=" + api_key + "&interval=" + interval + "&symbol=" + symbol
        + "&start_date=2024-06-06 19:25:00&end_date=2024-06-07 19:25:00&format=" + data_format)
    return response.json()


class StockData:
    apiKey = ""
    stock_symbol = ""
    time_interval = ""
    request_data_format = ""

    def set_api_key(self, api_key):
        self.apiKey = api_key

    def set_stock_symbol(self, stocksymbol):
        self.stock_symbol = stocksymbol
        
    def set_time_interval(self, timeinterval):
        self.time_interval = timeinterval
        
    def set_request_data_format(self, data_format):
        self.request_data_format = data_format


        


