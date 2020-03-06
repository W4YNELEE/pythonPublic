import time
import fileOperation as file

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Ck101_verify_code_crawler():
    def __init__(self):
        self.dir_name='ck101'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        try:
            self.driver=webdriver.Chrome(executable_path='./chromedriver.exe',\
                                         options=self.options)
        except:
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
    
class Ntltd_verify_code_crawler(Ck101_verify_code_crawler):
    def __init__(self):
        self.ntltd_dir_name='碩博網驗證碼'
        
    def mk_dir(self):
        file.mkdir(self.ntltd_dir_name)
    
    def go_to_ntltd(self):
        super().__init__()
        x="https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/ccd=jIxiqy/registry"
        self.driver.get(x)
        print("Reach successful")
        time.sleep(1)
        try:
            self.driver.find_element_by_link_text("登入").send_keys(Keys.RETURN)
            print("已鍵入")
        except:
            pass

    def get_verify_code(self,qty):
        for i in range(0,qty):
            element=self.driver.find_element_by_xpath('//*[@class="dispcheckimg_div"]/img')
            element.screenshot("%s/final%d.png"%(self.ntltd_dir_name,(i+1)))
            print(element.size)
            print("第%d張圖片擷取完成"%(i+1))
            self.driver.refresh()
            time.sleep(1)
    
    def get_the_code2(self,x):
        self.mk_dir()
        self.go_to_ntltd()
        self.get_verify_code(x)

class Thsrc_crawler(Ck101_verify_code_crawler):
    def __init__(self):
        self.thsrc_dir_name='tshrc'
        file.mkdir(self.thsrc_dir_name)
        
    def go_to_thsrc(self):
        super().__init__()
        x = 'https://irs.thsrc.com.tw/IMINT/?locale=tw'
        self.driver.get(x)
        print("reach successful")
        time.sleep(1)
        
    def click_btn(self):
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath('//*[@id="btn-confirm"]').send_keys(Keys.RETURN)
            print("clicked I agree")
    
        except:
            print("nothing happened")
            pass

    def save_the_code(self, qty):
        for i in range(0, qty):
            element = self.driver.find_element_by_id("BookingS1Form_\
                                                     homeCaptcha_passCode")
            element.screenshot("%s/final%d.png"%(self.thsrc_dir_name,(i+1)))

            print(element.size)
            print("第%d張圖片擷取完成"%(i+1))
            self.driver.refresh()
            time.sleep(1)

    def get_the_code(self, x):
        self.go_to_thsrc()
        self.click_btn()
        #self.save_the_code(x)
        

mission = Thsrc_crawler()
mission.get_the_code(2)

#mission = Ntltd_verify_code_crawler()
#mission.get_the_code2(2)

#mission = Ck101_verify_code_crawler()
#mission.get_the_code(3) #數量
