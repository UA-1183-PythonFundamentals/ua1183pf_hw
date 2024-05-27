import requests
from sqlalchemy import create_engine, Column, String, Integer, Float, distinct
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pygame
import sys

# Створюю базу даних
engine = create_engine('sqlite:///exchange_symbols.db', echo=True)  
Base = declarative_base()

class ExchangeSymbol(Base):
    __tablename__ = 'exchange_symbols'
    id = Column(Integer, primary_key=True, autoincrement=True)
    exchange = Column(String)
    symbol = Column(String)
    price = Column(Float)
    bidPrice = Column(Float)
    askPrice = Column(Float)
    symbol_uni = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def save_binance_symbols():
    """отримую і записую в SQL Alchemy дані валютних пар з біржі Binance"""
    binance_url = "https://api.binance.com/api/v3/ticker/24hr"
    binance_data = requests.get(binance_url).json()

    for item in binance_data:
        symbol = item['symbol']
        price = float(item['lastPrice']) if item['lastPrice'] else None
        bidPrice = float(item['bidPrice']) if item['bidPrice'] else None
        askPrice = float(item['askPrice']) if item['askPrice'] else None
        symbol_uni = item['symbol']
        exchange_symbol = ExchangeSymbol(exchange='Binance', symbol=symbol, price=price, bidPrice=bidPrice, askPrice=askPrice, symbol_uni=symbol_uni)
        session.add(exchange_symbol)

    session.commit()
    print("Binance symbols saved.")

def save_gate_symbols():
    """отримую і записую в SQL Alchemy дані валютних пар з біржі Gate"""
    gate_url = "https://api.gateio.ws/api/v4/spot/tickers/"
    gate_data = requests.get(gate_url).json()

    for item in gate_data:
        symbol = item['currency_pair']
        price = float(item['last']) if item['last'] else None
        bidPrice = float(item['highest_bid']) if item['highest_bid'] else None
        askPrice = float(item['lowest_ask']) if item['lowest_ask'] else None
        symbol_uni = item['currency_pair'].replace('_', '')
        exchange_symbol = ExchangeSymbol(exchange='Gate', symbol=symbol, price=price, bidPrice=bidPrice, askPrice=askPrice, symbol_uni=symbol_uni)
        session.add(exchange_symbol)

    session.commit()
    print("Gate symbols saved.")

def save_mexc_symbols():
    """отримую і записую в SQL Alchemy дані валютних пар з біржі Mexc"""
    gate_url = "https://api.mexc.com/api/v3/ticker/24hr"
    gate_data = requests.get(gate_url).json()

    for item in gate_data:
        symbol = item['symbol']
        price = float(item['lastPrice']) if item['lastPrice'] else None
        bidPrice = float(item['bidPrice']) if item['bidPrice'] else None
        askPrice = float(item['askPrice']) if item['askPrice'] else None
        symbol_uni = item['symbol']
        exchange_symbol = ExchangeSymbol(exchange='Mexc', symbol=symbol, price=price, bidPrice=bidPrice, askPrice=askPrice, symbol_uni=symbol_uni)
        session.add(exchange_symbol)

    session.commit()
    print("Mexc symbols saved.")

def print_symbols():
    symbols = session.query(ExchangeSymbol).all()
    for symbol in symbols:
        print(f"Exchange: {symbol.exchange}, Symbol: {symbol.symbol}, Price: {symbol.price}, BidPrice: {symbol.bidPrice}, AskPrice: {symbol.askPrice}, Symbol_uni: {symbol.symbol_uni}")

