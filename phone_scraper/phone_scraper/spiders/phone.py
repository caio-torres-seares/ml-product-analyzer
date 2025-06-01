import scrapy


class PhoneSpider(scrapy.Spider):
    name = "phone"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/celular?sb=all_mercadolibre#D[A:celular]"]

    def parse(self, response):

        products = response.css('div.ui-search-result__wrapper')

        for product in products:

            brand = product.css('span.poly-component__brand::text').get()
            name = product.css('a.poly-component__title::text').get()
            old_price = product.css('div.poly-component__price s span.andes-money-amount__fraction::text').get()
            new_price = product.css('div.poly-price__current span.andes-money-amount__fraction::text').get()
            link = product.css('a.poly-component__title::attr(href)').get()
            yield {
                'brand' : brand,
                'name': name,
                'old_price': old_price,
                'new_price': new_price,
                'link': link
            }

