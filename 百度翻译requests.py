import requests

url = 'https://fanyi.baidu.com/sug'

s = input('输入单词:')
dat = {'kw': s}

# 发送post请求
resp = requests.post(url, data=dat)
print(resp.json())
