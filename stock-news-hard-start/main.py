import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv() 
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
STOCK_API = os.getenv("STOCK_API")
NEWS_API = os.getenv("NEWS_API")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


stock_params = {
    "function" :"TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey": STOCK_API,
}
stock_response = requests.get(STOCK_ENDPOINT,stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_lst = [value for (key,value) in stock_data.items()]
yesterday_closing_price = stock_lst[0]["4. close"]
day_before_yes = stock_lst[1]["4. close"]

difference = abs(float(yesterday_closing_price)-float(day_before_yes))
up_down = None
if difference>0:
    up_down = "🔻"
else:
    up_down = "🔺"


percent_diff = (abs(difference)/float(yesterday_closing_price))* 100
print(percent_diff)



if percent_diff<5:
    parameters={
        "q": COMPANY_NAME,
        "apiKey": NEWS_API
    }
    top_3_l = []
    news_response = requests.get("https://newsapi.org/v2/everything",params=parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    content = news_data["articles"][:4]
    print(content)


formatted_articles = [
    f"{STOCK}:{up_down}{percent_diff}% Headline: {article['title']}.\nBrief: {article['description']}\n" 
    for article in content
]
client = Client(account_sid, auth_token)
for articles in formatted_articles:
    message = client.messages.create(
            body=articles,
            from_="+16188449732",
            to="+917994031462",
        )
print(message.status)


