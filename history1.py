


from fyers_apiv3 import fyersModel
import pandas as pd
import datetime as dt
with open('access.txt','r') as a:
    access_token=a.read()
client_id = '5YKT940X4B-100'

# Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")


now_epoch=int(dt.datetime.now().timestamp())
prev_epoch=int((dt.datetime.now()-dt.timedelta(days=5)).timestamp())
print(now_epoch)
print(prev_epoch)


now_date=dt.datetime.now()
prev_date=dt.datetime.now()-dt.timedelta(days=5)
print(now_date)
print(prev_date)

data = {
    "symbol":"MCX:SILVER24MARFUT",
    "resolution":"1",
    "date_format":"1",
    "range_from":prev_date.date(),
    "range_to":now_date.date(),
    "cont_flag":"1"
}

response = fyers.history(data=data)
print(response)
data=response['candles']
df=pd.DataFrame(data)
print(df)

df.columns=['date','open','high','low','close','volume']
df['date']=pd.to_datetime(df['date'], unit='s')

df.date=(df.date.dt.tz_localize('UTC').dt.tz_convert('Asia/Kolkata'))
print(df)
df['date'] = df['date'].dt.tz_localize(None)
df=df.set_index('date')

print(df)
df.to_csv('data.csv')
print(dt.datetime.now())


def fetchOHLC(ticker,interval,duration):
    """extracts historical data and outputs in the form of dataframe"""
    instrument = ticker
    data = {"symbol":instrument,"resolution":interval,"date_format":"1","range_from":dt.date.today()-dt.timedelta(duration),"range_to":dt.date.today(),"cont_flag":"1"}
    sdata=fyers.history(data)
    sdata=pd.DataFrame(sdata['candles'])
    sdata.columns=['date','open','high','low','close','volume']
    sdata['date']=pd.to_datetime(sdata['date'], unit='s')
    sdata.date=(sdata.date.dt.tz_localize('UTC').dt.tz_convert('Asia/Kolkata'))
    sdata['date'] = sdata['date'].dt.tz_localize(None)
    sdata=sdata.set_index('date')
    return sdata

ticker='NSE:NIFTYBANK-INDEX'
data=fetchOHLC(ticker,'1',60)
print(data)



def gethistory(symbol1,type,duration):
    symbol="NSE:"+symbol1+"-"+type
    start=dt.date.today()-dt.timedelta(duration)
    end=dt.date.today()-dt.timedelta()
    sdata=pd.DataFrame()
    while start <= end:
        end2=start+dt.timedelta(60)
        data = {"symbol":symbol,"resolution":"1","date_format":"1","range_from":start,"range_to":end2,"cont_flag":"1"}
        s=fyers.history(data)
        s=pd.DataFrame(s['candles'])
        sdata=pd.concat([sdata,s],ignore_index=True)
        start=end2+dt.timedelta(1)
    sdata.columns=['date','open','high','low','close','volume']
    sdata["date"]=pd.to_datetime(sdata['date'], unit='s')
    sdata.date=(sdata.date.dt.tz_localize('UTC').dt.tz_convert('Asia/Kolkata'))
    sdata['date'] = sdata['date'].dt.tz_localize(None)
    sdata=sdata.set_index('date')
    return sdata

data=gethistory('NIFTYBANK','INDEX',3000)
print(data)
data.to_csv('niftybank.csv')