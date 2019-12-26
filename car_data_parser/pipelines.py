# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from car_data_parser.car_data_dictionary import CarDataDictionary


class CarDataParserPipeline(object):
    item_to_converter = {
        'avito': 'convert_avito'
    }

    def convert_by_dict(self, item, dict):
        result = {}
        car_data = item['car_data']
        for name, value in car_data.items():
            try:
                result[dict[name]] = value
            except Exception as e:
                raise Exception('disctionary convert error: ' +
                                e.__class__ + ' : ' + e)

        result.pop('none', None)
        return result

    def convert_avito(self, item):
        return self.convert_by_dict(item, CarDataDictionary.avito())

    def process_item(self, item, spider):
        try:
            pipe_name = self.item_to_converter[spider.name]
            converted = getattr(self, pipe_name)(item)
            return converted
        except KeyError:
            raise DropItem("Missing pipe_name in " + item['_id'])
