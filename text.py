import requests
a = input()
params = {'q' : a}
response = requests.get('https://www.lamoda.ru/catalogsearch/result', params=params)
text = response.text
print(text)