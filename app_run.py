from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from car_data_parser.spiders.avito import AvitoSpider

avito_ads = [
    {
    '_id': '[autoru]17883722',
    'url': 'https://www.avito.ru/kaspiysk/avtomobili/opel_astra_2012_1609480606',
    }
    ]

process = CrawlerProcess(get_project_settings())
process.crawl(AvitoSpider, avito_ads=avito_ads)
process.start()
