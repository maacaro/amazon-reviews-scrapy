from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def get_reviews_from():
    process = CrawlerProcess(get_project_settings())

    process.crawl('amazon-reviews-spider', product_id = 'B07DHBM5RC')
    process.start() 