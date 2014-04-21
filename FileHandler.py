import csv
class FileHandler(object):

	def __init__(self):
		self.ValidateMethods{
		'phone': lambda phone: Validator.isValidPhone(phone),
		'city': lambda city: Validator.isValidCity(city),
		'state': lambda state: Validator.isValidState(state),
		'zipcode': lambda zipcode: Validator.isValidZip(zipcode)
		}



	def ValidAttr(self, attrName, attr):
		""" Returns Empty String if Invalid, else returns sanitized attr"""
		if self.ValidatMethods[attrName](attr):
			return Validator.sanitize(attr)
		return ''



	def readUSPS(self,row):

		attributes ={} 
		last = row['Last'].split(' ')
		attributes['name'] = row['Recipient']
		attributes['phone'] = self.ValidAttr('phone',row['Phone'])
		attributes['address'] = row['Delivery']
		attributes['address2'] = row['Second']
		attributes['city'] = self.ValidAttr('city',last[0])
		attributes['state'] = self.ValidAttr('state',last[1])
		attributes['zipcode'] = self.ValidAttr('zipcode',last[2])
		return attributes


	def writeUSPS(self,contact,dictwriter):
		attributes ={}
		attributes['Recipient'] = contact.getAttr('name')
		last = [contact.getAttr('city'),contact.getAttr('state'),contact.getAttr('zipcode')]
		attributes['Last'] = ' '.join(last)
		attributes['Delivery'] = contact.getAttr('address2')
		attributes['Phone'] = contact.getAttr('phone')
		dictwriter.writerow(attributes)

