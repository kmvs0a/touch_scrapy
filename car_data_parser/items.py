# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class CarDataParserItem(Item):
    _id      = Field()
    url      = Field()    
    car_data = Field()
    pass
