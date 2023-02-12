
import requests
from fake_headers import Headers
from bs4 import BeautifulSoup


HOST = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
#ARTICLES = f'{HOST}/ru/all/'

def get_headers():
    headers = Headers(browser='Microsoft Edge', os='win')
    return headers.generate()

response = requests.get(HOST, headers=get_headers())
hh_main = response.text

soup = BeautifulSoup(hh_main, features='lxml')

vacations = soup.find_all('div', class_='serp-item')
#vacations = vacation_list.find('vacation')
print(vacations)
#print(soup)

company = soup.find('div', class_='serp-item__title')
print(company)
    
    

