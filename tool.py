import requests, json
from bs4 import BeautifulSoup as bs

from models import Product

tag = "remarkable"

tag = input("Please enter a search tag: ")

url = "https://www.dba.dk/soeg/?soeg="
url += tag
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "dnt": "1",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"98\", \"Google Chrome\";v=\"98\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?0",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}


#url = "https://www.dba.dk/andet-maerke-remarkable/id-1088262475/"

req = requests.get(url, headers= headers)
soup = bs(req.text, 'html.parser')
prods = soup.find("table", {"class": "search-result searchResults srpListView"})

prods = prods.find("tbody")
prods = prods.find_all("tr", {"class": ["dbaListing listing", "dbaListing listing hasInsertionFee"]})

tesss = []

for prod in prods:
    mc = prod.find("td", {"class": "mainContent"})

    scrip = mc.find("script")

    help = json.loads(scrip.text, strict = False)
    name = help["name"]
    price = help["offers"]["price"] + help["offers"]["priceCurrency"]
    image = help["image"]
    url = help["url"]

    t=Product(name, price, url, image)
    tesss.append(t)
    #print(f"\nPrice: {price}   {name}")
    #print(url)
    #print(scrip.text)

with open("output.html", "w", encoding="utf8") as f:
    with open("data/top.txt", "r") as g:
        f.write(g.read())

    for product in tesss:
        f.write(product.toHtmlRow())

    with open("data/bottom.txt", "r") as g:
        f.write(g.read())