import matplotlib.pyplot as plt
import requests
from datetime import datetime


def get_crypto_price(crypto_id, days):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days,
        "interval": "daily"
    }
    response = requests.get(url, params=params)
    data = response.json()


    prices = data["prices"]
    date = [datetime.fromtimestamp(price[0] / 1000) for price in prices]
    values = [price[1] for price in prices]
    return date, values


def plot_crypto_chart(crypto_ids, days):
    color = "lightgreen"

    for crypto_id in crypto_ids:
        dates, prices = get_crypto_price(crypto_id, days)

        plt.figure(figsize=(12, 6))

        plt.plot(dates, prices, label=f"Курс {crypto_id.capitalize()}", color=color, marker="o")

        plt.title(f"Курс {crypto_id.capitalize()} за последние {days} дней", fontsize=14)
        plt.xlabel("Дата", fontsize=12)
        plt.ylabel("Цена в USD", fontsize=12)
        plt.grid(True)
        plt.legend()
        plt.xticks(rotation=45)

        plt.tight_layout()

    plt.show()


crypto_list = ["bitcoin", "ethereum"]  # Введи сюда название криптовалют
plot_crypto_chart(crypto_list, 30)
