import scrapy
import re


class TestSpider(scrapy.Spider):
    name = 'test'

    start_urls = [
        'https://www.7comm.com.br/'
    ]

    def parse(self, response, **kwargs):
        extract_logo_pattern = r"(https?:\/\/.*\.(?:svg))"
        for img in response.css("img").xpath("@src").getall():
            logo_match = re.match(extract_logo_pattern, img)
            if logo_match is not None:
                yield {
                    'logo': img,
                }
