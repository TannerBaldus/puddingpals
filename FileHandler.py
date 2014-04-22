from Validator import Validator
import csv
class FileHandler(object):

	def __init__(self):
         self.Validator = Validator()
         self.uspsFields = ['Last','Delivery','Second','Recipient','Phone']


	def ValidAttr(self, attrName, attr):
		""" Returns Empty String if Invalid, else returns sanitized attr"""
		if self.Validator.validateAttr(attrName, attr) :
			return self.Validator.sanitize(attr)

		return ''


	def splitLast(self,last):
		row = last.split(' ')
		stateIndex = None
		for index, el in enumerate(row):
			print el
			if self.Validator.isValidState(el):

				stateIndex = index

		if stateIndex:
			city = ' '.join(row[0:stateIndex])
			state = row[stateIndex]
			zipcode = row[stateIndex+1]
			return [city,state,zipcode]

		else:
			return ['','','']






	def readUSPS(self,filepath):
		tsv = open(filepath,'r')
		reader = csv.DictReader(tsv, delimiter='\t',restval='')
		attributes =[]

		for row in reader:
			attr ={} 
			print row
			last = self.splitLast(row['Last'])
			attr['name'] = row['Recipient']
			attr['phone'] = self.ValidAttr('phone',row['Phone'])
			attr['address'] = row['Delivery']
			attr['address2'] = row['Second']
			attr['city'] = self.ValidAttr('city',last[0])
			attr['state'] = self.ValidAttr('state',last[1])
			attr['zipcode'] = self.ValidAttr('zipcode',last[2])
			attributes.append(attr)
		return attributes




	def writeUSPS(self,contacts, filepath):
		tsv = open(filepath,'w')
		writer = csv.DictWriter(tsv, delimiter='\t', fieldnames=self.uspsFields)
		writer.writeheader()
		for contact in contacts:
			attributes ={}
			attributes['Recipient'] = contact.getAttr('name')
			last = [contact.getAttr('city'),contact.getAttr('state'),contact.getAttr('zipcode')]
			attributes['Last'] = ' '.join(last)
			attributes['Delivery'] = contact.getAttr('address2')
			attributes['Phone'] = contact.getAttr('phone')
			writer.writerow(attributes)

