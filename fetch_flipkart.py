# fetch_flipkart.py

"""To fetch the data from flipkart"""

import requests
from  bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser(description="To search from flipkart.com")
parser.add_argument('name',help="Pass the item you wish to search for ")
args = parser.parse_args()

search_result = requests.get(f"https://www.flipkart.com/search?q={args.name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup = BeautifulSoup(search_result.text, 'lxml')
# print(soup.prettify())
# print(search_result.text)

detail = soup.find_all('div', class_ = '_2kHMtA')
for item in detail:
    name = item.find('div', class_ = '_4rR01T').text
    price = item.find('div', class_ = '_30jeq3 _1_WHN1').text
    print(f"Item name is {name} and price is {price}.")
