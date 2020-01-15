from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from  selenium.webdriver.common.keys import Keys
import time
import sys
import threading
import requests
from aip import AipOcr
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CourseSelect:
    def __int__(self):
        pass

    filepath = "./cap/img.png"
    
    
    def get_captcha(self):
        APP_ID = '18275558'
        API_KEY = 'MSLnSpkm3P7HaAmdt9kRtxex'
        SECRET_KEY = 'xBhfzGBxKTn0PorejvggGkrOZNhME18L'

        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

        
        options = {
                'detect_direction' : 'true',
                'language_type' : 'ENG',
        }
        # 调用通用文字识别接口  
        with open(self.filepath, 'rb') as fp:
            content = fp.read()
            result = client.basicAccurate(content, options)
        rst = result['words_result']
        rst = rst[0]['words']
        print(rst)
        rst = rst.replace(' ', '')
        return rst
    
    
    def login(self, id, pwd):
        self.url = 'http://coursesel.umji.sjtu.edu.cn/welcome.action'
        self.browser=webdriver.Chrome("/Users/zhehaoyu/Desktop/web crawler/chromedriver-2")
        browser=self.browser
        time.sleep(2)
        page =browser.get(self.url)
        # input user info
        username=browser.find_element_by_id('user')
        password=browser.find_element_by_id('pass')
        username.send_keys(id)
        password.send_keys(pwd)
        
        # get captcha
        captcha=browser.find_element_by_id('captcha-img')                                        
        captcha.screenshot(self.filepath)
        
        cap = self.get_captcha()
        captcha_input=browser.find_element_by_id('captcha')
        captcha_input.send_keys(cap)
        
        loginBtn = browser.find_element_by_id('submit-button')
        loginBtn.click()
        time.sleep(3)

    def getin(self):
        browser = self.browser
        round=browser.find_element_by_class_name('electTurnName')
        round.click()
        time.sleep(3)
        mark=browser.find_element_by_class_name('elect-turn-detail-item-bottom-tip')
        mark.click()
        go=browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]')
        go.click()
        
    def select_by_xpath(self,xpath=""):
        browser=self.browser
        xk=browser.find_element_by_xpath(xpath)
        xk.click()
        browser.switch_to_alert().accept()
        time.sleep(1)


if __name__ == '__main__':
    username='ads1cft'
    pwd='yzhde1216'
    xp=input('input xpath: ')
    
    service = CourseSelect()
    service.login(username, pwd)
    time.sleep(3)
    service.get_in()
    
    time.sleep(10)
    
    service.select_by_xpath(xp)
    service.browser.close()
    