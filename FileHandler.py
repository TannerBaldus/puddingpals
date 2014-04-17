import csv
class Filehandler(object):

	def __init__(self):
		self.uspsFields = ['Recipient','Last','Delivery']

	def readUSPS(self,row):
		attributes ={}
	
		last = row['Last'].split(' ')
		attributes['name = row['Recipient'].split(' ')
		attributes['phone'] = row['Phone']
		attributes['address'] = row['Delivery']
		attributes['address2'] = row['Second']
		attributes['city'] = last[0]
		attributes['state'] = last[1]
		attributes['zipcode'] = last[2]

		zipcode = last[2]
		return Contact(**attributes)

	def writeUSPS(self,contact,writer):
		attributes['Recipient'] = contact.getAttr('name')
		last = [contact.getAttr('city'),contact.getAttr('state'),contact.getAttr('zipcode')]
		attributes['Last'] = ' '.join(last)
		attributes['Delivery'] = contact.getAttr('address2')
		attributes['phone'] = contact.getAttr('phone')

