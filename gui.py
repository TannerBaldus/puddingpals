import wx

class GUI(wx.Frame):
    title = "Jello Puddin' Pals"
    def __init__(self):
        wx.Frame.__init__(self, None, -1, self.title, wx.Point(30,30))
        self.create_menu()
        self.create_main_panel()


    def create_menu(self):
        self.menubar = wx.MenuBar()
        menu_file = wx.Menu()
        m_exit = menu_file.Append(-1, "&Exit\tCrl-X", "Exit")
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
        self.contacts = wx.ListBox(self.panel, -1, size=wx.Size(500, 400))
        ##### Min Degree controls
        self.addButton = wx.Button(self.panel, -1, "Create New Contact")
        self.Bind(wx.EVT_BUTTON, self.on_add, self.addButton)
        self.editButton = wx.Button(self.panel, -1, "Edit Contact Information")
        self.Bind(wx.EVT_BUTTON, self.on_edit, self.editButton)
        self.removeButton = wx.Button(self.panel, -1, "Remove Current Contact")
        self.Bind(wx.EVT_BUTTON, self.on_remove, self.removeButton)
        ##### Box sizers
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        flags = wx.ALIGN_LEFT | wx.ALL | wx.ALIGN_CENTER_VERTICAL
        self.hbox.Add(self.addButton, 0, border=5, flag=flags)
        self.hbox.Add(self.editButton, 0, border=5, flag=flags)
        self.hbox.Add(self.removeButton, 0, border=5, flag=flags)
        self.vbox.Add(self.hbox, 0, flag = wx.ALIGN_LEFT | wx.TOP)
        self.vbox.Add(self.contacts, 1, border=5, flag = wx.ALL | wx.GROW)
        self.panel.SetSizer(self.vbox)
        self.vbox.Fit(self)


    def on_add(self, event):
        self.flash_status_message("This button opens a dialog box prompting the user to create a new contact.")


    def on_edit(self, event):
        self.flash_status_message("This button allows the user to edit the information for the currently selected contact.")


    def on_remove(self, event):
        self.flash_status_message("This button deletes the currently selected contact from the address book.")


    def on_about(self, event):
        msg = "Bill Cosby's Eligible Bachelors of Science"
        dlg = wx.MessageDialog(self, msg, "About", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()


    def on_exit(self, event):
        self.Destroy()


    def flash_status_message(self, msg, flash_len_ms=1500):
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
