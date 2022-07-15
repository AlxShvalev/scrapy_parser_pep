import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Парсит страницу PEP-0, переходит по ссылкам каждого PEP."""
        section_selector = response.css('section#numerical-index')
        tbody_selector = section_selector.css('tbody')
        tr_selector_list = tbody_selector.css('tr')
        for tr in tr_selector_list:
            pep_link = tr.css('a').attrib['href']
            yield response.follow(
                pep_link,
                callback=self.parse_pep,
            )

    def parse_pep(self, response):
        """Парсит страницу PEP, получает статус PEP."""
        section = response.css('section#pep-content')
        h1 = section.css('h1::text').get()
        h1_to_list = h1.split(' – ')
        pep_num = h1_to_list[0].strip().split()
        number = pep_num[1].strip()
        name = h1_to_list[1].strip()
        status = section.css('dt:contains("Status") + dd::text').get().strip()
        yield PepParseItem(
            number=number,
            name=name,
            status=status,
        )
