import csv
import re
import os.path
from string import punctuation


class Validator(object):
    def __init__(self):
        pass

    @staticmethod
    def sanitize(string):
        exclude = {'\t':'    ','\n':''}
        for ch in exclude:
            string = string.replace(ch,exclude[ch])
        return string


    @staticmethod
    def isValidName(name):
        if name == "":
            return False
        return True


    @staticmethod
    def isValidPhone(rawphone):
        phone = rawphone.translate(None,punctuation)
        if len(phone) < 7 and phone != "": return False
        return True


    @staticmethod
    def isValidCity(city):
        """Always Return True for now but might want to expand later"""
        return True


    @staticmethod
    def isValidState(state):
        """"""
        if state in ["","AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","PR","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]:
            return True
        return False


    @staticmethod
    def isValidZip(zipcode):
         if re.match("^\\d{5}(-\\d{4})?$",zipcode) or zipcode == "": return True
         return False


    @staticmethod
    def isValidTSV(filein):
        return True


    @staticmethod
    def isValidUSPS(filein):
        if os.path.isfile(filein) and filein.endswith('.tsv') :
            fields = ['Last','Delivery','Second','Recipient','Phone']
            reader = csv.DictReader(filein)
            row = reader.next()
            return all(field in row.keys for field in fields)
        return False


    """@staticmethod
    def isValidUSPS(self,filein):
        reader = csv.DictReader(filein)
        row = reader.next()
        return all(field in row for field in self.uspsFields)"""




if __name__ == '__main__':
    v = Validator()
    x = 'Hello \t Roger \n Rabbit'
    v.sanitize(x)