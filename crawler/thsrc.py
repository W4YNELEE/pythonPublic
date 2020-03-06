# -*- coding: utf-8 -*-
import os

#建立目標資料夾
dest="tshrc1"
if os.path.exists(dest)==False:
    os.mkdir(dest)

from selenium import webdriver
import time

#用Chrome開啟網址（背景啟動模式）
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver=webdriver.Chrome(executable_path='./chromedriver',\
                                         options=options)
#driver=webdriver.Chrome()
x="https://irs.thsrc.com.tw/IMINT/?locale=tw"
driver.get(x)

#開始截圖動作
for i in range(0,3):
#找取程式碼的元素(路徑)並且取得定位
    element=driver.find_element_by_id("BookingS1Form_homeCaptcha_passCode")
    element.screenshot("tshrc1/final%d.png"%(i+1))
#檢查元素是否抓取正確
#print(element.get_attribute("src"))
    #print(element.location)
    print(element.size)
    print("第%d張圖片擷取完成"%(i+1))
    driver.refresh()
    time.sleep(1)
