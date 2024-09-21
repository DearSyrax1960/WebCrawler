import scrapy


class YorkuCourseSpider(scrapy.Spider):
    name = 'courses'
    start_urls = ['https://futurestudents.yorku.ca/program-search/']

    custom_settings = {
            'FEEDS': {
                'outputs/yorku_courses.json': {
                    'format': 'json',
                    'overwrite': True,
                },
            }
    }

    def parse(self, response):
        urls = response.css('div.program a::attr(href)').getall()

        for url in urls:
            yield scrapy.Request(response.urljoin(url), callback=self.parse_url)

    def parse_url(self, response):
        data = {
            f"{response.css('.wp-block-group .wp-block-columns .wp-block-column:nth-child(1) h3::text').get().strip()}": response.css('.wp-block-group .wp-block-columns .wp-block-column:nth-child(1) p::text').get(),
            f"{response.css('.wp-block-group .wp-block-columns .wp-block-column:nth-child(2) h3::text').get().strip()}": response.css('.wp-block-group .wp-block-columns .wp-block-column:nth-child(2) p::text').get(),
            f"{response.css('.wp-block-group .wp-block-columns .wp-block-column:nth-child(3) h3::text').get().strip()}": response.css('.wp-block-group .wp-block-columns .wp-block-column:nth-child(3) p::text').get(),
            'program link': response.url,
        }
        yield data
