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

