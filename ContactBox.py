from Gui import *
from Validator import Validator

class ContactBox(wx.Frame):
    def __init__(self, gui, mode, name='', phone='', address='', address2='', city='', state='', zipcode='', index=0):
        wx.Frame.__init__(self, None, -1, "Contact Information", pos=wx.Point(50,120))
        self.states = ["","AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","PR","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
        self.gui = gui
        self.mode = mode
        self.index = index
        self.create_main_panel()
        self.nameBox.SetValue(name)
        self.phoneBox.SetValue(phone)
        self.addressBox.SetValue(address)
        self.address2Box.SetValue(address2)
        self.cityBox.SetValue(city)
        self.stateBox.SetValue(self.states[self.states.index(state)])
        self.zipBox.SetValue(zipcode)
        self.Validator = Validator()


    def create_main_panel(self):
        self.panel = wx.Panel(self)

        ##### User Controls
        self.nameLabel = wx.StaticText(self.panel, -1, "Name: ")
        self.nameBox = wx.TextCtrl(self.panel, size=(200,-1))
        self.phoneLabel = wx.StaticText(self.panel, -1, "Phone: ")
        self.phoneBox = wx.TextCtrl(self.panel, size=(200,-1))
        self.addressLabel = wx.StaticText(self.panel, -1, "Address: ")
        self.addressBox = wx.TextCtrl(self.panel, size=(200,-1))
        self.address2Label = wx.StaticText(self.panel, -1, "Address, cont.: ")
        self.address2Box = wx.TextCtrl(self.panel, size=(200,-1))
        self.cityLabel = wx.StaticText(self.panel, -1, "City: ")
        self.cityBox = wx.TextCtrl(self.panel, size=(200,-1))
        self.stateLabel = wx.StaticText(self.panel, -1, "State: ")
        self.stateBox = wx.ComboBox(self.panel, value=self.states[0], choices=self.states, style=wx.CB_READONLY)
        self.zipLabel = wx.StaticText(self.panel, -1, "Zip: ")
        self.zipBox = wx.TextCtrl(self.panel, size=(100,-1))
        self.addButton = wx.Button(self.panel, -1, "Save")
        self.Bind(wx.EVT_BUTTON, self.on_add, self.addButton)
        self.cancelButton = wx.Button(self.panel, -1, "Cancel")
        self.Bind(wx.EVT_BUTTON, self.on_cancel, self.cancelButton)

        ##### Box Sizers
        self.window = wx.BoxSizer(wx.VERTICAL)
        self.info = wx.BoxSizer(wx.HORIZONTAL)

        self.labels = wx.BoxSizer(wx.VERTICAL)
        self.labels.Add(self.nameLabel, 1, border=8, flag=wx.ALL)
        self.labels.Add(self.phoneLabel, 1, border=7, flag=wx.ALL)
        self.labels.Add(self.addressLabel, 1, border=7, flag=wx.ALL)
        self.labels.Add(self.address2Label, 1, border=7, flag=wx.ALL)
        self.labels.Add(self.cityLabel, 1, border=7, flag=wx.ALL)
        self.labels.Add(self.stateLabel, 1, border=7, flag=wx.ALL)
        self.labels.Add(self.zipLabel, 1, border=7, flag=wx.ALL)

        self.boxes = wx.BoxSizer(wx.VERTICAL)
        self.boxes.Add(self.nameBox, 1, border=5, flag=wx.ALL)
        self.boxes.Add(self.phoneBox, 1, border=3, flag=wx.ALL)
        self.boxes.Add(self.addressBox, 1, border=3, flag=wx.ALL)
        self.boxes.Add(self.address2Box, 1, border=3, flag=wx.ALL)
        self.boxes.Add(self.cityBox, 1, border=3, flag=wx.ALL)
        self.boxes.Add(self.stateBox, 1, border=3, flag=wx.ALL)
        self.boxes.Add(self.zipBox, 1, border=3, flag=wx.ALL)

        self.errors = wx.BoxSizer(wx.VERTICAL)
        self.nameError = wx.StaticText(self.panel, -1, "")
        self.phoneError = wx.StaticText(self.panel, -1, "")
        self.addressError = wx.StaticText(self.panel, -1, "")
        self.address2Error = wx.StaticText(self.panel, -1, "")
        self.cityError = wx.StaticText(self.panel, -1, "")
        self.stateError = wx.StaticText(self.panel, -1, "")
        self.zipError = wx.StaticText(self.panel, -1, "")
        self.errors.Add(self.nameError, 1, border=8, flag=wx.ALL)
        self.errors.Add(self.phoneError, 1, border=7, flag=wx.ALL)
        self.errors.Add(self.addressError, 1, border=7, flag=wx.ALL)
        self.errors.Add(self.address2Error, 1, border=7, flag=wx.ALL)
        self.errors.Add(self.cityError, 1, border=7, flag=wx.ALL)
        self.errors.Add(self.stateError, 1, border=7, flag=wx.ALL)
        self.errors.Add(self.zipError, 1, border=7, flag=wx.ALL)

        flags = wx.ALIGN_LEFT | wx.ALL
        self.info.Add(self.labels, 1, flag=flags)
        self.info.Add(self.boxes, 1, flag=flags)
        self.info.Add(self.errors, 1, flag=flags)

        self.buttons = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons.Add(self.addButton, 1, border=3, flag=wx.ALL)
        self.buttons.Add(self.cancelButton, 1, border=3, flag=wx.ALL)

        self.window.Add(self.info, 1, border=3, flag=wx.ALL)
        self.window.Add(self.buttons, 1, border=3, flag=wx.ALL)

        self.panel.SetSizer(self.window)
        self.window.Fit(self)
        self.SetSize(wx.Size(700,300))
        self.SetMinSize(wx.Size(700,300))
        self.SetMaxSize(wx.Size(700,300))


    def on_add(self, event):
        self.name = str(self.nameBox.GetValue())
        self.phone = str(self.phoneBox.GetValue())
        self.address = str(self.addressBox.GetValue())
        self.address2 = str(self.address2Box.GetValue())
        self.city = str(self.cityBox.GetValue())
        self.state = str(self.stateBox.GetValue())
        self.zipcode = str(self.zipBox.GetValue())

        if self.Validator.validName(self.name) and \
           self.Validator.isValidPhone(self.phone) and \
           self.Validator.validAddress(self.address) and \
           self.Validator.isValidCity(self.city) and \
           self.Validator.isValidState(self.state) and \
           self.Validator.isValidZip(self.zipcode):

            if self.mode == "add":
                self.gui.addressBook.addContact(**{"name": self.name, "phone": self.phone, "address": self.address, "address2": self.address2, "city": self.city, "state": self.state, "zipcode": self.zipcode})
                self.gui.addressBook.sort(self.gui.addressBook.sortMethod[0],self.gui.addressBook.sortMethod[1])
                self.gui.display()
                self.gui.flash_status_message("Added {}".format(str(self.name)))
                self.gui.addressBook.changed = True
                self.Destroy()
            if self.mode == "edit":
                del self.gui.addressBook.contacts[self.index]
                self.gui.addressBook.addContact(**{"name": self.name, "phone": self.phone, "address": self.address, "address2": self.address2, "city": self.city, "state": self.state, "zipcode": self.zipcode})
                self.gui.addressBook.sort(self.gui.addressBook.sortMethod[0],self.gui.addressBook.sortMethod[1])
                self.gui.display()
                self.gui.flash_status_message("Edited {}".format(str(self.name)))
                self.gui.addressBook.changed = True
                self.Destroy()
        else:
            self.nameError.SetLabel("")
            self.phoneError.SetLabel("")
            self.addressError.SetLabel("")
            self.address2Error.SetLabel("")
            self.cityError.SetLabel("")
            self.stateError.SetLabel("")
            self.zipError.SetLabel("")
            if not self.Validator.validName(self.name):
                self.nameError.SetLabel("Cannot be blank")
            if not self.Validator.isValidPhone(self.phone):
                self.phoneError.SetLabel("Invalid phone number")
            if not self.Validator.validAddress(self.address):
                self.addressError.SetLabel("Invalid Address")
            if not self.Validator.validAddress(self.address2):
                self.address2Error.SetLabel("Invalid Address")
            if not self.Validator.isValidCity(self.city):
                self.cityError.SetLabel("Invalid City")
            if not self.Validator.isValidState(self.state):
                self.stateError.SetLabel("Invalid State")
            if not self.Validator.isValidZip(self.zipcode):
                self.zipError.SetLabel("Must be ##### or #####-####")


    def on_cancel(self, event):
        self.Destroy()