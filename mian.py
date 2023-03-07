
import requests
from fake_headers import Headers
from bs4 import BeautifulSoup

parsed_list = []

HOST = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
#ARTICLES = f'{HOST}/ru/all/'

def get_headers():
    headers = Headers(browser='Microsoft Edge', os='win')
    return headers.generate()

response = requests.get(HOST, headers=get_headers())
hh_main = response.text

soup = BeautifulSoup(hh_main, features='lxml')

vacations = soup.find_all('div', class_='serp-item')
#salary = soup.find_all(attrs={'data-qa' : 'vacancy-serp__vacancy-compensation'})

#vacations = vacation_list.find('vacation')
#print(salary)


for vac in vacations:
    hh_vac = vac.find('a')
    vac_link = hh_vac['href']
    #print(vac_link)
    company_name = vac.find('div', {'class': 'bloko-text'}).find('a').text
    #print(company_name)
    city = vac.find(attrs={'data-qa' : 'vacancy-serp__vacancy-address'}).text
    #print(city)
    salary = vac.find(attrs={'data-qa' : 'vacancy-serp__vacancy-compensation'})
    
    if salary == None:
        salary_num = ''
    else:
        salary_num = salary.text
    #print(salary_num)

    item = {
        'link': vac_link,
        'salary': salary_num,
        'company': company_name,
        'city': city
    }
    parsed_list.append(item)

print(parsed_list)
    

 
    
    

