import threading
import time
import MySQLdb
import requests
from itertools import combinations
import re


# TELEGRAM_TOKEN = ''
# TELEGRAM_CHANNEL = ''

# def send_message(text):
#     url = 'https://api.telegram.org/bot{}/sendMessage'.format(TELEGRAM_TOKEN)
#     data = {
#         'chat_id': TELEGRAM_CHANNEL,
#         'text': text
#     }
#     response = requests.post(url, data=data)

#send_message('text')

setting = {
        "refreshTime":15 
    }


def connectDB():
    return MySQLdb.connect(host="localhost", user="root", passwd="", db="price_binance")

def transform_symbol(original_symbol):
    return re.sub(r'[^A-Za-z0-9]', '', original_symbol)

def update_symbol_uni(cursor, symbol, birza):
    cursor.execute(f"SELECT symbol_uni FROM price WHERE symbol = '{symbol}' AND birza = {birza}")
    result = cursor.fetchone()

    if not result or not result[0]:  
        new_symbol = transform_symbol(symbol)
        cursor.execute(f"UPDATE price SET symbol_uni = '{new_symbol}' WHERE symbol = '{symbol}' AND birza = {birza}")



def load_Binance():
    time_start = time.time() 

    conn = connectDB()
    cursor = conn.cursor()

    price_list = requests.get("https://api.binance.com/api/v3/ticker/24hr").json() 

    if 'code' in price_list:
        print(f"Error code {price_list['code']} msg = {price_list['msg']}")
        time.sleep(10)
        return False

    count_symbol = 0
    for symbol in price_list:
        try:
            count_symbol += 1
            if float(symbol['lastPrice']) > 0: 
                cursor.execute(f"INSERT INTO `price` (`birza`, `symbol`, `price`, `bidPrice`, `bidQty`, `askPrice`, `askQty`, `symbol_uni`) VALUES (1, '{symbol['symbol']}', '{symbol['lastPrice']}', '{symbol['bidPrice']}', '{symbol['bidQty']}', '{symbol['askPrice']}', '{symbol['askQty']}', '{symbol['symbol']}') ON DUPLICATE KEY UPDATE price = '{symbol['lastPrice']}' , bidPrice = '{symbol['bidPrice']}', bidQty = '{symbol['bidQty']}', askPrice = '{symbol['askPrice']}', askQty = '{symbol['askQty']}' , last_update = UNIX_TIMESTAMP();")    
        except Exception as inst:
            print(inst) 
    print(f"Binance symbol : {count_symbol}")
    conn.commit() 
    conn.close()

    print(f"Upload Binance for {round(time.time()-time_start,3)} seconds")


def while_binance():
    global setting

    while True: 
        load_Binance()
        time.sleep(setting["refreshTime"])


def load_Gate():
    
    time_start = time.time()

    
    conn = connectDB() 
    cursor = conn.cursor()

    
    data = requests.get("https://api.gateio.ws/api/v4/spot/tickers/").json()

    count_symbol = 0
    for symbol in data:
        try:
            count_symbol += 1
            cursor.execute(f"INSERT INTO `price` (`birza`, `symbol`, `price`, `bidPrice`, `askPrice`) VALUES (2, '{symbol['currency_pair']}', '{symbol['last']}', '{symbol['highest_bid']}', '{symbol['lowest_ask']}') ON DUPLICATE KEY UPDATE price = '{symbol['last']}' , bidPrice = '{symbol['highest_bid']}', askPrice = '{symbol['lowest_ask']}', last_update = UNIX_TIMESTAMP();") 
            update_symbol_uni(cursor, symbol['currency_pair'], 2) 
        except Exception as inst:
            print(inst) 
    print(f"Gate symbol : {count_symbol}")
    conn.commit()
    conn.close()
    print(f"Upload Gate for {round(time.time()-time_start,3)} seconds")


def while_Gate():
    global setting

    while True: 
        load_Gate()
        time.sleep(setting["refreshTime"])



