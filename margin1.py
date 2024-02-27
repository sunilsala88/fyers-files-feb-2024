

import requests
with open('access.txt','r') as a:
    access_token=a.read()
client_id = '5YKT940X4B-100'
api_secret='KZGC320N71'

from fyers_apiv3 import fyersModel
import pandas as pd
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")


def get_span_margin(api_key, api_secret):
    url = "https://api.fyers.in/api/v2/span_margin"
    
    headers = {
        'Authorization': f'{api_key}:{access_token}',
        'Content-Type': 'application/json'
    }
    
    data = {
        "data": [

            {
                "symbol": "NSE:NIFTY24FEB22800CE",
                "qty": 50,
                "side": -1,
                "type": 2,
                "productType": "INTRADAY",
                "limitPrice": 0.0,
                "stopLoss": 0.0
            }
            ,
                        {
                "symbol": "NSE:NIFTY24FEB22800PE",
                "qty": 50,
                "side": 1,
                "type": 2,
                "productType": "INTRADAY",
                "limitPrice": 0.0,
                "stopLoss": 0.0
            }
        ]
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}, {response.text}"



result = get_span_margin(client_id, api_secret)
print(result)

