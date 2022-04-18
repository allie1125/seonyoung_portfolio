import requests
import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8') #이부분이 없으면 콘솔에 출력하는것은 잘 되지만 노드로 데이터 전달이 안된다. 
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8') #이부분이 없으면 콘솔에 출력하는것은 잘 되지만 노드로 데이터 전달이 안된다.

# Session 생성 
s = requests.Session() 
# 헤더 설정 
headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36' } 
req = s.get('http://feeds.bbci.co.uk/news/rss.xml',headers=headers) 
## HTML 소스 가져오기 
html = req.text

print(html)