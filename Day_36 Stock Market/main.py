import requests
from datetime import datetime, timedelta
from twilio.rest import Client


STOCK = "EICHERMOT"
COMPANY_NAME = "Royal Enfeild"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""




account_sid = "ACaebd41d636800afb03703d8cc17e23c2"
auth_token = "053dbd94d5f58195e056a7934f5f3d4d"



today = datetime.now().date()


month = today.month
day = today.day - 2
current_day = today.day -1
year = today.year

yesterday = today - timedelta(days=1)
day_before = today - timedelta(days=2)


stck_api = "https://www.alphavantage.co/query" #demo
stck_api_id = "Z9QJLFU82FPECKIR"

parameters = { "function" : "TIME_SERIES_DAILY", 
              "symbol" : "EICHERMOT.BSE",
              "apikey" : stck_api_id
              }

stck_response = requests.get(stck_api, params= parameters)
stck_response.raise_for_status()

data = stck_response.json()["Time Series (Daily)"]


yesterday_closing = float(data[f"{day_before:%Y-%m-%d}"]["4. close"])
today_open = float(data[f"{year:04d}-{month:02d}-{current_day:02d}"]["1. open"])

print(yesterday_closing, today_open)

change_in_price = today_open - yesterday_closing
print(round(change_in_price), 3)





news_api_id ="d9b15f4b261349bda33c84e3e7e0c3be"
news_api = "https://newsapi.org/v2/everything"
news_parameter = {"apiKey" : news_api_id,
                  "qInTitle" : "TATA MOTORS"
                  }

news_response = requests.get(news_api, news_parameter)
news_response.raise_for_status()

news_data_0 = news_response.json()["articles"][0]["title"]
news_data_1 = news_response.json()["articles"][1]["title"]
news_data_2 = news_response.json()["articles"][2]["title"]

titles = [article["title"] for article in news_response.json()["articles"][:3]]
news_data_0, news_data_1, news_data_2 = titles


print(news_data_1)
print(news_data_0)
print(news_data_2)


client = Client(account_sid, auth_token)
message = client.messages.create(
        body=f"{STOCK} news alert, price close: {yesterday_closing}, price open : {today_open} difference : {change_in_price} news Highlihgts {news_data_0, news_data_1, news_data_2}",
        from_="+16825028861",
        to="+919999999999"
    )
print(message.status)

