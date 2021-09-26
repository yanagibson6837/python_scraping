#2021/09/26
#課題対応　Webスクレイピングの学習
#Webサイトより意味のある任意のデータを抽出して、エクセルファイルに書き込む

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.nikkei.com/markets/worldidx/chart/nk225/'#参照先URLの記載
response = requests.get(url)

#参照先URLのHTMLをBeautifulSoupオブジェクト形式で取得
soup = BeautifulSoup(response.text, 'html.parser')

#h2タグの中から第二引数のクラス名を持つタグのテキストを検索
#get_text()によってタグのテキストを取得
title = soup.find('h2', class_='m-headline_text_large').get_text()
print(title)

#株価と日時、株価移動量の取得
value = soup.find('div', class_='m-article economic').get_text()
print(value)

#エクセルファイルへの書き込み
#第1引数；データ
#第2引数：要素名（行）
#第3引数；要素数（列）
df = pd.DataFrame(value,columns=[1],index=[1])
df.to_excel('C:\workspase\python\scraping\kadai_20210926\stock.xlsx')
