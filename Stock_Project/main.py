from stock import get_data

# quick test

api_key = ""
symbol = "VOO"
time_interval = "1min"
data_format = "JSON"

stock_data = get_data(api_key, time_interval, symbol, data_format)

print(stock_data.json())
