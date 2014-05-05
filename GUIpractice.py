
#!/usr/bin/python
#Leticia Sanchez
#initialize wx
import wx


class myApp(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(myApp, self).__init__(*args, **kwargs) 
            
        self.InitUI()
        
    def InitUI(self):
        

        menubar = wx.MenuBar()

        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW, '&New')
        fileMenu.Append(wx.ID_OPEN, '&Open')
        fileMenu.Append(wx.ID_SAVE, '&Save')
        fileMenu.Append(wx.ID_STOP, '&Stop')
        fileMenu.Append(wx.ID_FORWARD, '&Forward')
        fileMenu.AppendSeparator()

        imp = wx.Menu()
        imp.Append(wx.ID_ANY, 'Import newsfeed list...')
        imp.Append(wx.ID_ANY, 'Import bookmarks...')
        imp.Append(wx.ID_ANY, 'Import mail...')
        imp.Append(wx.ID_ANY, 'Import newfeed list...')
        imp.Append(wx.ID_ANY, 'Import newlist ...')
       
        

        fileMenu.AppendMenu(wx.ID_ANY, 'I&mport', imp)

        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        fileMenu.AppendItem(qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

        menubar.Append(fileMenu, '&File')
        #menubar.Append(viewMenu, '&View')
        self.SetMenuBar(menubar)

        self.SetSize((550, 350))
        self.SetTitle('Final Project')
        self.Centre()
        self.Show(True)
        
    def OnQuit(self, e):
        self.Close()

def main():
    
    ex = wx.App()
    myApp(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()
