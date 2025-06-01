import scrapy


class PhoneSpider(scrapy.Spider):
    name = "phone"
    allowed_domains = ["lista.mercadolivre.com.br"]
    base_url = "https://lista.mercadolivre.com.br/celulares-telefones/celulares-smartphones/celular_Desde_{offset}_NoIndex_True"
    start_urls = [base_url.format(offset=1)]
    page_count = 1
    max_page = 10

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

        # Paginação (Mercado livre não disponibiliza o href da próxima página em seu html)
        if self.page_count < self.max_page:
            offset = self.page_count * 50 + 1
            self.page_count += 1
            next_page = self.base_url.format(offset=offset)
            yield scrapy.Request(url=next_page, callback=self.parse)

