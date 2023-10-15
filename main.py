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
    price_pattern = r'span>\s+class="x-product-card-description__price-old[^"₽]*">([^<]+)</span>'
    brand_pattern = r'<div\s+class="x-product-card-description__brand-name">([^<]+)</div>'
    article_pattern = r'"short_sku":"([A-Za-z0-9]+)"'

    articles = re.findall(article_pattern, text)
    names = re.findall(name_pattern, text)
    prices = re.findall(price_pattern, text)
    brands = re.findall(brand_pattern, text)

    for article, name, brand in zip(articles, names, brands):
        print(f'Number: {article}, Name:{name}, Brand: {brand}')

