from stock import StockData
from store import *

api_key = ""
symbol = "VOO"
time_interval = "1day"
data_format = "JSON"

stock_data = StockData(api_key, symbol, time_interval, data_format)
data = stock_data.get_data()

print(data.values.open)



#dataframe = build_dataframe(stock_data)

#dataframe_to_csv(dataframe)
