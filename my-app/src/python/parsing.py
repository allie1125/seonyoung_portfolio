import requests
import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8') #이부분이 없으면 콘솔에 출력하는것은 잘 되지만 노드로 데이터 전달이 안된다. 
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8') #이부분이 없으면 콘솔에 출력하는것은 잘 되지만 노드로 데이터 전달이 안된다.

url = 'https://ko.aliexpress.com/'

response = requests.get(url)

# 응답 코드가 200일 때, html을 받아와서 soup 객체로 변환
if response.status_code == 200: 
    html = response.content
    soup = BeautifulSoup(html, 'lxml')
    print(soup)
    #print([i.text for i in soup.select('div._1nker.WCeVm')])
    #titles = soup.select('div._1nker.WCeVm > a > div._3GR-w > div._1tu1Z > h1')
   # print([i.text for i in soup.select('._1nker.WCeVm')])


    #ul = soup.select_one('#root > div:nth-child(6) > div > div._1nker.WCeVm')#s_content > div.section > ul
    #print(ul)
    #titles = ul.select('a > div._3GR-w > div._1tu1Z > h1')
    #for title in titles:
    #    print(title.get_text())
else : 
    print(response.status_code)