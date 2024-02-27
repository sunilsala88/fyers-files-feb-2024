from fyers_apiv3.FyersWebsocket import order_ws
from fyers_apiv3 import fyersModel
import pandas as pd
import datetime as dt
with open('access.txt','r') as a:
    access_token=a.read()
client_id = '5YKT940X4B-100'

new_access_token=f"{client_id}:{access_token}"
def onOrder(message):
    """
    Callback function to handle incoming messages from the FyersDataSocket WebSocket.

    Parameters:
        message (dict): The received message from the WebSocket.

    """
    print("Order Response:", message)

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
    data_type = "OnOrders"
    # data_type = "OnTrades"
    # data_type = "OnPositions"
    # data_type = "OnGeneral"
    # data_type = "OnOrders,OnTrades,OnPositions,OnGeneral"

    fyers.subscribe(data_type=data_type)

    # Keep the socket running to receive real-time data
    fyers.keep_running()


# Create a FyersDataSocket instance with the provided parameters
fyers = order_ws.FyersOrderSocket(
    access_token=new_access_token,  # Your access token for authenticating with the Fyers API.
    write_to_file=False,        # A boolean flag indicating whether to write data to a log file or not.
    log_path="",                # The path to the log file if write_to_file is set to True (empty string means current directory).
    on_connect=onopen,          # Callback function to be executed upon successful WebSocket connection.
    on_close=onclose,           # Callback function to be executed when the WebSocket connection is closed.
    on_error=onerror,           # Callback function to handle any WebSocket errors that may occur.
    on_orders=onOrder,          # Callback function to handle order-related events from the WebSocket.
)


# Establish a connection to the Fyers WebSocket
fyers.connect()

                
# {
#   "s":"ok",
#   "orders":{
#       "clientId":"XV20986",
#       "id":"23080400089344",
#       "exchOrdId":"1100000009596016",
#       "qty":1,
#       "filledQty":1,
#       "limitPrice":7.95,
#       "type":2,
#       "fyToken":"101000000014366",
#       "exchange":10,
#       "segment":10,
#       "symbol":"NSE:IDEA-EQ",
#       "instrument":0,
#       "offlineOrder":false,
#       "orderDateTime":"04-Aug-2023 10:12:58",
#       "orderValidity":"DAY",
#       "productType":"INTRADAY",
#       "side":-1,
#       "status":90,
#       "source":"W",
#       "ex_sym":"IDEA",
#       "description":"VODAFONE IDEA LIMITED",
#       "orderNumStatus":"23080400089344:2"
#   }
# }


# Order Response: {'s': 'ok', 'orders': {'clientId': 'XS45474', 'id': '24022200550989', 'qty': 1, 'remainingQuantity': 1, 'type': 2, 'fyToken': '1120240305254350', 'exchange': 11, 'segment': 20, 'symbol': 'MCX:SILVER24MARFUT', 'instrument': 30, 'offlineOrder': False, 'orderDateTime': '22-Feb-2024 21:32:41', 'orderValidity': 'DAY', 'productType': 'INTRADAY', 'side': 1, 'status': 4, 'source': 'W', 'ex_sym': 'SILVER', 'description': 'SILVER 24 Mar 05 FUT', 'orderTag': '2:Untagged', 'orderNumStatus': '24022200550989:4'}}
# Order Response: {'s': 'ok', 'orders': {'clientId': 'XS45474', 'id': '24022200550989', 'qty': 1, 'remainingQuantity': 0, 'type': 2, 'fyToken': '1120240305254350', 'exchange': 11, 'segment': 20, 'symbol': 'MCX:SILVER24MARFUT', 'instrument': 30, 'message': 'RED:Margin Shortfall:INR 3,31,581.40 Available:INR 495.42 for C-XS45474 [FYERS_RISK_CUG]', 'offlineOrder': False, 'orderDateTime': '22-Feb-2024 21:32:41', 'orderValidity': 'DAY', 'productType': 'INTRADAY', 'side': 1, 'status': 5, 'source': 'W', 'ex_sym': 'SILVER', 'description': 'SILVER 24 Mar 05 FUT', 'orderTag': '2:Untagged', 'orderNumStatus': '24022200550989:5'}}