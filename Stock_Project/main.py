from stock import getData

#quicktest

apiKey = ""
symbol = "VOO"
interval = "1min"

stock_data = getData(apiKey,interval, symbol)

print(stock_data.json())
