import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

URL='https://ko.aliexpress.com'

def crawl():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get(URL)

    ul=driver.find_element_by_class_name("_1nker")
    print(ul)

crawl()

#soup = BeautifulSoup(r.html.find('._1nker.WCeVm').text, 'html.parser')
#print(soup)