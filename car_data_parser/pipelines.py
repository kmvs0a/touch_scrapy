# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from car_data_parser.parser.car_data_dictionary import CarDataDictionary

class CarDataParserPipeline(object):
    item_to_converter = {
        'avito': 'convert_avito'
    }

    def convert_avito(self, item):
        car_data_dictionary = CarDataDictionary.avito()
        return item

    def process_item(self, item, spider):
        try:
            pipe_name = self.item_to_converter[spider.name]
            return getattr(self, pipe_name)(item) 
        except KeyError:
            raise DropItem("Missing pipe_name in " + item['_id'])

    
