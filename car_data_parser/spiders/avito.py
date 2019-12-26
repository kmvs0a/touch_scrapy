from scrapy.spiders import Spider
from scrapy import Request
from scrapy.exceptions import CloseSpider
from ..items import CarDataParserItem
import re
import unicodedata
import json


class AvitoSpider(Spider):
    avito_ads = []
    name = "avito"
    allowd_domains = ["avito.ru"]

    def start_requests(self):
        try:
            ads = self.avito_ads
            if ads is None:
                raise ValueError('ads is empty')

            for ad in ads:
                yield Request(url=ad['url'], meta={"_id": ad['_id']}, callback=self.parse)

        except Exception as e:
            raise CloseSpider(e.__class__ + ' : ' + e)

    def params_list_convert(self, params):
        car_data = {}
        regex = re.compile('<[^>]*>')

        for param in params:
            row = unicodedata.normalize("NFKD", regex.sub('', param))
            arr = row.split(":", 1)
            car_data[arr[0].strip()] = arr[1].strip() if len(arr) > 1 else ''

        return car_data

    def parse(self, response):
        item = CarDataParserItem()

        params = response.css('li.item-params-list-item').getall()

        item['_id'] = response.meta['_id']
        item['url'] = response.url
        item['car_data'] = self.params_list_convert(params)

        yield item
