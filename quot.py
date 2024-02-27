


from fyers_apiv3 import fyersModel
import pandas as pd
import datetime as dt
with open('access.txt','r') as a:
    access_token=a.read()
client_id = '5YKT940X4B-100'

# Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

#quotes data

data = {
    "symbols":"MCX:SILVER24MARFUT"
}

response = fyers.quotes(data=data)
print(response)
d=response['d'][0]['v']['lp']
print(d)

# import pandas as pd
# df=pd.DataFrame(d)
# print(df)

#depth data
data = {
    "symbol":"MCX:SILVER24MARFUT",
    "ohlcv_flag":"1"
}

response = fyers.depth(data=data)
print(response)