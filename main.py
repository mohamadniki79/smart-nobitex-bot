
import time
from utils import get_best_pair, should_buy, should_sell, get_balance, place_order
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("NOBITEX_API_KEY")
BASE_TOMAN = 140_000
TRADE_PERCENT = 0.03  # فقط 3 درصد از سرمایه ترید بشه

def run_bot():
    while True:
        print("در حال بررسی بازار...")
        best_pair = get_best_pair()
        if not best_pair:
            print("جفت‌ارز مناسب پیدا نشد.")
            time.sleep(300)
            continue

        balance = get_balance(API_KEY)
        trade_amount = balance * TRADE_PERCENT

        if should_buy(best_pair):
            place_order(API_KEY, "buy", best_pair, trade_amount)
            print(f"خرید انجام شد: {best_pair}")

        elif should_sell(best_pair):
            place_order(API_KEY, "sell", best_pair, trade_amount)
            print(f"فروش انجام شد: {best_pair}")

        time.sleep(300)  # هر 5 دقیقه یک بار

if __name__ == "__main__":
    run_bot()
