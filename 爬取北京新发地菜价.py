import requests
import csv
from concurrent.futures import ThreadPoolExecutor


f = open('北京新发地菜价.csv', mode='a+', encoding='gbk')
csv_writer = csv.writer(f)
csv_writer.writerow(["id", "菜名", "均价/元", "单位"])


def download_one_page(j):
    data = {'current': j}

    url = 'http://www.xinfadi.com.cn/getPriceData.html'
    resp = requests.get(url, data)

    lst = resp.json()['list']
    for p in lst:
        id = p['id']
        prodName = p['prodName']
        avgPrice = p['avgPrice']
        unitInfo = p['unitInfo']

        csv_writer.writerow([id, prodName, avgPrice, unitInfo])

    f.close()
    print('over!!!')


if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        for j in range(1, 5):
            # 把下载任务提交给线程池
            t.submit(download_one_page, j)

    print('over all!!!')