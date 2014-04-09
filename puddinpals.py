import csv
import unittest


class Contact(object):
	def __init__(self,firstname,lastname,phone,address,zipcode):
		self.firstname = firstname
		self.lastname = lastname
		self.phone = phone
		self.zipcode = zipcode
		self.address = address

	def getAttr(self,attr):
		"""We can use this to sort the contacts by attribute """

		if attr=='firstname': return self.firstname
		elif attr='lastname': return self.lastname
		elif attr='phone': return self.phone
		elif attr=='zipcode': return self.zipcode
		elif attr=='address':return self.address


class AddressBook(object):

	def __init__(self,csvfile=''):
		self.contacts = []

	def sort(self,attr):
		contactAttr = lambda contact: contact.getAttr(attr)
		self.contacts.sort(key=contactAttr)

	def addContact(self,firstname='',lastname='',phone='',address='',zipcode=''):
		self.contacts += Contact(self,firstname,lastname,phone,address,zipcode)

class ABTest(unittest.TestCase):
	def __init__(self):
		super(ABTest,self).__init__()
		self.ab = AddressBook()

	def testAdd(self):
		self.ab.addContact('Tester','Mcgee','985.555.555','555 foo lane','70471')
		self.assertEqual( self.ab.contacts[0].firstname,'Tester')








		
