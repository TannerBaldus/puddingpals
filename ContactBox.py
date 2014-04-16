from Gui import *

class ContactBox(wx.Frame):
    def __init__(self, gui, mode, name='', phone='', address='', zip='', index=0):
        wx.Frame.__init__(self, None, -1, "Contact Information", pos=wx.Point(100,100))
        self.gui = gui
        self.mode = mode
        self.index = index
        self.create_main_panel()
        self.nameBox.SetValue(name)
        self.phoneBox.SetValue(phone)
        self.addressBox.SetValue(address)
        self.zipBox.SetValue(zip)


    def create_main_panel(self):
        self.panel = wx.Panel(self)

        ##### User Controls
        self.nameLabel = wx.StaticText(self.panel, -1, "Name: ")
        self.nameBox = wx.TextCtrl(self.panel, size=(125,-1))
        self.phoneLabel = wx.StaticText(self.panel, -1, "Phone: ")
        self.phoneBox = wx.TextCtrl(self.panel, size=(125,-1))
        self.addressLabel = wx.StaticText(self.panel, -1, "Address: ")
        self.addressBox = wx.TextCtrl(self.panel, size=(250,-1))
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
        self.labels.Add(self.nameLabel, 1, border=5, flag=wx.ALL)
        self.labels.Add(self.phoneLabel, 1, border=5, flag=wx.ALL)
        self.labels.Add(self.addressLabel, 1, border=5, flag=wx.ALL)
        self.labels.Add(self.zipLabel, 1, border=5, flag=wx.ALL)

        self.boxes = wx.BoxSizer(wx.VERTICAL)
        self.boxes.Add(self.nameBox, 1, border=3, flag=wx.ALL)
        self.boxes.Add(self.phoneBox, 1, border=3, flag=wx.ALL)
        self.boxes.Add(self.addressBox, 1, border=3, flag=wx.ALL)
        self.boxes.Add(self.zipBox, 1, border=3, flag=wx.ALL)

        flags = wx.ALIGN_LEFT | wx.ALL
        self.info.Add(self.labels, 1, flag=flags)
        self.info.Add(self.boxes, 1, flag=flags)

        self.buttons = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons.Add(self.addButton, 1, border=3, flag=wx.ALL)
        self.buttons.Add(self.cancelButton, 1, border=3, flag=wx.ALL)

        self.window.Add(self.info, 1, border=3, flag=wx.ALL)
        self.window.Add(self.buttons, 1, border=3, flag=wx.ALL)

        self.panel.SetSizer(self.window)
        self.window.Fit(self)
        self.SetSize(wx.Size(325,180))


    def on_add(self, event):
        self.name = self.nameBox.GetValue()
        self.address = self.addressBox.GetValue()
        self.zip = self.zipBox.GetValue()
        self.phone = self.phoneBox.GetValue()
        #valid = self.gui.addressBook.validate(self.name,self.address,self.zip,self.phone)
        valid = True
        if valid:
            if self.mode == "add":
                self.gui.addressBook.addContact(self.name, self.phone, self.address, self.zip)
                self.gui.addressBook.sort(self.gui.addressBook.sortMethod[0],self.gui.addressBook.sortMethod[1])
                self.gui.display()
                self.gui.flash_status_message("Added {}".format(str(self.name)))
                self.gui.addressBook.changed = True
                self.Destroy()
            if self.mode == "edit":
                del self.gui.addressBook.contacts[self.index]
                self.gui.addressBook.addContact(self.name, self.phone, self.address, self.zip)
                self.gui.addressBook.sort(self.gui.addressBook.sortMethod[0],self.gui.addressBook.sortMethod[1])
                self.gui.display()
                self.gui.flash_status_message("Edited {}".format(str(self.name)))
                self.gui.addressBook.changed = True
                self.Destroy()

    def on_cancel(self, event):
        self.Destroy()

if __name__ == "__main__":
    app = wx.App()
    app.frame = ContactBox('foo')
    app.frame.Show()
    app.MainLoop()