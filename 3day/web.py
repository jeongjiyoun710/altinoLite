# https://school.busanedu.net/buil-h/main.do

import os

from urllib import request
import requests
from bs4 import BeautifulSoup

url = "https://school.busanedu.net/buil-h/main.do"

response = requests.get(url)

# 내용 읽어오기
page_content = response.content

# html처럼 바꾸기
soup = BeautifulSoup(page_content, 'html.parser')

# .meal_list 찾아오기
quotes = soup.find_all('dd',class_='meal_list')

# 코드말고 텍스트만!
# class는 배열로 꺼내오기,,,
for q in quotes:
    print(q.getText())

os.system("pause")