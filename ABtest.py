from AddressBook import AddressBook
from Contact import Contact
import unittest
class ABTest(unittest.TestCase):

	def testAdd(self):
		ab = AddressBook()
		attrs = {'name':'Tester Mcgee','phone':'985.555.555','address':'555 foo lane','zipcode':'70471'}
		ab.addContact(**attrs)
		self.assertEqual(ab.contacts[0].getAttr('name'),'Tester Mcgee')


		
	def testSort(self):
		names = ['Bane A','Adam C', 'Charles C']
		ab = AddressBook()
		self.fillAb(ab)
		ab.sort('name',False)
		abNames = [contact.getAttr('name') for contact in ab.contacts]
		self.assertEqual(names,abNames)



	def testRemove(self):
		ab = AddressBook()
		self.fillAb(ab) ## Adam Charles Bane
		names = ['Charles C','Bane A']
		selected = [0]
		ab.removeSelected(selected)
		abNames = [contact.getAttr('name') for contact in ab.contacts]
		self.assertEqual(names,abNames)


	def testLoadTSV(self):
		ab = AddressBook()
		filein = 'tester.tsv'
		ab.loadTSV(filein)
		self.assertEqual(ab.contacts[0].getAttr('name'),'Tanner Baldus')
		self.assertEqual(ab.contacts[1].getAttr('name'), 'Dean Baldus')


	def testWriteTSV(self):
		ab = AddressBook()
		self.fillAb(ab)
		ab.writeTSV('testero.tsv')
		ab2 = AddressBook()
		ab2.loadTSV('testero.tsv')
		abNames = [contact.getAttr('name') for contact in ab.contacts]
		ab2Names = [contact.getAttr('name') for contact in ab2.contacts]
		self.assertEqual(abNames,ab2Names)


	def fillAb(self, ab):
		names = ['Adam C','Bane A','Charles C']
		c1 = {'name':names[0],'phone':'555555555','address':'321 lane'}
		c2 = {'name':names[2],'phone':'555444333','address':'123 lane'}
		c3 = {'name':names[1],'phone':'555444222','address':'456 lane'}
		ab.addContact(**c1)
		ab.addContact(**c2)
		ab.addContact(**c3)


if __name__ == '__main__':
	ab = AddressBook()
	ab.loadTSV('tester.tsv')
	unittest.main()

