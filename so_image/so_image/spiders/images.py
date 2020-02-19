# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json


class ImagesSpider(scrapy.Spider):


    # allowed_domains = ['image.so.com']
    # start_urls = ['http://image.so.com/']
    #BASE_URL = 'http://image.so.com/zj?ch=art&sn=%s&listtype=new&temp=1'
    BASE_URL = 'https://image.so.com/zjl?ch=wallpaper&sn=%s&listtype=new&temp=1'
    start_index = 0

    MAX_DOWNLOAD_NUM = 1000

    name = "images"
    start_urls = [BASE_URL % 0]


    def parse(self, response):

        infos = json.loads(response.body.decode('utf-8'))
        yield {'image_urls': [info['qhimg_url'] for info in infos['list']]}

        self.start_index += infos['count']
        if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAD_NUM:
            yield Request(self.BASE_URL % self.start_index)
