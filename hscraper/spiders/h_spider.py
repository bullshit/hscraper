import scrapy

class HCrawler(scrapy.Spider):
	name = 'hcrawler'
	start_urls = []

	def test(self, response):
		self.logger.info('test %s',response.url)

	def __init__(self, filename=None):
		if filename:
			with open(filename, 'r') as f:
				for line in f:
					if not line.startswith('#'):
						self.start_urls.append(line);

	def parse(self, response):
		self.logger.info('Parse %s', response.url)

		for item_url in response.xpath('//a[contains(@itemprop, "url")]/@href').extract():
			yield scrapy.Request(response.urljoin(item_url), callback=self.parseDetails)

		next_page = response.css('li.next > a ::attr(href)').extract_first()
		if next_page:
			yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

	def parseDetails(self, response):
		self.logger.info('parseItem %s', response.url)
		latitude = response.xpath('//div[contains(@itemprop,"latitude")]/@content').extract_first()
		longitude = response.xpath('//div[contains(@itemprop,"longitude")]/@content').extract_first()
		if latitude is not None and longitude is not None:
			gmaps = "https://www.google.at/maps/place/"+latitude+"+"+longitude
		else:
			gmaps = ""
		#print response.xpath('//*[@id="companyResult"]/span/text()').extract_first()
		yield {
			'name' : response.xpath('//*[@id="companyResult"]/span/text()').extract_first(),
			'branche' : response.xpath('//*[@id="companyResult"]/span/small/text()').extract_first(),
			'adresse' : response.xpath('//span[contains(@itemprop,"streetAddress")]/text()').extract(),
			'plz' : response.xpath('//span[contains(@itemprop,"postalCode")]/text()').extract_first(),
			'ort' : response.xpath('//span[contains(@itemprop,"addressRegion")]/text()').extract_first(),
			#'tel' : response.xpath('//td[contains(@itemprop,"telephone")]/text()').extract(),
			'tel' : response.css('span.tel-number-full ::text').extract_first(),
			'fax' : response.xpath('//td[contains(@itemprop,"faxNumber")]/text()').extract_first(),
			'email' : response.xpath('//a[contains(@itemprop,"email")]/text()').extract_first(),
			'oeffnungszeiten' : response.css('#dataHours ::text').extract(),
			'gmaps' : gmaps,
			'url' : response.url
		}
		self.state['items_count'] = self.state.get('items_count', 0) + 1
