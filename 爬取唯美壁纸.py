import time
import requests
from bs4 import BeautifulSoup
import re


url = 'https://umei.cc/weimeitupian/'
resp = requests.get(url)
resp.encoding = 'utf-8'

# 把源代码交给bs
main_page = BeautifulSoup(resp.text, 'html.parser')
alist = main_page.find('div', class_="TypeList").find_all('a')
headerurl = 'https://umei.cc/'
for a in alist:
    href = headerurl + a.get("href")
    # 拿到子页面的源代码
    child_page_resp = requests.get(href)
    child_page_resp.encoding = 'utf-8'
    child_page_text = child_page_resp.text
    # 从子页面中拿到图片的下载地址
    child_page = BeautifulSoup(child_page_text, "html.parser")
    img = child_page.find('div', class_="ImageBody").find("img")
    src = img.get("src")
    # 下载图片
    img_resp = requests.get(src)

    # 图片名称
    imgname = child_page.find('p', class_="ArticleDesc")
    name = re.finditer(r"一组(?P<name1>.*?)图集", imgname.text)
    for i in name:
        img_name = i.group("name1") + '.jpg'

        with open(f'../img/{img_name}', mode='wb') as f:
            f.write(img_resp.content)
            print('over', img_name)
            time.sleep(1)

print("overall!!!")