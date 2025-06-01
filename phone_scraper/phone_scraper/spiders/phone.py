import scrapy


class PhoneSpider(scrapy.Spider):
    name = "phone"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/celular?sb=all_mercadolibre#D[A:celular]"]

    def parse(self, response):
        pass
