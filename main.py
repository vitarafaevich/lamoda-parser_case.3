"""
Котлярова Полина
Рафаевич Вита
"""

import requests
import re

if __name__ == '__main__':
    goods = input()
    params = {'q' : goods}
    response = requests.get('https://www.lamoda.ru/catalogsearch/result', params=params)
    base_url = 'https://www.lamoda.ru'

    text = response.text

    name_pattern = r'<div\s+class="x-product-card-description__product-name">(.*?)</div>'
    price_pattern = r'span>\s+class="x-product-card-description__price-old[^"₽]*">([^<]+)</span>'
    brand_pattern = r'<div\s+class="x-product-card-description__brand-name">([^<]+)</div>'
    article_pattern = r'"short_sku":"([A-Za-z0-9]+)"'

    articles = re.findall(article_pattern, text)
    countries = []
    for article in articles:
        product_url = f'{base_url}/p/{article}'
        response = requests.get(product_url)
        product = response.text
        country_pattern = r'"production_country","title":"Страна производства","value":"(.*?)"'
        country = re.findall(country_pattern, product)
        countries.append(country)


    names = re.findall(name_pattern, text)
    prices = re.findall(price_pattern, text)
    brands = re.findall(brand_pattern, text)

    for article, name, brand, country in zip(articles, names, brands, countries):
        print(f'Number: {article}, Name:{name}, Brand: {brand}, Production country: {country}')

