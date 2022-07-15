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
            a_selector_list = tr.css('a')
            a_selector = a_selector_list[0]
            number = a_selector.xpath('./text()').get()
            name = a_selector_list[1].xpath('./text()').get()
            yield response.follow(
                a_selector,
                callback=self.parse_pep,
                cb_kwargs={'number': number, 'name': name}
            )

    def parse_pep(self, response, number, name):
        """Парсит страницу PEP, получает статус PEP."""
        section = response.css('section#pep-content')
        status = section.css('dt:contains("Status") + dd::text').get()
        yield PepParseItem(
            number=number,
            name=name,
            status=status,
        )