def load_Mexc():
    time_start = time.time() 

    conn = connectDB()
    cursor = conn.cursor()


    price_list = requests.get("https://api.mexc.com/api/v3/ticker/24hr").json() 

    count_symbol = 0 
    for symbol in price_list:
        count_symbol += 1 
        cursor.execute(f"INSERT INTO `price` (`birza`, `symbol`, `price`, `bidPrice`, `bidQty`, `askPrice`, `askQty`, `symbol_uni`) VALUES (3, '{symbol['symbol']}', '{symbol['lastPrice']}', '{symbol['bidPrice']}', '{symbol['bidQty']}', '{symbol['askPrice']}', '{symbol['askQty']}', '{symbol['symbol']}') ON DUPLICATE KEY UPDATE price = '{symbol['lastPrice']}' , bidPrice = '{symbol['bidPrice']}', bidQty = '{symbol['bidQty']}', askPrice = '{symbol['askPrice']}', askQty = '{symbol['askQty']}', symbol_uni = '{symbol['symbol']}' , last_update = UNIX_TIMESTAMP();") 
    print(f"Mexc symbol : {count_symbol}")   
    conn.commit() 
    conn.close()
    print(f"Upload Mexc for {round(time.time()-time_start,3)} seconds")


def while_Mexc():
    global setting

    while True: 
        load_Mexc()
        time.sleep(setting["refreshTime"])


def load_KuCoin():
    time_start = time.time() 

    
    conn = connectDB()
    cursor = conn.cursor()

    price_list = requests.get("https://api.kucoin.com/api/v1/market/allTickers").json() 

    count_symbol = 0
    for symbol in price_list['data']['ticker']:
        count_symbol += 1 
        cursor.execute(f"INSERT INTO `price` (`birza`, `symbol`, `price`, `bidPrice`, `askPrice`) VALUES ( 4, '{symbol['symbol']}', '{symbol['last']}', '{symbol['buy']}', '{symbol['sell']}') ON DUPLICATE KEY UPDATE price = '{symbol['last']}' , bidPrice = '{symbol['buy']}', askPrice = '{symbol['sell']}', last_update = UNIX_TIMESTAMP();") 
        update_symbol_uni(cursor, symbol['symbol'], 4)  
    print(f"KuCoin symbol : {count_symbol}")
    conn.commit() 
    conn.close()
    print(f"Upload KuCoin for {round(time.time()-time_start,3)} seconds")



def while_KuCoin():
    global setting
    while True: 
        load_KuCoin()
        time.sleep(setting["refreshTime"])




def load_Bybit():
    time_start = time.time() 

    conn = connectDB()
    cursor = conn.cursor()


    price_list = requests.get("https://api.bybit.com/v5/market/tickers?category=spot").json() 

    count_symbol = 0 
    for symbol in price_list['result']['list']:
        count_symbol += 1 
        cursor.execute(f"INSERT INTO `price` (`birza`, `symbol`, `price`, `bidPrice`, `bidQty`, `askPrice`, `askQty`, `symbol_uni`) VALUES (5, '{symbol['symbol']}', '{symbol['lastPrice']}', '{symbol['bid1Price']}', '{symbol['bid1Size']}', '{symbol['ask1Price']}', '{symbol['ask1Size']}', '{symbol['symbol']}') ON DUPLICATE KEY UPDATE price = '{symbol['lastPrice']}' , bidPrice = '{symbol['bid1Price']}', bidQty = '{symbol['bid1Size']}', askPrice = '{symbol['ask1Price']}', askQty = '{symbol['ask1Size']}', symbol_uni = '{symbol['symbol']}' , last_update = UNIX_TIMESTAMP();") 
    print(f"Bybit symbol : {count_symbol}")    
    conn.commit() 
    conn.close()
    print(f"Upload ByBit for {round(time.time()-time_start,3)} seconds")



def while_ByBit():
    global setting
    while True: 
        load_Bybit()
        time.sleep(setting["refreshTime"])

        

