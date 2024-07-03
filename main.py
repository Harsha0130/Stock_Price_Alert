import requests
from twilio.rest import Client

STOCK_NAME = "NVDA"
COMPANY_NAME = "Nvidia Corporation"

acc_sid -- here
acc_token -- here

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "EHTQNX41N4R19TBZ"
NEWS_API_KEY = "7123ece7755b49199b808bc9a6be3324"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

news_params = {
    "q": STOCK_NAME,
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
print(response.json())
data = response.json()["Time Series (Daily)"]
list_data = [value for (key, value) in data.items()]

yesterday_data = list_data[0]
yesterday_cl_price = yesterday_data["4. close"]
print(yesterday_cl_price)

day_b_yesterday_data = list_data[1]
day_b_yesterday_cl_price = day_b_yesterday_data["4. close"]
print(day_b_yesterday_cl_price)

difference = float(yesterday_cl_price) - float(day_b_yesterday_cl_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

print(difference)

diff_per = round(difference / float(yesterday_cl_price)) * 100

if abs(diff_per) > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [(f"{STOCK_NAME}: {up_down}{diff_per}%\nHeadline: {article['title']}."
                           f"\nBrief: {article['description']}\nSource: {article['source']['name']}")
                          for article in three_articles]

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+14152879729",
            to="+91---UR_Number---",
        )
