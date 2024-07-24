import scrapy
import os

class TerceirizadosSpider(scrapy.Spider):
    name = "terceirizados"
    allowed_domains = ["www.gov.br"]
    start_urls = ["https://www.gov.br/cgu/pt-br/acesso-a-informacao/dados-abertos/arquivos/terceirizados"]

    def parse(self, response):
        #Seleciona os paths dos arquivos CSV e XLSX
        paths = response.xpath('//a[contains(@href, ".csv") or contains(@href, ".xlsx")]/@href').extract()

        # Para cada item da lista, cria uma requisição para baixar o arquivo da vez
        for path in paths:        
            yield scrapy.Request(url=response.urljoin(path), callback=self.download_file)

    def download_file(self, response):
        # Definindo diretório onde os arquivos serão salvos
        download_dir = '../dados'

        # Cria o diretório, caso não exista
        os.makedirs(download_dir, exist_ok=True)

        # Captura o nome do arquivo 
        file_name = os.path.join(download_dir, response.url.split("/")[-1])

        # Salva o arquivo no diretório acima especificado
        with open(file_name, 'wb') as f:
            f.write(response.body)
        self.log(f'Salvo arquivo {file_name}')