def load_Okx():
    time_start = time.time() 


    conn = connectDB()
    cursor = conn.cursor()


    price_list = requests.get("https://www.okx.com/api/v5/market/tickers?instType=SPOT").json() 

    count_symbol = 0 
    for symbol in price_list['data']:
        count_symbol += 1 
        cursor.execute(f"INSERT INTO `price` (`birza`, `symbol`, `price`, `bidPrice`, `bidQty`, `askPrice`, `askQty`) VALUES (6, '{symbol['instId']}', '{symbol['last']}', '{symbol['bidPx']}', '{symbol['bidSz']}', '{symbol['askPx']}', '{symbol['askSz']}') ON DUPLICATE KEY UPDATE price = '{symbol['last']}' , bidPrice = '{symbol['bidPx']}', bidQty = '{symbol['bidSz']}', askPrice = '{symbol['askPx']}', askQty = '{symbol['askSz']}' , last_update = UNIX_TIMESTAMP();") 
        update_symbol_uni(cursor, symbol['instId'], 6)  
    print(f"Okx symbol : {count_symbol}")     
    conn.commit() 
    conn.close()
    print(f"Upload Okx for {round(time.time()-time_start,3)} seconds")


def while_Okx():
    global setting
    while True: 
        load_Okx()
        time.sleep(setting["refreshTime"])




def load_Bitstamp():
    
    time_start = time.time()

    conn = connectDB() 
    cursor = conn.cursor()

    data = requests.get("https://www.bitstamp.net/api/v2/ticker/").json()

    count_symbol = 0
    for symbol in data:
        try:
            count_symbol += 1
            cursor.execute(f"INSERT INTO `price` (`birza`, `symbol`, `price`, `bidPrice`, `askPrice`) VALUES (7, '{symbol['pair']}', '{symbol['last']}', '{symbol['bid']}', '{symbol['ask']}') ON DUPLICATE KEY UPDATE price = '{symbol['last']}' , bidPrice = '{symbol['bid']}', askPrice = '{symbol['ask']}', last_update = UNIX_TIMESTAMP();") 
            update_symbol_uni(cursor, symbol['pair'], 7)     
        except Exception as inst:
            print(inst) 
    print(f"Bitstamp symbol : {count_symbol}") 
    conn.commit() 
    conn.close()
    print(f"Upload Bitstamp for {round(time.time()-time_start,3)} seconds")


def while_Bitstamp():
    global setting

    while True: 
        load_Bitstamp()
        time.sleep(setting["refreshTime"])



