import scrapy


class TerceirizadosSpider(scrapy.Spider):
    name = "terceirizados"
    allowed_domains = ["www.gov.br"]
    start_urls = ["https://www.gov.br/cgu/pt-br/acesso-a-informacao/dados-abertos/arquivos/terceirizados"]

    def parse(self, response):
        pass
