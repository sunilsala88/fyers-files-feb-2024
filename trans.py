

from fyers_apiv3 import fyersModel
import pandas as pd
import datetime as dt
with open('access.txt','r') as a:
    access_token=a.read()
client_id = '5YKT940X4B-100'

fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

response = fyers.orderbook()['orderBook']
print(response)
df=pd.DataFrame(response)
print(df)
