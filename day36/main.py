STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

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

import requests
import datetime
from newsapi import NewsApiClient
from twilio.rest import Client

articles_response_title = []
articles_response_discription = []

today_class = datetime.datetime.now()
month = today_class.month
year = today_class.year
day = today_class.day
yesterday = day - 1
day_before_yesterday = day - 2

if month < 9:
    month_string = "0" + f"{month}"
else:
    month_string = str(month)

if yesterday < 9:
    yesterday_string = "0" + f"{yesterday}"
else:
    yesterday_string = str(yesterday)

if day_before_yesterday < 9:
    day_before_yesterday_string = "0" + f"{day_before_yesterday}"
else:
    day_before_yesterday_string = str(day_before_yesterday)

parameter_stock = {
    #function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": ""
}

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url_alphavantage_stock = 'https://www.alphavantage.co/query'
result_stock = requests.get(url_alphavantage_stock, params= parameter_stock)
data = result_stock.json()

compact_yesterday = (data["Time Series (Daily)"][f"{year}-{month_string}-{yesterday_string}"]["4. close"])

compact_day_before_yesterday = (data["Time Series (Daily)"][f"{year}-{month_string}-{day_before_yesterday_string}"]["4. close"])

changes = float(compact_yesterday) - float(compact_day_before_yesterday)

if ((changes / float(compact_day_before_yesterday))*100 < (-5)) or ((changes / float(compact_day_before_yesterday))*100 > (5)):
    #GET https://newsapi.org/v2/everything?q=apple&from=2023-07-27&to=2023-07-27&sortBy=popularity&apiKey=d43a328f807348b7bc238bb889004eaa
    
    # Init
    newsapi = NewsApiClient(api_key='')

    # /v2/everything
    all_articles = newsapi.get_everything(q=COMPANY_NAME,
                                      language='en',
                                      page_size=3,
                                      page=1)
    
    for article in all_articles['articles']:
        articles_response_title.append(article['title'])
        articles_response_discription.append(article['description'])

    account_sid = ""
    auth_token = ""


    client = Client(account_sid, auth_token)

    for me in all_articles['articles']:
        if ((changes / float(compact_day_before_yesterday)) * 100) > 0:
            message = client.messages \
                .create(
                     body=f"TSLA: 🔺{(changes / float(compact_day_before_yesterday)) * 100}%\nHeadline: {me['title']}\nBrief: {me['description']}",
                     from_='',
                     to=''
                 )
        else:
            message = client.messages \
                .create(
                     body=f"TSLA: 🔻{(changes / float(compact_day_before_yesterday)) * 100}%\nHeadline: {me['title']}\nBrief: {me['description']}",
                     from_='',
                     to=''
                 )
    print(message.status)
