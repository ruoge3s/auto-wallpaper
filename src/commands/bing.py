# coding=utf-8
import os
import re
import time
import requests
from src.base.command import Command
from src.base import mapper
from src.base.config import Config
from src.base.application import Application


@mapper.describe('壁纸下载器')
class Bing(Command):

    home = None
    base_uri = None
    rank_uri = None
    headers = None

    def _init(self):
        self.home = Config().get('wallpaper:home')

        if self.home[0] is not '/':
            self.home = Application.BASEDIR + '/' + self.home

        if not os.path.isdir(self.home):
            os.mkdir(self.home, 0o766)

        self.rank_uri = Config().get('bing:rank-uri')
        self.base_uri = Config().get('bing:base-uri')
        # 构建请求头
        self.headers = Config().section('bing-http-headers')

    @mapper.describe('从bing下载壁纸')
    def download(self):
        # 创建下载目录
        self._init()

        # 获取总页数
        response = requests.get(self.rank_uri, headers=self.headers)

        if response.status_code != 200:
            print('下载壁纸失败,请求壁纸状态码为：' + str(response.status_code))
            print(response.text)
            return

        pres = re.compile("<span>\d{1,3}\s/\s(\d{1,3})</span>").findall(response.text)

        if len(pres) == 1:
            total_page = int(pres[0])
        else:
            total_page = 0

        for page in range(1, total_page + 1):
            print(F"Get pic from page {page}")
            urls = self._pic_urls(page)
            for i, j in enumerate(urls):
                try:
                    pic_name = j[:-1]  # + '_1920x1080.jpg'
                    file_name = self.home + '/' + pic_name

                    if os.path.isfile(file_name + '.jpg'):
                        continue
                    pic_url = self.base_uri + pic_name + '?force=download'
                    res = requests.get(pic_url, headers=self.headers)
                    res.encoding = 'utf8'
                    with open(file_name + '.jpg', 'wb') as f:  # 保存到本地
                        f.write(res.content)
                except Exception as e:
                    print(e)

            time.sleep(3)

    def _pic_urls(self, page):
        """
        提取所有壁纸的url正则
        :param page:
        :return:
        """
        url = self.rank_uri + '?p=' + str(page)
        res = requests.get(url, headers=self.headers)

        rs = re.compile('<a class="ctrl download" href="/photo/(.*?)/?force=download"')
        return rs.findall(res.text)
