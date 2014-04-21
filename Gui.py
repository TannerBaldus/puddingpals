import wx
import sys
from AddressBook import *
from ContactBox import ContactBox

class GUI(wx.Frame):
    title = "Jello Puddin' Pals"
    def __init__(self):
        wx.Frame.__init__(self, None, -1, self.title, wx.Point(30,30))
        self.addressBook = AddressBook()
        self.saveName = ""
        self.create_menu()
        self.create_main_panel()


    def create_menu(self):
        ##### Menu Bar
        self.Bind(wx.EVT_CLOSE, self.on_exit, self)
        self.menubar = wx.MenuBar()

        menu_file = wx.Menu()
        m_open = menu_file.Append(-1, "&New", "New Address Book")
        self.Bind(wx.EVT_MENU, self.on_new, m_open)
        m_open = menu_file.Append(-1, "&Open", "Open Address Book")
        self.Bind(wx.EVT_MENU, self.on_open, m_open)
        m_save = menu_file.Append(-1, "&Save", "Save Address Book")
        self.Bind(wx.EVT_MENU, self.on_save, m_save)
        m_save_as = menu_file.Append(-1, "&Save as...", "Save Address Book as...")
        self.Bind(wx.EVT_MENU, self.on_save_as, m_save_as)
        m_import = menu_file.Append(-1, "&Import", "Import Address Book")
        self.Bind(wx.EVT_MENU, self.on_import, m_import)
        m_export = menu_file.Append(-1, "&Export", "Export Address Book")
        self.Bind(wx.EVT_MENU, self.on_export, m_export)
        m_exit = menu_file.Append(-1, "&Exit", "Exit Program")
        self.Bind(wx.EVT_MENU, self.on_exit, m_exit)

        menu_contact = wx.Menu()
        m_add = menu_contact.Append(-1, "&Add New Contact", "Add New Contact to Address Book")
        self.Bind(wx.EVT_MENU, self.on_add, m_add)
        m_edit = menu_contact.Append(-1, "&Edit Selected", "Edit Selected Contact")
        self.Bind(wx.EVT_MENU, self.on_edit, m_edit)
        m_remove = menu_contact.Append(-1, "&Remove Selected", "Remove Selected Contact from Address Book")
        self.Bind(wx.EVT_MENU, self.on_remove, m_remove)
        m_print = menu_contact.Append(-1, "Get Mailing Label", "Get Mailing Label for Selected Contact")
        self.Bind(wx.EVT_MENU, self.on_print, m_print)

        menu_help = wx.Menu()
        m_about = menu_help.Append(-1, "&About", "About this application")
        self.Bind(wx.EVT_MENU, self.on_about, m_about)
        self.menubar.Append(menu_file, "&File")
        self.menubar.Append(menu_contact, "&Contact")
        self.menubar.Append(menu_help, "&Help")
        self.SetMenuBar(self.menubar)
        self.statusbar = self.CreateStatusBar()


    def create_main_panel(self):
        self.panel = wx.Panel(self)

        ##### List of Contacts
        self.list = wx.ListCtrl(self.panel, -1, size=wx.Size(775,500), style=wx.LC_REPORT | wx.LC_SINGLE_SEL)
        self.list.InsertColumn(0, 'Name', width=150)
        self.list.InsertColumn(1, 'Phone', width=125)
        self.list.InsertColumn(2, 'Address', width=150)
        self.list.InsertColumn(3, 'Address, cont.', width=100)
        self.list.InsertColumn(4, 'City', width=125)
        self.list.InsertColumn(5, 'State', width=50)
        self.list.InsertColumn(6, 'Zip', width=75)
        self.display()

        ##### User Controls
        self.addButton = wx.Button(self.panel, -1, "+ Add", size=wx.Size(80,20))
        self.Bind(wx.EVT_BUTTON, self.on_add, self.addButton)
        self.removeButton = wx.Button(self.panel, -1, "- Remove", size=wx.Size(80,20))
        self.Bind(wx.EVT_BUTTON, self.on_remove, self.removeButton)
        self.editButton = wx.Button(self.panel, -1, "Edit", size=wx.Size(80,20))
        self.Bind(wx.EVT_BUTTON, self.on_edit, self.editButton)
        self.printButton = wx.Button(self.panel, -1, "Mail Label", size=wx.Size(80,20))
        self.Bind(wx.EVT_BUTTON, self.on_print, self.printButton)
        self.sortName = wx.Button(self.panel, -1, u"Sort by Name \u25B2", size=wx.Size(120,20))
        self.Bind(wx.EVT_BUTTON, self.on_sort_name, self.sortName)
        self.sortZip = wx.Button(self.panel, -1, u"Sort by Zip", size=wx.Size(120,20))
        self.Bind(wx.EVT_BUTTON, self.on_sort_zip, self.sortZip)

        ##### Layout
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        flags = wx.ALIGN_LEFT | wx.ALL | wx.ALIGN_CENTER_VERTICAL
        self.hbox.Add(self.addButton, 0, border=5, flag=flags)
        self.hbox.Add(self.editButton, 0, border=5, flag=flags)
        self.hbox.Add(self.removeButton, 0, border=5, flag=flags)
        self.hbox.Add(self.printButton, 0, border=5, flag=flags)
        self.hbox.AddStretchSpacer()
        self.hbox.Add(self.sortName, 0, border=5, flag=wx.ALIGN_RIGHT | wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        self.hbox.Add(self.sortZip, 0, border=5, flag=wx.ALIGN_RIGHT | wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        self.vbox.Add(self.hbox, 0, flag = wx.ALIGN_LEFT | wx.TOP | wx.EXPAND)
        self.vbox.Add(self.list, 1, border=5, flag = wx.ALL | wx.GROW)
        self.panel.SetSizer(self.vbox)
        self.vbox.Fit(self)


    ##### Functionality
    def display(self):
        self.list.DeleteAllItems()
        for contact in self.addressBook.contacts:
            self.show_contact(contact)
        if self.saveName != "":
            file = self.saveName.split('/')
            self.SetTitle("Jello Puddin' Pals - {}".format(file[len(file)-1]))


    def show_contact(self, contact):
        index = self.list.InsertStringItem(sys.maxint, contact.getAttr('name'))
        self.list.SetStringItem(index, 1, contact.getAttr('phone'))
        self.list.SetStringItem(index, 2, contact.getAttr('address'))
        self.list.SetStringItem(index, 3, contact.getAttr('address2'))
        self.list.SetStringItem(index, 4, contact.getAttr('city'))
        self.list.SetStringItem(index, 5, contact.getAttr('state'))
        self.list.SetStringItem(index, 6, contact.getAttr('zipcode'))

    def on_add(self, event):
        cb = ContactBox(self, "add")
        cb.Show()


    def on_edit(self, event):
        if len(self.addressBook.contacts)>0:
            i = self.list.GetFirstSelected()
            name = self.addressBook.contacts[i].getAttr('name')
            phone = self.addressBook.contacts[i].getAttr('phone')
            address = self.addressBook.contacts[i].getAttr('address')
            address2 = self.addressBook.contacts[i].getAttr('address2')
            city = self.addressBook.contacts[i].getAttr('city')
            state = self.addressBook.contacts[i].getAttr('state')
            zipcode = self.addressBook.contacts[i].getAttr('zipcode')
            cb = ContactBox(self, "edit", name, phone, address, address2, city, state, zipcode, index=i)
            cb.Show()
        else:
            self.flash_status_message("Address book is empty")


    def on_remove(self, event):
        if len(self.addressBook.contacts)>0:
            i = self.list.GetFirstSelected()
            name = self.addressBook.contacts[i].getAttr('name')
            dlg = wx.MessageDialog(self, "Are you sure you want to remove {}?".format(name), "Confirm Delete", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
            result = dlg.ShowModal()
            dlg.Destroy()
            if result == wx.ID_OK:
                del self.addressBook.contacts[i]
                self.addressBook.sort(self.addressBook.sortMethod[0],self.addressBook.sortMethod[1])
                self.display()
                self.addressBook.changed = True
                self.flash_status_message("Removed {}".format(name))
        else:
            self.flash_status_message("Address book is empty")


    def on_sort_name(self, event):
        if self.addressBook.sortMethod == ('name', False):
            self.addressBook.sortMethod = ('name',True)
            self.addressBook.sort('name',True)
            self.sortName.SetLabel(u"Sort by Name \u25BC")
            self.sortZip.SetLabel(u"Sort by Zip")
            self.flash_status_message("Sorted address book by last name, Z-A")
        else:
            self.addressBook.sortMethod = ('name',False)
            self.addressBook.sort('name',False)
            self.sortName.SetLabel(u"Sort by Name \u25B2")
            self.sortZip.SetLabel(u"Sort by Zip")
            self.flash_status_message("Sorted address book by last name, A-Z")
        self.display()


    def on_sort_zip(self, event):
        if self.addressBook.sortMethod == ('zipcode', False):
            self.addressBook.sortMethod = ('zipcode',True)
            self.addressBook.sort('zipcode',True)
            self.sortZip.SetLabel(u"Sort by Zip \u25BC")
            self.sortName.SetLabel(u"Sort by Name")
            self.flash_status_message("Sorted address book by zip code, 9-0")
        else:
            self.addressBook.sortMethod = ('zipcode',False)
            self.addressBook.sort('zipcode',False)
            self.sortZip.SetLabel(u"Sort by Zip \u25B2")
            self.sortName.SetLabel(u"Sort by Name")
            self.flash_status_message("Sorted address book by zip code, 0-9")
        self.display()


    ##### Menu functions
    def on_new(self, event):
        if self.addressBook.changed:
            if wx.MessageBox("This address book contains unsaved changes! Continue anyway?", "Are you sure?", wx.ICON_QUESTION | wx.YES_NO, self) == wx.NO:
                return
        newGui = GUI()
        newGui.display()
        newGui.Show()
        self.Destroy()


    def on_open(self, event):
        if self.addressBook.changed:
            if wx.MessageBox("This address book contains unsaved changes! Continue anyway?", "Are you sure?", wx.ICON_QUESTION | wx.YES_NO, self) == wx.NO:
                return
        openFileDialog = wx.FileDialog(self, "Open .tsv file", "", "", ".tsv files (*.tsv)|*.tsv", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return
        inFilePath = openFileDialog.GetPath()
        newGui = GUI()
        newGui.addressBook.loadTSV(inFilePath)
        newGui.saveName = inFilePath
        newGui.addressBook.sort('name',False)
        newGui.display()
        newGui.Show()
        newGui.flash_status_message("Opened address book {}".format(newGui.saveName))
        self.Destroy()


    def on_save_as(self, mode):
        defaultName = ""
        if mode != 1:
            default = self.saveName.split('/')
            if len(default) > 0:
                defaultName = default[len(default)-1]
        saveFileDialog = wx.FileDialog(self, "Save .tsv file", "", defaultName, ".tsv files (*.tsv)|*.tsv", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if saveFileDialog.ShowModal() == wx.ID_CANCEL:
            return
        self.saveName = saveFileDialog.GetPath()
        self.addressBook.writeTSV(self.saveName)
        self.addressBook.changed = False
        self.flash_status_message("Saved address book as {}".format(self.saveName))


    def on_import(self, event):
        openFileDialog = wx.FileDialog(self, "Import .tsv file", "", "", ".tsv files (*.tsv)|*.tsv", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return
        inFilePath = openFileDialog.GetPath()
        temp = AddressBook()
        temp.loadTSV(inFilePath)
        for contact in temp.contacts:
            self.addressBook.contacts.append(contact)
        self.addressBook.sort(self.addressBook.sortMethod[0],self.addressBook.sortMethod[1])
        self.display()
        self.flash_status_message("Imported address book {}".format(inFilePath))
        self.addressBook.changed = True


    def on_export(self, event):
        self.on_save_as(mode=1)


    def on_save(self, event):
        if self.saveName == "":
            self.on_save_as(mode=0)
        else:
            self.addressBook.writeTSV(self.saveName)
            self.addressBook.changed = False
            self.flash_status_message("Saved address book {}".format(self.saveName))


    def on_print(self, event):
        if len(self.addressBook.contacts)>0:
            i = self.list.GetFirstSelected()
            mail = self.addressBook.contacts[i].getLabel()
            dlg = wx.MessageDialog(self, mail, "USPS Mailing Label", wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
        else:
            self.flash_status_message("Address book is empty")


    def on_exit(self, event):
        if self.addressBook.changed:
            if wx.MessageBox("This address book contains unsaved changes! Exit anyway?", "Are you sure?", wx.ICON_QUESTION | wx.YES_NO, self) == wx.NO:
                return
        self.Destroy()


    def on_about(self, event):
        msg = "Bill Cosby's Eligible Bachelors of Science"
        dlg = wx.MessageDialog(self, msg, "About", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()


    def flash_status_message(self, msg, flash_len_ms=3000):
        self.statusbar.SetStatusText(msg)
        self.timeroff = wx.Timer(self)
        self.Bind(
            wx.EVT_TIMER,
            self.on_flash_status_off,
            self.timeroff)
        self.timeroff.Start(flash_len_ms, oneShot=True)
    def on_flash_status_off(self, event):
        self.statusbar.SetStatusText('')