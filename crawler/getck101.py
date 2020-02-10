import time
import fileOperation as file

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class ck101_verify_code_crawler():
    def __init__(self):
        self.dir_name='ck101'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver=webdriver.Chrome(executable_path='./chromedriver',\
                                     options=self.options)
    
    def mk_dir(self):
        file.mkdir(self.dir_name)
    
    def go_to_ck101(self):
        x="https://ck101.com/member.php?\
        mod=register&referer=https%3A%2F%2Fck101.com%2Findex.php"
        self.driver.get(x)
        print("Reach successful")

    def get_verify_code(self,qty):
        for i in range(0,qty):
            #有時候會有pop up banner
            try:
                popup=self.driver.find_element_by_xpath("//*[@id='custominfo_register']/img")
                ActionChains(self.driver).move_to_element(popup).perform()
                popup.click()
            except:
                pass
            
            element=self.driver.find_element_by_xpath("//span[@id='seccode_S0']/img")
            element.screenshot("%s/final%d.png"%(self.dir_name,(i+1)))
            
            print(element.size)
            print("第%d張圖片擷取完成"%(i+1))
            self.driver.refresh()
            time.sleep(1)

    def get_the_code(self,x):
        self.mk_dir()
        self.go_to_ck101()
        self.get_verify_code(x)
    

mission = ck101_verify_code_crawler()
mission.get_the_code(3) #數量