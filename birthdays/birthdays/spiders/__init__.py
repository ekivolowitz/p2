# Stat 302 Project 2 Data collection spider.
# Crawling http://www.foxsports.com/mlb/players pages 1 through 116 for birthday information
# Copyright Evan Kivolowitz
# 11/20/16



import scrapy
from scrapy.selector import Selector

class BirthdaySpider(scrapy.Spider):
	name = "bday"
	
	def start_requests(self):
		start_url = "http://www.foxsports.com/mlb/players"
		yield scrapy.Request(start_url)


	def parse(self, response):
		baseurl = "http://www.foxsports.com"
		hasnext = response.xpath("//div[@class='wisbb_paginator']/a/text()").extract()
		if "Next" in hasnext[-1]:
		# 	f = open("output.txt", 'a+')
			nextpage = response.xpath("//div[@class='wisbb_paginator']/a/@href").extract()
			full_next_page = baseurl + nextpage[-1]
			info = response.xpath("//table['@class=wisbb_standardTable']/tbody/tr/td[6]/text()").extract()
			f = open("birthdays.txt", 'a+')
			for item in info:
				if "-" not in item:
					f.write(item + '\n')
			f.close()


		# 	f.write(full_next_page + "\n")
		# 	f.close()
			yield scrapy.Request(full_next_page, callback = self.parse)
		

		# info = response.xpath("//table['@class=wisbb_standardTable']/tbody/tr/td[6]/text()").extract()
		# for item in info:
		# 	if "-" not in item:
		# 		f = open("birthdays.txt", 'a+')
		# 		f.write(item + '\n')
		# 		f.close()
