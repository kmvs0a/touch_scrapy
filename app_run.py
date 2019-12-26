from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.signalmanager import dispatcher

from car_data_parser.spiders.avito import AvitoSpider


def run_avito_spiders(avito_ads):
    if avito_ads is None:
        avito_ads = [
            {
                '_id': '[autoru]17883722',
                'url': 'https://www.avito.ru/kaspiysk/avtomobili/opel_astra_2012_1609480606',
            }
        ]

    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    process = CrawlerProcess(get_project_settings())
    process.crawl(AvitoSpider, avito_ads=avito_ads)
    process.start()

    return results


if __name__ == '__main__':
    print(run_avito_spiders(None))
