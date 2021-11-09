import requests
import re

obj = re.compile(r'var now="(?P<url>.*?)";', re.S)
url = 'https://www.91mjw.cc/video/29-0-0.html'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                            Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30"
}

resp = requests.get(url, headers=headers)
m3u8_url = obj.search(resp.text).group("url")

resp.close()

resp2 = requests.get(m3u8_url, headers=headers)

with open("m3u8文件.m3u8", mode='wb') as f:
    f.write(resp2.content)

resp2.close()
print("over")