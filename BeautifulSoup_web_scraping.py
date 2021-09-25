#Webスクレイピング
#参照URL
#https://www.pasonatech.co.jp/workstyle/column/detail.html?p=2638

import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.pasonatech.co.jp/') #正常に動作
#response = requests.get('https://www.toyota-ti.ac.jp/') #なぜか文字化けする

soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find('title').get_text()
print(title)