def compare_prices():
    conn = connectDB()
    cursor = conn.cursor()

    
    cursor.execute("SELECT DISTINCT symbol_uni FROM price")
    symbols = cursor.fetchall()

    price_diffs = []

    for symbol in symbols:
        cursor.execute(f"SELECT birza, askPrice, bidPrice FROM price WHERE symbol_uni = '{symbol[0]}'")
        prices = cursor.fetchall()

        #зразок: bl_3 = ['GMTUSDT', 'LOOPUSDT']
        bl_1 = []
        bl_2 = ['ORTUSDT', 'MANUSDT', 'LUFFYUSDT', 'ASSUSDT', 'LOOPUSDT', 'BNB3LUSDT', 'WITUSDT']
        bl_3 = ['ETHFUSDT', 'PRQUSDT', 'IMPTUSDT', 'IRONUSDT', 'FMCUSDT', 'MDXUSDT', 'QUACKUSDT', 'GMTUSDT', 'GMEEUSDT', 'ICEUSDT', 'CTYUSDT', 'LUFFYUSDT', 'ASSUSDT', 'LOOPUSDT', 'WITUSDT', 'VMPXUSDT', 'ANCUSDT', 'QIUSDT', 'TRCLUSDT', 'DEUSUSDT']
        bl_4 = ['NEAR3LUSDT', 'GMEEUSDT', 'BNB3LUSDT', 'PEPE2USDT']
        bl_5 = ['ENJUSDT', 'EVERUSDT']
        bl_6 = []
        bl_7 = []

        for birza_1, birza_2 in combinations(prices, 2):
            ask_price_1 = birza_1[1]
            bid_price_2 = birza_2[2]
            

            
            if ask_price_1 != 0 and float(ask_price_1) != 0 and float(bid_price_2) > float(ask_price_1):
                price_diff = abs(float(bid_price_2) - float(ask_price_1))
                percentage_diff = (price_diff / float(ask_price_1)) * 100
                if percentage_diff <= 10 and percentage_diff > 3:
                    if (symbol[0] not in bl_1 and (birza_1[0] != '1' or birza_2[0] != '1')
                        and symbol[0] not in bl_2 and (birza_1[0] != '2' or birza_2[0] != '2')
                        and symbol[0] not in bl_3 and (birza_1[0] != '3' or birza_2[0] != '3')
                        and symbol[0] not in bl_4 and (birza_1[0] != '4' or birza_2[0] != '4')
                        and symbol[0] not in bl_5 and (birza_1[0] != '5' or birza_2[0] != '5')
                        and symbol[0] not in bl_6 and (birza_1[0] != '6' or birza_2[0] != '6')
                        and symbol[0] not in bl_7 and (birza_1[0] != '7' or birza_2[0] != '7')
                        ):
                        price_diffs.append((percentage_diff, symbol, birza_1[0], birza_2[0], ask_price_1, bid_price_2))

            
            ask_price_2 = birza_2[1]
            bid_price_1 = birza_1[2]



            
            if ask_price_2 != 0 and float(ask_price_2) != 0 and float(bid_price_1) > float(ask_price_2):
                price_diff = abs(float(bid_price_1) - float(ask_price_2))
                percentage_diff = (price_diff / float(ask_price_2)) * 100
                if percentage_diff <= 10 and percentage_diff > 3:
                    if (symbol[0] not in bl_1 and (birza_1[0] != '1' or birza_2[0] != '1')
                        and symbol[0] not in bl_2 and (birza_1[0] != '2' or birza_2[0] != '2')
                        and symbol[0] not in bl_3 and (birza_1[0] != '3' or birza_2[0] != '3')
                        and symbol[0] not in bl_4 and (birza_1[0] != '4' or birza_2[0] != '4')
                        and symbol[0] not in bl_5 and (birza_1[0] != '5' or birza_2[0] != '5')
                        and symbol[0] not in bl_6 and (birza_1[0] != '6' or birza_2[0] != '6')
                        and symbol[0] not in bl_7 and (birza_1[0] != '7' or birza_2[0] != '7')
                        ):
                        price_diffs.append((percentage_diff, symbol, birza_2[0], birza_1[0], ask_price_2, bid_price_1))

    sorted_price_diffs = sorted(price_diffs, reverse=True)

    def get_exchange_name(code):
        exchange_names = {'1': 'Binance', '2': 'Gate', '3': 'Mexc', '4': 'Kucoin', '5': 'Bybit', '6': 'Okx', '7': 'Bitstamp'}
        return exchange_names.get(code, code)

    print("Top 10 price differences:")
    for i in range(min(100, len(sorted_price_diffs))):
        price_diff = sorted_price_diffs[i]
        
        birza_1_name = get_exchange_name(str(price_diff[2]))
        birza_2_name = get_exchange_name(str(price_diff[3]))

        print(f"Difference: {price_diff[0]}%, Symbol: {price_diff[1]}, Exchanges: {birza_1_name} - {birza_2_name}")
        print(f"Exchange 1 Price: birza: {birza_1_name}  askPrice: {price_diff[4]}")
        print(f"Exchange 2 Price: birza: {birza_2_name}  bidPrice: {price_diff[5]}")
        # send_message(f"Condition met: Difference: {price_diff[0]}%, Symbol: {price_diff[1]}, Exchanges: {birza_1_name} - {birza_2_name}")


    conn.close()





def while_compare_prices():
    global setting
    while True: 
        compare_prices()
        time.sleep(setting["refreshTime"])




def start():

    binance = threading.Thread(target = while_binance)
    binance.start()

    Gate = threading.Thread(target = while_Gate)
    Gate.start()

    Mexc = threading.Thread(target = while_Mexc)
    Mexc.start()

    KuCoin = threading.Thread(target = while_KuCoin)
    KuCoin.start()

    ByBit = threading.Thread(target = while_ByBit)
    ByBit.start()

    Okx = threading.Thread(target = while_Okx)
    Okx.start()
    
    Bitstamp = threading.Thread(target = while_Bitstamp)
    Bitstamp.start()

    Compare = threading.Thread(target = while_compare_prices)
    Compare.start()

if __name__ == '__main__':
    start()