def compare_prices():
    symbols = session.query(distinct(ExchangeSymbol.symbol_uni)).all()
    price_diffs = []

    for symbol in symbols:
        symbol_uni = symbol[0]
        prices = session.query(ExchangeSymbol.exchange, ExchangeSymbol.askPrice, ExchangeSymbol.bidPrice).filter(ExchangeSymbol.symbol_uni == symbol_uni).all()

        #мій чорний список
        bl_1 = []
        bl_2 = ['ORTUSDT', 'MANUSDT', 'LUFFYUSDT', 'ASSUSDT', 'LOOPUSDT', 'BNB3LUSDT', 'WITUSDT']
        bl_3 = ['ETHFUSDT', 'PRQUSDT', 'IMPTUSDT', 'IRONUSDT', 'FMCUSDT', 'MDXUSDT', 'QUACKUSDT', 'GMTUSDT', 'GMEEUSDT', 'ICEUSDT', 'CTYUSDT', 'LUFFYUSDT', 'ASSUSDT', 'LOOPUSDT', 'WITUSDT', 'VMPXUSDT', 'ANCUSDT', 'QIUSDT', 'TRCLUSDT', 'DEUSUSDT']

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                birza_1, ask_price_1, bid_price_1 = prices[i]
                birza_2, ask_price_2, bid_price_2 = prices[j]

                if ask_price_1 and float(ask_price_1) != 0 and bid_price_2 and float(bid_price_2) > float(ask_price_1):
                    price_diff = abs(float(bid_price_2) - float(ask_price_1))
                    percentage_diff = (price_diff / float(ask_price_1)) * 100
                    if percentage_diff <= 10 and percentage_diff > 3:
                        if (symbol_uni not in bl_1 and (birza_1 != 'Binance' or birza_2 != 'Binance')
                            and symbol_uni not in bl_2 and (birza_1 != 'Gate' or birza_2 != 'Gate')
                            and symbol_uni not in bl_3 and (birza_1 != 'Mexc' or birza_2 != 'Mexc')):
                            price_diffs.append((percentage_diff, symbol_uni, birza_1, birza_2, ask_price_1, bid_price_2))

                if ask_price_2 and float(ask_price_2) != 0 and bid_price_1 and float(bid_price_1) > float(ask_price_2):
                    price_diff = abs(float(bid_price_1) - float(ask_price_2))
                    percentage_diff = (price_diff / float(ask_price_2)) * 100
                    if percentage_diff <= 10 and percentage_diff > 3:
                        if (symbol_uni not in bl_1 and (birza_1 != 'Binance' or birza_2 != 'Binance')
                            and symbol_uni not in bl_2 and (birza_1 != 'Gate' or birza_2 != 'Gate')
                            and symbol_uni not in bl_3 and (birza_1 != 'Mexc' or birza_2 != 'Mexc')):
                            price_diffs.append((percentage_diff, symbol_uni, birza_2, birza_1, ask_price_2, bid_price_1))

    sorted_price_diffs = sorted(price_diffs, reverse=True)
    return sorted_price_diffs

def display_results(results):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Price Differences")

    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 28)

    white = (255, 255, 255)
    black = (0, 0, 0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(white)

        y_offset = 20
        header = font.render("Top 5 price differences:", True, black)
        screen.blit(header, (20, y_offset))
        y_offset += 40

        for i in range(min(5, len(results))):
            price_diff = results[i]
            line1 = f"Difference: {price_diff[0]:.2f}%, Symbol: {price_diff[1]}, Exchanges: {price_diff[2]} - {price_diff[3]}"
            line2 = f"Exchange 1 Price: askPrice: {price_diff[4]}"
            line3 = f"Exchange 2 Price: bidPrice: {price_diff[5]}"

            line1_surf = small_font.render(line1, True, black)
            line2_surf = small_font.render(line2, True, black)
            line3_surf = small_font.render(line3, True, black)

            screen.blit(line1_surf, (20, y_offset))
            y_offset += 30
            screen.blit(line2_surf, (20, y_offset))
            y_offset += 30
            screen.blit(line3_surf, (20, y_offset))
            y_offset += 40

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    save_binance_symbols()
    save_gate_symbols()
    save_mexc_symbols()
    results = compare_prices()
    display_results(results)
