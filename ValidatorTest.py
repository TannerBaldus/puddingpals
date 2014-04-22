from Validator import Validator
import unittest
class ValidatorTest(unittest.TestCase):

	def testSanitize(self):
		v = Validator()
		bad = 'Hello\tRoger\n Rabbit'
		good = "Hello    Roger Rabbit"
		self.assertEqual(good,v.sanitize(bad))

	def testGoodZip(self):
		zipcode = '97401'
		self.assertTrue(Validator.isValidZip(zipcode))

	def testBadZip(self):
		zipcode = '7401'
		self.assertFalse(Validator.isValidZip(zipcode))

	def testGoodLongZip(self):
		zipcode = '97401-1234'
		self.assertTrue(Validator.isValidZip(zipcode))

	def testBadLongZip(self):
		zipcode = '97-4011282'
		self.assertFalse(Validator.isValidZip(zipcode))

	def testGoodPhone(self):
		phone = '985.377.9835'
		self.assertTrue(Validator.isValidPhone(phone))

	def  testDNETSV(self):
		"""tests if validator rejects files that don't exist"""
		filein = 'blah.tsv'
		self.assertFalse(Validator.isValidUSPS(filein))

		
	def testNonTSV(self):
		filein = 'testTSV/test.csv'
		self.assertFalse(Validator.isValidUSPS(filein))
		
	

if __name__ == '__main__':
	unittest.main()

