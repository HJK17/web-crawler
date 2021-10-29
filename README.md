- 服务器渲染：在服务器那边直接把数据和html整合在一起，统一返回给浏览器
    - 在页面源代码中能看到数据

- 客户端渲染：第一次请求只要一个html骨架，第二次请求拿到数据，进行数据展示。
    - 在页面源代码中看不到数据

# 第一个爬虫程序

- 爬取百度页面
- 安装 requests 
- pip install requests

```
import requests

query = input("请输入你想查询的内容：")
url = f'https://www.baidu.com/s?wd={query}'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                            Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30"
}

resp = requests.get(url, headers=headers)  # 处理一个小小的反爬

print(resp)
print(resp.text)  # 拿到页面源代码
```

# 正则表达式
在线正则表达式测试 [开源中国](https://tool.oschina.net/regex)
## 常用的正则表达式
1. \d 匹配一个数字

2. [1-9] 连续1-9 。 [1-36-9] 1-3连续，6-9连续。 [123456] 匹配123456 。[1-5a-d] 连续1-5，a-d

3. [^abc] 匹配除了abc以外的字符(取反)

4. \w 匹配单个字符   0-9, a-z, A-Z, 数字、字母、下划线

5. \s 匹配空白，即空格， tab键(\t)

6. .  匹配任意一个字符（除了\n）

7. {m,n}匹配连续m-n位, \d{1,3}（123， 1，34）

8. ？问号前面的字符可有可无, (-?,%?)

9. *匹配任意多个

10. .*匹配任意多个(贪婪匹配)

11. .*？尽量少匹配(惰性匹配)

12. +匹配前一个字符出现1次或者无限次，至少有1次

## Python re模块的使用
```
import re

# finditer: 匹配字符串中所有的内容[返回的是迭代器]，从迭代器中拿到的内容 需要.group()
it = re.finditer(r"\d+", "我的电话是：10086， 你的电话是：10010")
for i in it:
    print(i.group())

# 输出结果为：10086 10010


# search, 找到一个结果就返回， 返回的结果是match对象。那数据需要.group()
s = re.search(r"\d+", "我的电话是：10086， 你的电话是：10010")
print(s.group())

# 输出结果为：10086


# match 是从头开始匹配
s = re.match(r"\d+", "10086， 你的电话是：10010")
print(s.group())

# 输出结果为：10086


# 预加载正则表达式
obj = re.compile(r"\d+")

ret = obj.finditer("我的电话是：10086， 你的电话是：10010")
for it in ret:
    print(it.group())

ret = obj.findall("我的电话是：10086， 你的电话是：10010")
print(ret)


s = """<div class='p'><span id='1'>Python</span></div>" \
    "<div class='j'><span id='2'>java</span></div>" \
    "<div class='c'><span id='3'>C</span></div>" \
    "<div class='G'><span id='4'>Golang</span></div>" \
    "<div class='r'><span id='5'></span>rust</div>
    """

# (?P<名字>正则表达式) 可以单独从正则匹配内容中进一步提取内容
obj = re.compile(r"<div class='(?P<one>.*?)'><span id='(?P<two>\d+)'>(?P<three>.*?)</span></div>", re.S)  # re.S 让.匹配换行符

result = obj.finditer(s)
for it in result:
    print(it.group("one"))
    print(it.group("two"))
    print(it.group("three"))
```

## 爬取豆瓣top250数据
```
import requests
import re
import csv

for i in range(0, 275, 25):
    url = f'https://movie.douban.com/top250?start={i}&filter='
    print(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'}
    resp = requests.get(url, headers=headers)
    page_content = resp.text

    # 解析数据
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
                     r'.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">'
                     r'(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>', re.S)
    # 开始匹配
    result = obj.finditer(page_content)
    f = open('data.csv', mode='a+')
    csvwriter = csv.writer(f)
    for it in result:
        # print(it.group('name'))
        # print(it.group('year').strip())
        # print(it.group('score'))
        # print(it.group('num'))
        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        csvwriter.writerow(dic.values())
    f.close()
print('over')

```