import requests

url = (input('请输入梨视频的链接：'))
contId = url.split('_')[1]

videoStatusUrl = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.27100311550203515'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.121 Safari/537.36 HBPC/11.0.3.301',
    'Referer': url  # 防盗链， 溯源， 本次请求的上一级是谁
}

resp = requests.get(videoStatusUrl, headers=headers)
dic = resp.json()

srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']
srcUrl = srcUrl.replace(systemTime, f'cont-{contId}')

name = url.rsplit('/', 1)[1]
with open(name + '.mp4', mode='wb') as f:
    f.write(requests.get(srcUrl).content)
print('-----over！！！-------')



