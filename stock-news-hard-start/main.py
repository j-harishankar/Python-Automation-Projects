import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid = "ACb138b03ac85b2e8eab58da845a00c987"
auth_token = "8a697ac1e460b62ae1dd8d487b89d8f0"
STOCK_API = "SD9W87UZE72UQAW4"
NEWS_API  = "815c69246e5c4afb954e0d917da3ba13"
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
## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 



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

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.


#Optional: Format the SMS message like this: 
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
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

