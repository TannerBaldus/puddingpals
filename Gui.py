import wx
import sys
from AddressBook import *
from ContactBox import *

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
        m_exit = menu_file.Append(-1, "&Exit", "Exit Program")
        self.Bind(wx.EVT_MENU, self.on_exit, m_exit)
        menu_help = wx.Menu()
        m_about = menu_help.Append(-1, "&About\tF1", "About this application")
        self.Bind(wx.EVT_MENU, self.on_about, m_about)
        self.menubar.Append(menu_file, "&File")
        self.menubar.Append(menu_help, "&Help")
        self.SetMenuBar(self.menubar)
        self.statusbar = self.CreateStatusBar()


    def create_main_panel(self):
        self.panel = wx.Panel(self)

        ##### List of Contacts
        self.list = wx.ListCtrl(self.panel, -1, size=wx.Size(625,500), style=wx.LC_REPORT | wx.LC_SINGLE_SEL)
        self.list.InsertColumn(0, 'Name', width=175)
        self.list.InsertColumn(1, 'Phone', width=125)
        self.list.InsertColumn(2, 'Address', width=250)
        self.list.InsertColumn(3, 'Zip', width=75)
        self.display()

        ##### User Controls
        self.addButton = wx.Button(self.panel, -1, "+ Add")
        self.Bind(wx.EVT_BUTTON, self.on_add, self.addButton)
        self.removeButton = wx.Button(self.panel, -1, "- Remove")
        self.Bind(wx.EVT_BUTTON, self.on_remove, self.removeButton)
        self.editButton = wx.Button(self.panel, -1, "Edit")
        self.Bind(wx.EVT_BUTTON, self.on_edit, self.editButton)
        self.sortName = wx.Button(self.panel, -1, "Sort by Name")
        self.Bind(wx.EVT_BUTTON, self.on_sort_name, self.sortName)
        self.sortZip = wx.Button(self.panel, -1, "Sort by Zip")
        self.Bind(wx.EVT_BUTTON, self.on_sort_zip, self.sortZip)

        ##### Layout
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        flags = wx.ALIGN_LEFT | wx.ALL | wx.ALIGN_CENTER_VERTICAL
        self.hbox.Add(self.addButton, 0, border=5, flag=flags)
        self.hbox.Add(self.editButton, 0, border=5, flag=flags)
        self.hbox.Add(self.removeButton, 0, border=5, flag=flags)
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


    def show_contact(self, contact):
        index = self.list.InsertStringItem(sys.maxint, contact.getAttr('name'))
        self.list.SetStringItem(index, 1, contact.getAttr('phone'))
        self.list.SetStringItem(index, 2, contact.getAttr('address'))
        self.list.SetStringItem(index, 3, contact.getAttr('zipcode'))


    def on_add(self, event):
        cb = ContactBox(self, "add")
        cb.Show()


    def on_edit(self, event):
        i = self.list.GetFirstSelected()
        name = self.addressBook.contacts[i].getAttr('name')
        phone = self.addressBook.contacts[i].getAttr('phone')
        address = self.addressBook.contacts[i].getAttr('address')
        zip = self.addressBook.contacts[i].getAttr('zipcode')
        cb = ContactBox(self, "edit", name, phone, address, zip, index=i)
        cb.Show()


    def on_remove(self, event):
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


    def on_sort_name(self, event):
        if self.addressBook.sortMethod == ('name', False):
            self.addressBook.sortMethod = ('name',True)
            self.addressBook.sort('name',True)
            self.flash_status_message("Sorted address book by last name, Z-A")
        else:
            self.addressBook.sortMethod = ('name',False)
            self.addressBook.sort('name',False)
            self.flash_status_message("Sorted address book by last name, A-Z")
        self.display()


    def on_sort_zip(self, event):
        if self.addressBook.sortMethod == ('zipcode', False):
            self.addressBook.sortMethod = ('zipcode',True)
            self.addressBook.sort('zipcode',True)
            self.flash_status_message("Sorted address book by zip code, 9-0")
        else:
            self.addressBook.sortMethod = ('zipcode',False)
            self.addressBook.sort('zipcode',False)
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


    def on_save_as(self, event=0):
        default = self.saveName.split('/')
        if len(default) > 0:
            defaultName = default[len(default)-1]
        else:
            defaultName = ""
        saveFileDialog = wx.FileDialog(self, "Save .tsv file", "", defaultName, ".tsv files (*.tsv)|*.tsv", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if saveFileDialog.ShowModal() == wx.ID_CANCEL:
            return
        self.saveName = saveFileDialog.GetPath()
        self.addressBook.writeTSV(self.saveName)
        self.addressBook.changed = False
        self.flash_status_message("Saved address book as {}".format(self.saveName))


    def on_save(self, event):
        if self.saveName == "":
            self.on_save_as()
        else:
            self.addressBook.writeTSV(self.saveName)
            self.addressBook.changed = False
            self.flash_status_message("Saved address book {}".format(self.saveName))


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

if __name__ == "__main__":
    app = wx.App()
    app.frame = GUI()
    app.frame.Show()
    app.MainLoop()