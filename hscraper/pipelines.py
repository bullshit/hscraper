# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HscraperPipeline(object):
	def process_item(self, item, spider):
		openHours = []
		openHoursStr = ""

		item["bundesland"] = "unbekannt"
		if item['plz'][0] == '1':
			item["bundesland"] = "Wien"
		elif item['plz'][0] == '2':
			item["bundesland"] = "ost sued Niederoesterreich"
		elif item['plz'][0] == '3':
			item["bundesland"] = "Niederoesterreich"
		elif item['plz'][0] == '4':
			item["bundesland"] = "Oberoesterreich"
		elif item['plz'][0] == '5':
			item["bundesland"] = "Salzburg"
		elif item['plz'][0] == '6':
			item["bundesland"] = "Tirol Voralberg"
		elif item['plz'][0] == '7':
			item["bundesland"] = "Burgenland"
		elif item['plz'][0] == '8':
			item["bundesland"] = "Steiermark"
		elif item['plz'][0] == '9':
			item["bundesland"] = "Kaernten"



		if item['email']:
			item['email']=item['email'].replace('[at]','@').replace('[dot]','.')
		if item['tel']:
			item['tel']=item['tel'].replace(' ','')
		if item['fax']:
			item['fax']=item['fax'].replace(' ','')
		if item['oeffnungszeiten']:
			for tmp in item['oeffnungszeiten']:
				if (tmp != u'Öffnungszeiten') and ( not tmp.startswith(u'Mobil ')) :
					openHours.append(tmp.replace(',',' '))

			for count, i in enumerate(openHours):
				if count % 2 == 1:
					sep = "|"
				else:
					sep = " "
				openHoursStr+=i+sep
			item['oeffnungszeiten'] = openHoursStr[:-1]
		return item


