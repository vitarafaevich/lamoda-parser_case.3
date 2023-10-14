"""
Котлярова Полина
Рафаевич Вита
"""

import requests
import re

if __name__ == '__main__':
    a = input()
    params = {'q' : a}
    response = requests.get('https://www.lamoda.ru/catalogsearch/result', params=params)

    text = response.text

    pattern = r'<div\s+class="x-product-card-description__product-name">(.*?)</div>'

    titles = re.findall(pattern, text)
    for title in titles:
        print(title)

    price_pattern = r'<div\s+class="x-product-card-description__product-name"[^"]*">([^<]+)</div>'
    brand_pattern = r'<div\s+class="x-product-card-description__brand-name">([^<]+)</div>'

    prices = re.findall(price_pattern, text)
    brands = re.findall(brand_pattern, text)


    for brand in brands:
        print(f'Бренд: {brand}')
    for price in prices:
        print(f'Бренд: {price}')

    for price, brand in zip(prices, brands):
        print(f'Цена: {price}, Бренд: {brand}')

