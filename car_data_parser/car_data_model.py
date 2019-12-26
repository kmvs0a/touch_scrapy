from scrapy.item import Item, Field

class CarDataItem(Item):
    url         = Field()
    gear_type   = Field()
    body_type   = Field()

