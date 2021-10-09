#-------------------------------------------------------------
# seleniumを用いてはてなブログのサイトにログインする
#-------------------------------------------------------------
# version:
# 1.0.0
#-------------------------------------------------------------
# required plugin:
# ・selenium
# ・chromedriver
#-------------------------------------------------------------

from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
import time

# ログイン情報の定義
mail_address = "ログイン用のメールアドレスを記入"
login_pw = "ログイン用のパスワードを記入"


# Chromeを操作
driver = webdriver.Chrome(executable_path="chromedriver.exeまでのパスを指定")
url = "https://www.hatena.ne.jp/"

# はてなブログのTOP画面を開く
driver.get(url)
# 3秒待機
time.sleep(3)
# ログインボタンをクリック
login_btn = driver.find_element_by_xpath('/html/body/div[2]/div/header/ul/li[1]/a')
login_btn.click()

time.sleep(3)

# ログインIDを入力
login_id = driver.find_element_by_name("name")
login_id.send_keys(mail_address)

time.sleep(3)

# パスワードを入力
login_pass = driver.find_element_by_name("password")
login_pass.send_keys(login_pw)

# ロボット判定対策のために10秒待機
time.sleep(10)

#「送信する」ボタンをクリック
submit_btn = driver.find_element_by_xpath('//*[@id="login-button"]')
submit_btn.click()
