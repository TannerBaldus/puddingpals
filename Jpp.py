from Gui import *

if __name__ == "__main__":
    app = wx.App()
    app.frame = GUI()
    app.frame.Show()
    app.MainLoop()