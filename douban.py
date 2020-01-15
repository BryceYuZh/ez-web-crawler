from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
 
class DBDY:
    def __init__(self):                               #进行初始化操作
        self.driver = webdriver.Chrome("/Users/zhehaoyu/Desktop/web crawler/chromedriver-2")
        self.wait = WebDriverWait(self.driver,10)
    def open_page(self):                              #利用selenium驱动，打开豆瓣电影的网页
        driver = self.driver
        driver.get('https://www.douban.com/doulist/46373997/')
    def get_response(self,page_num):         #该函数用来获取信息
        driver = self.driver
        wait = self.wait
        try:                           #判断我们需要的内容是否加载出来
            wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'#content > div > div.article'))
            )
        except TimeoutException:
            raise TimeoutException
        page = driver.page_source        #获取网页源代码
        soup = BeautifulSoup(page,'html.parser')
        items = soup.find_all('div',class_ = 'doulist-item')           #找到每一部电影的相关信息
        print('开始打印第{}页'.format(page_num))
        for item in items:                                          #将每部电影的信息打印出来
            product = {
                'movie':item.find('div',class_ = 'title').find('a').text.strip(),
                'rating_nums':item.find('span',class_ = 'rating_nums').text,
                'people':item.find('div',class_ = 'abstract').text.strip()
            }
            print(product)
    def next_page(self):  #翻页函数
        driver = self.driver
        wait = self.wait
        #检查下一页的元素是否加载出来
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#content > div > div.article > div.paginator > span.next > a'))
        )
        #找到这个下一页的元素
        next_p = driver.find_elements_by_class_name('next')[0]
        #进行点击
        next_p.click()
        
        
if __name__ == '__main__':
    db = DBDY()
    db.open_page()
    for i in range(1,4):      #这里各位想要抓取多少页的信息看各位
        db.get_response(i)
        db.next_page()
    #抓取完所有的信息后关闭网页
    db.driver.quit()
