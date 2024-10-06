import requests
respone = requests.get('https://books.toscrape.com/')
if respone.ok:
    with open('books.txt', 'w',encoding="utf-8") as f:
        f.write(respone.text)
else:
    print(respone)