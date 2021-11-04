import requests
from lxml import etree
import csv


f = open('豆瓣影评.csv', mode='a+', encoding='utf-8')
csv_writer = csv.writer(f)
csv_writer.writerow(["用户名", "评论", "评价", "时间"])

for i in range(0, 1):  # 自定义范围

    url = f'https://movie.douban.com/subject/3001114/comments?start={i}&?limit=20&status=P&sort=new_score'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                                Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30"
    }

    resp = requests.get(url, headers=headers)
    html = etree.HTML(resp.text)

    divs = html.xpath("/html/body/div[3]/div[1]/div/div[1]/div[4]/div")
    for div in divs:
        person = div.xpath("./div[2]/h3/span[2]/a/text()")
        person = person[0] if len(person) != 0 else person  # 会抓取到空的数据，取第一个下标会报错
        comment = div.xpath("./div[2]/p/span/text()")
        comment = comment[0] if len(comment) != 0 else comment
        value = div.xpath("./div[2]/h3/span[2]/span[2]/@title")
        value = value[0] if len(value) != 0 else value
        time = div.xpath("./div[2]/h3/span[2]/span[3]/text()")
        time = time[0] if len(time) != 0 else time

        if len(person) != 0:
            csv_writer.writerow([person, comment, value, time])


f.close()
print("over!!")

