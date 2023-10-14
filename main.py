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

    name_pattern = r'<div\s+class="x-product-card-description__product-name">(.*?)</div>'
    price_pattern = r'<div\s+class="x-product-card-description__x-product-card__card">(.*?)</div>'
    brand_pattern = r'<div\s+class="x-product-card-description__brand-name">([^<]+)</div>'

    names = re.findall(name_pattern, text)
    prices = re.findall(price_pattern, text)
    brands = re.findall(brand_pattern, text)


    for brand in brands:
        print(f'Бренд: {brand}')
    for price in prices:
        print(f'Бренд: {price}')

    for name, brand in zip(names, brands):
        print(f'Наименование:{name}, Бренд: {brand}')

