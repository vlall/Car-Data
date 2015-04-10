import json
import urllib2
import numpy 
import xlsxwriter
#url = ('https://api.edmunds.com/v1/api/incentive/incentiverepository/findincentivesbymodelyearidandzipcode?modelyearid=100537293&zipcode=90019&fmt=json&api_key=%s' % (identity) )

wb = xlsxwriter.Workbook('%s_Output.xlsx' % ('Name_blank'))

class Datafest: 
	def __init__(self, name):
		identity = 'XXXXXXXXX'
		json_data = urllib2.urlopen('https://api.edmunds.com/v1/api/incentive/incentiverepository/findincentivesbymodelyearidandzipcode?modelyearid=100537293&zipcode=90019&fmt=json&api_key=%s' % (identity))
		self.data = json.load(json_data)
		json_data.close()  
		self.name = name

	def display_name(self):
		return self.name

	def get_id(self):
		return self.data['id']	

	def array(self, data):
		for i in data:
			something1 = data[i]
			something2 = data[y]
			x = numpy.asarray([[something1, something2]])

	def add_data(self, datasheet):
		ws = wb.add_worksheet(datasheet)
wb.close()
