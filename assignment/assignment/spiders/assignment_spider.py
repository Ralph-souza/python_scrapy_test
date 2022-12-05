import scrapy
import re


class ContactsSpider(scrapy.Spider):
    name = "company_info"

    def start_requests(self):
        """
        Reads a .txt file containing a list of companies in dynamic way.
        It is necessary to describe de absolute route to make it readable.
        """
        url_list = open("/home/ralph/Udemy/python_scrapy_test/url_list.txt")
        for url in url_list:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        """
        Gather information from the websites in the list and place them into a .json file
        """
        extract_logo_pattern = r"(https?:\/\/.*\.(?:svg))"
        for img in response.css("img").xpath("@src").getall():
            logo_match = re.match(extract_logo_pattern, img)
            if logo_match is not None:
                yield {
                    'logo': img,
                }
