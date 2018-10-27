# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class Oneplus6Spider(scrapy.Spider):
    name = 'oneplus6'
    allowed_domains = ['amazon.in']
    start_urls = ['https://www.amazon.in/OnePlus-Silk-White-128GB-Storage/product-reviews/B078BNQ2ZS/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&reviewerType=all_reviews&filterByStar=positive&pageNumber=1']


    def parse(self,response):
        yield from self.extract_reviews(response)


    def extract_reviews(self, response):
        items = AmazonreviewsItem()

        opinions = response.xpath('//*[@class="a-size-base a-link-normal review-title a-color-base a-text-bold"]/text()').extract()
        reviewers = response.xpath('//*[@class="a-size-base a-link-normal author"]/text()').extract()
        verified = response.xpath('//*[@class="a-size-mini a-color-state a-text-bold"]/text()').extract()
        ratings = response.xpath('//span[@class="a-icon-alt"]/text()').extract()


        for opinion in opinions:
            yield({'Opinion':opinion})

        for reviewer in reviewers:
            yield({'Reviewer':reviewer})

        for verified_buyer in verified:
            yield({'Verified_buyer':verified_buyer})

        for rating in ratings:
            yield({'Rating':rating[0]})
