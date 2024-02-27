from fyers_apiv3.FyersWebsocket import data_ws
from fyers_apiv3 import fyersModel
import pandas as pd
import datetime as dt
with open('access.txt','r') as a:
    access_token=a.read()
client_id = '5YKT940X4B-100'


def onmessage(message):
    """
    Callback function to handle incoming messages from the FyersDataSocket WebSocket.

    Parameters:
        message (dict): The received message from the WebSocket.

    """
    print("Response:", message)
    # price=message['ltp']
    # vol=message['vol_traded_today']
    # print(price,vol)


def onerror(message):
    """
    Callback function to handle WebSocket errors.

    Parameters:
        message (dict): The error message received from the WebSocket.


    """
    print("Error:", message)


def onclose(message):
    """
    Callback function to handle WebSocket connection close events.
    """
    print("Connection closed:", message)


def onopen():
    """
    Callback function to subscribe to data type and symbols upon WebSocket connection.

    """
    # Specify the data type and symbols you want to subscribe to
    data_type = "DepthUpdate"

    # Subscribe to the specified symbols and data type
    symbols = ['MCX:SILVER24MARFUT']
    fyers.subscribe(symbols=symbols, data_type=data_type)

    # Keep the socket running to receive real-time data
    fyers.keep_running()




# Create a FyersDataSocket instance with the provided parameters
fyers = data_ws.FyersDataSocket(
    access_token=access_token,       # Access token in the format "appid:accesstoken"
    log_path="",                     # Path to save logs. Leave empty to auto-create logs in the current directory.
    litemode=False,                  # Lite mode disabled. Set to True if you want a lite response.
    write_to_file=False,              # Save response in a log file instead of printing it.
    reconnect=True,                  # Enable auto-reconnection to WebSocket on disconnection.
    on_connect=onopen,               # Callback function to subscribe to data upon connection.
    on_close=onclose,                # Callback function to handle WebSocket connection close events.
    on_error=onerror,                # Callback function to handle WebSocket errors.
    on_message=onmessage             # Callback function to handle incoming messages from the WebSocket.
)

# Establish a connection to the Fyers WebSocket
fyers.connect()



{'ltp': 70305.0, 
 'vol_traded_today': 12291, 
 'last_traded_time': 1708616943, 
 'exch_feed_time': 1708616952, 
 'bid_size': 1, 
 'ask_size': 1, 
 'bid_price': 70289.0, 
 'ask_price': 70304.0, 
 'last_traded_qty': 1, 
 'tot_buy_qty': 420, 
 'tot_sell_qty': 1320, 
 'avg_trade_price': 70737.48, 
 'low_price': 70155.0, 
 'high_price': 71200.0, 
 'lower_ckt': 0, 
 'upper_ckt': 0, 
 'open_price': 70724.0, 
 'prev_close_price': 70609.0, 
 'type': 'sf', 
 'symbol': 'MCX:SILVER24MARFUT', 
 'ch': -304.0, 
 'chp': -0.4305}

# {'bid_price1': 70293.0, 
#  'bid_price2': 70292.0, 
#  'bid_price3': 70290.0, 
#  'bid_price4': 70289.0, 'bid_price5': 70288.0, 'ask_price1': 70308.0, 'ask_price2': 70309.0, 'ask_price3': 70310.0, 'ask_price4': 70312.0, 'ask_price5': 70313.0, 'bid_size1': 1, 'bid_size2': 11, 'bid_size3': 2, 'bid_size4': 1, 'bid_size5': 3, 'ask_size1': 1, 'ask_size2': 2, 'ask_size3': 10, 'ask_size4': 3, 'ask_size5': 1, 'bid_order1': 1, 'bid_order2': 2, 'bid_order3': 1, 'bid_order4': 1, 'bid_order5': 2, 'ask_order1': 1, 'ask_order2': 2, 'ask_order3': 2, 'ask_order4': 2, 'ask_order5': 1, 'type': 'dp', 'symbol': 'MCX:SILVER24MARFUT'}
