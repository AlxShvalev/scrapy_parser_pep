import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['http://peps.python.org/']

    def parse(self, response):
        table = response.css('section#numerical-index')
        pep_list = table.css('a[class="pep reference internal"]')
        for pep_url in pep_list:
            number = pep_url.css('./text()').get()
            yield response.follow(pep_url, callback=self.parse_pep)

    def parse_pep(self, response):
        section = response.css('section#pep-content')
        status = section.css('dt:contains("Status") + dd::text').get()
        head = section.css('h1::text').get()
        head_split = head.split(' – ')
        number = head_split[0].split()[-1].strip()
        name = head_split[1].strip()
        yield PepParseItem(
            number=number,
            name=name,
            status=status,
        )
