import requests
from bs4 import BeautifulSoup

template = '''
<div class="ip" id="d_clip_button" style="cursor: pointer;">
                                    <span>93.109.99.66</span>

                                    <i class="ip-icon-shape btn-copy"></i>
                                </div>
'''

HOST = 'https://2ip.ru'


response = requests.get(HOST)
response_text = response.text

soup = BeautifulSoup(response_text, features='lxml')
d_clip_button = soup.find(id='d_clip_button')
span = d_clip_button.find('span')

ip_address = span.text

print(f'Your IP address is {ip_address}')