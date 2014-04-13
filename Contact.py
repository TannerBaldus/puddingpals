class Contact(object):
	def __init__(self,name,phone,address,zipcode):
		self.name = name
		self.phone = phone
		self.zipcode = zipcode
		self.address = address
		self.attrs = {'name':self.name,'phone':self.phone,'zipcode':self.zipcode,'address':self.address}

	def getAttr(self,attr):
		"""We can use this to sort the contacts by attribute """
		return self.attrs[attr]

	def setName(self,name):
		self.name = name

	def setPhone(self,phone):
		self.phone = phone

	def setZip(self,zipcode):
		self.zipcode = zipcode

	def setAddress(self,address):
		self.address = address