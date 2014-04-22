import csv
import re
import os.path
from string import punctuation


class Validator(object):

    def __init__(self):
        self.uspsFields = ['Last','Delivery','Second','Recipient','Phone']
        self.validateMethods={
            'phone': lambda phone: self.isValidPhone(phone),
            'city': lambda city: self.isValidCity(city),
            'state': lambda state: self.isValidState(state),
            'zipcode': lambda zipcode: self.isValidZip(zipcode),
            'name': lambda name: self.isValidName(name),

        }
        self.states= ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]







    def validateAttr(self,attrName,attr):
        return self.validateMethods[attrName](attr)



    def sanitize(self, string):
        exclude = {'\t':'    ','\n':''}
        for ch in exclude:
            string = string.replace(ch,exclude[ch])
        return string


    def isValidPhone(self, rawphone):
        phone = rawphone.translate(None,punctuation)
        if len(phone) < 7 and rawphone !='': return False
        return True

    def isValidZip(self,zipcode):
        if re.match("^\\d{5}(-\\d{4})?$",zipcode) or zipcode=='': return True
        return False

    def isValidCity(self,city):
        """Always Return True for now but might want to expand later"""
        return True

    def isValidState(self,state):
        if state in self.states:
            return True
        return False 

    def isValidName(self,name):
        if name: return True
        return False

    def isValidUSPS(self,filein):
        if os.path.isfile(filein) and filein.endswith('.tsv'):
            reader = csv.DictReader(filein)
            row = reader.next()
            return all(field in row for field in self.uspsFields)
        return False

    def isValidAddress(self,address):
        return True

if __name__ == '__main__':
    v = Validator()
    x = 'Hello \t Roger \n Rabbit'
    v.sanitize(x)
