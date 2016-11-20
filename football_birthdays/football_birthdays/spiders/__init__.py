# Stat 302 Project 2 Data collection spider.
# Crawling http://www.foxsports.com/nfl/players pages 1 through 168 for birthday information
# Copyright Evan Kivolowitz
# 11/20/16



import scrapy
from scrapy.selector import Selector

class FootballBirthdaysSpider(scrapy.Spider):
	name = "fbbday"
	
	def start_requests(self):
		start_url = "http://www.foxsports.com/nfl/players"
		yield scrapy.Request(start_url)


	def parse(self, response):
		baseurl = "http://www.foxsports.com"
		hasnext = response.xpath("//div[@class='wisbb_paginator']/a/text()").extract()
		if "Next" in hasnext[-1]:
			players = response.xpath("//a[@class='wisbb_fullPlayer']/@href").extract()
			for player in players:
				full_url = baseurl + player
				yield scrapy.Request(full_url, callback = self.parsePlayer)
			nextURL = response.xpath("//div[@class='wisbb_paginator']/a/@href").extract()
			yield scrapy.Request(baseurl + nextURL[-1], callback = self.parse)


	def parsePlayer(self, response):
		bday = response.xpath("//table[@class='wisfb_playerData']/tbody/tr[1]/td[2]/text()").extract()
		if '-' not in bday:
			f = open("fb_players.txt", 'a+')
			f.write(str(bday) + "\n")
			f.close()