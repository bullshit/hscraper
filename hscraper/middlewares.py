import os
import random
from scrapy.conf import settings
import logging

class RandomUserAgentMiddleware(object):
	def process_request(self, request, spider):
		ua  = random.choice(settings.get('USER_AGENT_LIST'))
		if ua:
			logging.debug("Using User-Agent %s",ua)
			request.headers.setdefault('User-Agent', ua)
			