"""
Котлярова Полина
Рафаевич Вита
"""

import requests
import re

if __name__ == '__main__':
    goods = input()
    params = {'q': goods}
    response = requests.get('https://www.lamoda.ru/catalogsearch/result', params=params)
    base_url = 'https://www.lamoda.ru'

    text = response.text
    page_pattern = r'"pagination":{"page":\d+,"pages":(\d+),'
    pages = re.findall(page_pattern, text)
    pages = str(pages).strip("[']")
    for page in range(1, int(pages)+1):
        params = {'q': goods, 'page': page}
        response = requests.get('https://www.lamoda.ru/catalogsearch/result', params=params)
        text = response.text

        name_pattern = r'<div\s+class="x-product-card-description__product-name">(.*?)</div>'
        brand_pattern = r'<div\s+class="x-product-card-description__brand-name">([^<]+)</div>'
        article_pattern = r'"short_sku":"([A-Za-z0-9]+)"'

        articles = re.findall(article_pattern, text)
        countries = []
        prices = []
        discounts = []
        products = []
        for article in articles:
            product_url = f'{base_url}/p/{article}'
            response = requests.get(product_url)
            product = response.text

            country_pattern = r'"production_country","title":"Страна производства","value":"(.*?)"'
            country = re.findall(country_pattern, product)
            country = str(country).strip("[']")
            countries.append(country)

            price_pattern = r'"price":"(.*?)"'
            pricess = re.findall(price_pattern, product)
            prices.append(f'{pricess[0]} ₽')

            pricess = str(pricess).replace(' ', '')
            pricess = pricess.split(',')

            if len(pricess) == 2:
                pricess[0] = pricess[0].strip("[']")
                pricess[1] = pricess[1].strip("[']")
                discount = int(((int(pricess[1]) - int(pricess[0])) / int(pricess[1])) * 100)
                discounts.append(f'{discount}%')
            else:
                discount = '0%'
                discounts.append(discount)

        names = re.findall(name_pattern, text)
        brands = re.findall(brand_pattern, text)
with open('output.txt', 'w', encoding='utf-8') as f_out:
        for article, name, brand, price, discount, country in zip(articles, names, brands, prices, discounts, countries):
            print(f'Number: {article}, Name: {name}, Brand: {brand}, Price: {price}, Discount: {discount}, 'f'Production Country: {country}', file = f_out)

