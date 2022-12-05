import time
import requests
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By

chop = webdriver.ChromeOptions()
#chop.add_extension("extension_3_0_3_0.crx")
driver = webdriver.Chrome(chrome_options=chop)

#textfoat = input("Введите максимальное значение float: ")
#textfloat = str(textfoat)
#speed = input("Введите время задержки: ")
#new_speed = int(speed)
time.sleep(1)
driver.get("https://steamcommunity.com/login/home/?goto=market%2Flistings%2F730")
input("Войдите в аккаунт Steam и нажмите Enter ")

while(True):
    time.sleep(1)
    weblink = "https://steamcommunity.com/market/listings/730/MAC-10%20%7C%20Candy%20Apple%20(Factory%20New)"
    driver.get(weblink)
    speed = "19"
    new_speed = int(speed)
    webfloat = "0.0138"
    inspect = driver.find_element("class name", "market_actionmenu_button")
    driver.execute_script("arguments[0].click();", inspect)
    popup = driver.find_element("css selector", "#market_action_popup_itemactions > a")
    href = popup.get_attribute('href')

    response = requests.get('https://api.csgofloat.com/?url=' + href)

    json_response = response.json()
    json_response_name = str(json_response["iteminfo"]["full_item_name"])
    json_response_float = str(json_response["iteminfo"]["floatvalue"])
    json_response_pattern = str(json_response["iteminfo"]["paintseed"])

    json_response_stickers = str(json_response["iteminfo"]['stickers'])

    # price1 = driver.find_element('xpath', '//*[@id="listing_4062838791705166135"]/div[1]/a[2]').text        # первая цена

    now = datetime.now()
    current_time = now.strftime("[%H:%M:%S]")

    TOKEN_INFO = '5804532416:AAEkf3D7oJ8ZyLm2Mhz0Wy0PeK9y_Rb0TVM'
    id_chat = '1172102069'
    say = '\nКупил: '
    name = '\nНазвание: ' + json_response_name
    tgfloat = '\nFloat: ' + json_response_float
    tgpattern = '\nPattern: ' + json_response_pattern
    stickers = '\nStickers: ' + json_response_stickers

    if not webfloat >= json_response_float:
        print(current_time)
        print("#2 Поиск... " + webfloat)
    else:
        print(current_time)
        print("#2 Найдено! ")
        buy_buttons = driver.find_element("class name", "item_market_action_button")
        driver.execute_script("arguments[0].click();", buy_buttons)
        time.sleep(0.1)
        check_box = driver.find_element("id", "market_buynow_dialog_accept_ssa")
        driver.execute_script("arguments[0].click();", check_box)
        time.sleep(0.1)
        buy_button = driver.find_element("id", "market_buynow_dialog_purchase")
        driver.execute_script("arguments[0].click();", buy_button)
        time.sleep(0.1)
        close_button = driver.find_element("id", "market_buynow_dialog_close")
        driver.execute_script("arguments[0].click();", close_button)
        print("#2 Float: " + json_response_float)
        requests.get('https://api.telegram.org/bot{}/sendMessage'.format(TOKEN_INFO),  # Отправляет сообщение
                     params=dict(chat_id=id_chat, text=current_time + say + name + tgfloat + tgpattern + stickers))
        time.sleep(60)

    time.sleep(new_speed)
    driver.refresh()
