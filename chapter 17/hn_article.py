import requests
import json

#یک ای پی آی را می خوانیم
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r= requests.get(url)
print(f" status code : {r.status_code}")
