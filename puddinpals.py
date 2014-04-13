import csv
import unittest
import docopt

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






class AddressBook(object):

	def __init__(self,csvfile=''):
		self.contacts = []  ##holds contact objects
		# csvfile = open(csvfile,'rb')
		# self.reader=reader(csvfile)


	def sort(self,attr,isDescending):
		contactAttr = lambda contact: contact.getAttr(attr)
		self.contacts.sort(key=contactAttr,reverse=isDescending)

	def addContact(self,name='',phone='',address='',zipcode=''):
		""" adds new contact instance to contact list """
		self.contacts.append(Contact(name, phone, address, zipcode))

	def removeContact(self,selected):
		"""remove contact list from self.contacts """
		for index in selected:
			del self.contacts[index]


	def loadTSV(self, filepath):
		tsv = open(filepath,'r')
		reader = csv.DictReader(tsv,delimiter='\t')
		for row in reader:
			contact = Contact(row['name'],row['phone'], row['address'], row['zip'])
			self.contacts.append(contact)




class ABTest(unittest.TestCase):

	def testAdd(self):
		ab = AddressBook()
		ab.addContact('Tester Mcgee','985.555.555','555 foo lane','70471')
		self.assertEqual(ab.contacts[0].name,'Tester Mcgee')


		
	def testSort(self):
		ab = AddressBook()
		names = ['Adam','Bane','Charles']
		ab.addContact(names[2])
		ab.addContact(names[1])
		ab.addContact(names[0])
		ab.sort('name',False)
		abNames = [contact.name for contact in ab.contacts]
		self.assertEqual(names,abNames)

	def testRemove(self):
		ab = AddressBook()
		names = ['Adam','Bane','Charles']
		ab.addContact(names[0])
		ab.addContact(names[1])
		ab.addContact(names[2])
		selected = [0]
		ab.removeContact(selected)
		abNames = [contact.name for contact in ab.contacts]
		self.assertEqual(names[1:],abNames)

	def testLoadTSV(self):
		ab = AddressBook()
		filein = 'tester.tsv'
		ab.loadTSV(filein)
		self.assertEqual(ab.contacts[0].name,'Tanner Baldus')
		self.assertEqual(ab.contacts[1].name, 'Dean Baldus')






if __name__ == '__main__':
	unittest.main()









		
