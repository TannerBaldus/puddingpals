import csv
import unittest
import docopt


class Contact(object):
	def __init__(self,name,phone,address,zipcode):
		self.name = name
		self.phone = phone
		self.zipcode = zipcode
		self.address = address
		self.attrs = {'name':self.name,'phone':self.phone,'zipcode':self.zipcode}

	def getAttr(self,attr):
		"""We can use this to sort the contacts by attribute """
		return self.attrs[attr]

class AddressBook(object):

	def __init__(self,csvfile=''):
		self.contacts = []
		# csvfile = open(csvfile,'rb')
		# self.reader=reader(csvfile)


	def sort(self,attr,isDescending):
		contactAttr = lambda contact: contact.getAttr(attr)
		self.contacts.sort(key=contactAttr,reverse=isDescending)

	def addContact(self,name='',phone='',address='',zipcode=''):
		self.contacts.append(Contact(name, phone, address, zipcode))

	def removeContact(self,selected):
		removal = [self.contacts.remove(contact) for contact in selected]


	def readTSV(self,filepath):
		tsv = open(filepath,'r')
		reader = csv.reader=(tsv,delimiter='\t')



class ABTest(unittest.TestCase):

	def testAdd(self):
		ab = AddressBook()
		ab.addContact('Tester Mcgee','985.555.555','555 foo lane','70471')
		self.assertEqual( ab.contacts[0].name,'Tester Mcgee')

		
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
		selected = [ab.contacts[0]]
		ab.removeContact(selected)
		abNames = [contact.name for contact in ab.contacts]
		self.assertEqual(names[1:],abNames)






if __name__ == '__main__':
	unittest.main()









		
