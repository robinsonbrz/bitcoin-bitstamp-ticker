import time
import datetime
import ssl
import json
import credentials

import websocket
import bitstamp.client


def get_trading_client():
    trading_client = bitstamp.client.Trading(username=credentials.USERNAME,
                                             key=credentials.KEY,
                                             secret=credentials.SECRET)
    return trading_client


def buy(quantity):
    trading_client = get_trading_client()
    trading_client.buy_market_order(amount=quantity, base="btc",
                                    quote="usd")


def sell(quantity):
    trading_client = get_trading_client()
    trading_client.sel_market_order(amount=quantity, base="btc",
                                    quote="usd")


def exhibit_json(json_message):
    # JSON message sample
    # {"data":{"id":219979332,"timestamp":"1643902080","amount":0.15,"amount_str":"0.15000000","price":36920.85,"price_str":"36920.85","type":0,"microtimestamp":"1643902080760000","buy_order_id":1454354866597889,"sell_order_id":1454354806321159},"channel":"live_trades_btcusd","event":"trade"}
    # print(mensagem, "mensagem")
    # print("mensagem['data'] ", len(mensagem["data"]))

    if len(json_message["data"]) == 0:
        print("______________________________________________________________________________________")
        print(
            f'{fixed_width_string("Trade pair")}{fixed_width_string("Price")}{fixed_width_string("Quantity")}{fixed_width_string("Timestamp")}{fixed_width_string("Transaction")}|')
        print("______________________________________________________________________________________")
    else:
        trade_pair = json_message["channel"].replace("live_trades_btcusd", "BTC/USD")
        price = json_message["data"]["price_str"]
        amount = json_message["data"]["amount_str"]
        transaction = json_message["data"]["id"]

        timestamp = int(json_message["data"]["timestamp"])

        date = time.strftime("%D %H:%M", time.localtime(timestamp))
        print(
            f'{fixed_width_string(trade_pair)}{fixed_width_string(price)}{fixed_width_string(amount)}{fixed_width_string(date)}{fixed_width_string(transaction)}|')


def fixed_width_string(rec_string):
    WIDTH = 15
    lenght = len(str(rec_string))
    ret_string = str(rec_string)

    if lenght < WIDTH:
        while len(ret_string) < WIDTH:
            ret_string += " "
    ret_string = "| " + ret_string
    return ret_string


def on_message(ws, message):
    json_message = json.loads(message)
    exhibit_json(json_message)


def on_mess(ws, message):
    print("Raw JSON message", message)
    json_menssage = json.loads(message)
    print("JSON message object", json_menssage)
    print("JSON data", json_menssage["channel"])


def on_error(ws, error):
    print("Error:", error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    json_subscribe = """
    {
        "event": "bts:subscribe",
        "data": {
            "channel": "live_trades_btcusd"
        }
    }
    """
    print("Connection opened!")
    ws.send(json_subscribe)



if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net",
                                on_open = on_open,
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close
                                )

    # ws.run_forever()
    # parameters if you want to disable ssl
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    print(ws)
