from Validator import Validator
import unittest
class ValidatorTest(unittest.TestCase):

    def testSanitize(self):
        v = Validator()
        bad = 'Hello\tRoger\n Rabbit'
        good = "Hello    Roger Rabbit"
        self.assertEqual(good,v.sanitize(bad))

    def testGoodZip(self):
        v = Validator()
        zipcode = '97401'
        self.assertTrue(v.isValidZip(zipcode))

    def testBadZip(self):
        v = Validator()
        zipcode = '7401'
        self.assertFalse(v.isValidZip(zipcode))

    def testGoodLongZip(self):
        v = Validator()
        zipcode = '97401-1234'
        self.assertTrue(v.isValidZip(zipcode))

    def testBadLongZip(self):
        v = Validator()
        zipcode = '97-4011282'
        self.assertFalse(v.isValidZip(zipcode))

    def testGoodPhone(self):
        v = Validator()
        phone = '985.377.9835'
        self.assertTrue(v.isValidPhone(phone))

    def  testDNETSV(self):
        v = Validator()
        """tests if v rejects files that don't exist"""
        filein = 'blah.tsv'
        self.assertFalse(v.isValidUSPS(filein))

        
    def testNonTSV(self):
        v = Validator()
        filein = 'testTSV/test.csv'
        self.assertFalse(v.isValidUSPS(filein))
        
    

if __name__ == '__main__':
    unittest.main()

