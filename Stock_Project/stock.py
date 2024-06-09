import requests

# 12 data api
apiKey = ""
stock_symbol = "VOO"
time_interval = "1min"
request_data_format = "JSON"


def get_data(api_key, interval, symbol, data_format):
    response = requests.get(
        "https://api.twelvedata.com/time_series?apikey=" + api_key + "&interval=" + interval + "&symbol=" + symbol
        + "&start_date=2024-06-06 19:25:00&end_date=2024-06-07 19:25:00&format=" + data_format)
    return response.json()
