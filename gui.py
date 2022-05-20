
import wx
class VirtualAssistant(wx.Frame):
    '''
        A aplication that searches and returns search result from either wolframaplha or wikipedia of 
        any query you give to it.        
    '''
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw,size=wx.Size(450,150),style=wx.MINIMIZE_BOX |wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX|wx.CLIP_CHILDREN) #inheriting the parameters from the parent class and edit some

        panel=wx.Panel(self) #create a panel in the frame. Its just a place where you can write stuff. Like a board

        #put some text with a larger bold font on the board
        statictext=wx.StaticText(panel,label='Hello I am your virtual assistant for today. How can i help you?')
        font=statictext.GetFont()
        # font.PointSize +=10
        font=font.Bold()
        statictext.SetFont(font)

        #create a sizer to manage layout of child widgets
        sizer=wx.BoxSizer(wx.VERTICAL)
        sizer.Add(statictext,0,wx.ALL,5)                        #add the sizer to the board
        panel.SetSizer(sizer)
        self.txt=wx.TextCtrl(panel,style=wx.TE_PROCESS_ENTER,size=(400,30)) #this creates a text box
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER,self.OnEnter)
        sizer.Add(self.txt,0,wx.ALL,5)
        panel.SetSizer(sizer)
        self.Show()

        #add a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to Dami's Virtual asssitant!")


    def OnEnter(self,event):
        input=self.txt.GetValue().lower()
        print('it worked')



        








if __name__=='__main__':                                           #how you get your app to run
    app=wx.App(True)                                                #the True redirects the answer to a dialog box 
    frame=VirtualAssistant(None,title="Dami Sotomi's virtual assistant") #this is just to build the frame
    frame.Show()                                                  #this is to make the frame show
    app.MainLoop()                                                #to make the frame stay on your screen instead of disapperaing after showing          


    #the idea is that we are creating a frame and inheriting from wx inbuilt frame.
    #             