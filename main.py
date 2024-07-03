import requests
STOCK_NAME = "NVDA"
COMPANY_NAME = "Nvidia Corporation"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "QAD9MV4IVMEO1QBF"
NEWS_API_KEY = "7123ece7755b49199b808bc9a6be3324"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
list_data = [value for (key, value) in data.items()]
yesterday_data = list_data[0]
yesterday_cl_price = yesterday_data["4. close"]
print(yesterday_cl_price)

day_b_yesterday_data = list_data[1]
day_b_yesterday_cl_price = day_b_yesterday_data["4. close"]
print(day_b_yesterday_cl_price)

