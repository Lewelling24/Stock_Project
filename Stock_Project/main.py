from stock import get_data
from store import *

api_key = ""
symbol = "VOO"
time_interval = "1min"
data_format = "JSON"

stock_data = get_data(api_key, time_interval, symbol, data_format)


dataframe = build_dataframe(stock_data)

print(dataframe)
# dataframe_to_csv(dataframe)
