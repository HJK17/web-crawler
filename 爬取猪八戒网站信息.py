import requests
from lxml import etree
import csv

file = open("八戒.csv", "w", encoding='utf-8')
csv_writer = csv.writer(file)
csv_writer.writerow(["公司名", "地址", "商品", "价格"])

name = input("请输入要查找的信息：")
url = f'https://chongqing.zbj.com/search/f/?kw={name}'

resp = requests.get(url)
html = etree.HTML(resp.text)

divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")
for div in divs:
    price = div.xpath("./div/div/a[2]/div[2]/div[1]/span[1]/text()")[0].strip("￥")
    title = 'saas'.join(div.xpath("./div/div/a[2]/div[2]/div[2]/p/text()"))
    com_name = div.xpath("./div/div/a[1]/div[1]/p/text()")  # 会提取多余公司名信息
    com_name1 = (str(com_name).split("n")[-1]).split("'")[0]  # 处理得到准确公司名
    location = div.xpath("./div/div/a[1]/div[1]/div/span/text()")[0]

    csv_writer.writerow([com_name1, location, title, price])

file.close()
print("完成！！")

