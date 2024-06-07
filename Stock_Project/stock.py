import requests

#12 data api
apiKey = ""
symbol = "VOO"
interval = "1min"


def getData(apiKey, interval, symbol):
    response = requests.get("https://api.twelvedata.com/time_series?apikey="+apiKey+"&interval="+interval+"&symbol="+symbol
                        +"&start_date=2024-06-06 19:25:00&end_date=2024-06-07 19:25:00&format=JSON")
    return response