# pip install requests

import requests
import time

def get_exchange_rates():
    # Замените 'YOUR_API_KEY' на Ваш ключ API
    url = "https://api.exchangerate-api.com/v4/latest/USD"  # пример использования API
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['rates']
    else:
        print("Ошибка при получении данных:", response.status_code)
        return None

def display_exchange_rates(rates):
    print("Курсы валют:")
    for currency, rate in rates.items():
        print(f"{currency}: {rate}")
    print("\n" + "-"*30 + "\n")

if __name__ == "__main__":
    while True:
        rates = get_exchange_rates()
        if rates:
            display_exchange_rates(rates)
        time.sleep(10)  # обновление каждые 10 секунд
