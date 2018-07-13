# -*- coding: utf-8 -*-
import scrapy


class IndeedSpider(scrapy.Spider):
    name = 'indeed'
    allowed_domains = ['https://www.indeed.co.uk/jobs?q=python&l=West+Midlands']
    start_urls = ['https://www.indeed.co.uk/jobs?q=python&l=West+Midlands']

    def get_all_jobs_fromPage(self, page):
        for job in page:
            yield (job.css('a::attr(href)').extract_first())

    def get_job_link(self, page_source):
        jobs = self.get_all_jobs_fromPage(page_source)
        for link in jobs:
            job = 'https://www.indeed.co.uk' + link
            yield job

    def get_job_info(self, page_source):
        info = self.get_job_link(page_source)
        for page in info:
            self.log(page)


    def parse(self, response):

        page_source = response.css('div.row.result')
        self.get_job_info(page_source)




# job = response.css('div.row.result')[0]
#job.css('a::attr(href)').extract_first()
#for job in response.css('div.row.result'):
#    item = {
#        'jobTitle': job.css('a.jobtitle::text').extract(),
#        'location': job.css('span.location::text').extract(),
#        'summary': job.css('span.summary::text').extract(),
#    }
#    yield item
#next_page = response.css('div.pagination > a::attr(href)')
#self.log("_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+")
#self.log(next_page)
#allowed_domains += next_page
#self.log("_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+")
#self.log(next_page)



# scrapy runspider Indeed.py --output test.json
# more test.json