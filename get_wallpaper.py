import requests
import re
import time
import os

headers = {
        'Host': "h1.ioliu.cn",
        'Connection': "keep-alive",
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        'Accept': "image/webp,image/apng,image/*,*/*;q=0.8",
        'Accept-Encoding': "gzip, deflate",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cookie': "__jsluid=e095d5332b8a908a9947826225e5b9dd"
    }


def total_page():
    url = 'https://bing.ioliu.cn/ranking?p=1'
    response = requests.get(url)
    pres = re.compile("<span>\d{1,3}\s/\s(\d{1,3})</span>").findall(response.text)

    if len(pres) == 1:
        return int(pres[0])
    else:
        print("Obtain total page numbers error.")
        exit()


def pic_urls(page):
    url = 'https://bing.ioliu.cn/ranking?p=' + str(page)
    res = requests.get(url)
    rs = re.compile('<a class="ctrl download" href="/photo/(.*?)/?force=download"')  # 提取壁纸名称正则表达式
    return rs.findall(res.text)


def run(dir_name):
    base_uri = 'http://h1.ioliu.cn/bing/'  # 图片服务器

    for page in range(1, total_page() + 1):
        print(F"Get pic from page {page}")
        urls = pic_urls(page)
        for i, j in enumerate(urls):
            try:
                pic_name = j[:-1] + '_1920x1080.jpg'
                file_name = dir_name + '/' + pic_name

                if os.path.isfile(file_name):
                    continue

                res = requests.get(base_uri + pic_name, headers=headers)
                res.encoding = 'utf8'
                # print(res.status_code)
                with open(file_name, 'wb') as f:  # 保存到本地
                    f.write(res.content)
            except Exception as e:
                print(e)

        time.sleep(3)
