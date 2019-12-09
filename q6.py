#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from datetime import datetime
bitcoin_api_url = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"
ifttt_webhook_url = 'https://maker.ifttt.com/trigger/bitcoin_price/with/key/keyyyyyyy'


# In[2]:


def get_latest_bitcoin_price():
    response = requests.get(bitcoin_api_url)
    response_json = response.json()
    return float(response_json[0]['price_usd'])


def post_ifttt_webhook_notify(event, value):
    data = {'value1': value}
    ifttt_event_url = ifttt_webhook_url.format(event)
    requests.post(ifttt_event_url, json=data)

def main():

        price = get_latest_bitcoin_price()
        post_ifttt_webhook_notify('bitcoin_price', price)
    
if __name__ == '__main__':
    try:
        main()
    except IOError:
        print("Check Network connectivity")

