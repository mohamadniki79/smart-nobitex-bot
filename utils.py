
import requests

TOP_PAIRS = ["btc-irt", "eth-irt", "ada-irt", "doge-irt", "trx-irt", "shiba-irt"]

def get_best_pair():
    prices = {}
    for pair in TOP_PAIRS:
        try:
            r = requests.get(f"https://api.nobitex.ir/market/stats/{pair}")
            prices[pair] = float(r.json()["stats"]["latest"])
        except:
            continue
    if not prices:
        return None
    return max(prices, key=prices.get)

def should_buy(pair):
    return True

def should_sell(pair):
    return False

def get_balance(api_key):
    return 140_000  # شبیه‌سازی شده، در واقعیت از API نوبیتکس بگیر

def place_order(api_key, type, pair, amount):
    print(f"{type.upper()} {pair} => {amount} تومان")
    return True
