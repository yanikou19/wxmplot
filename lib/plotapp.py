import wx
from .plotframe import PlotFrame

class PlotApp(object):
    def __init__(self):
        self.app   = wx.App()
        self.frame = PlotFrame()

    def plot(self,x,y,**kw):
        return self.frame.plot(x,y,**kw)

    def oplot(self,x,y,**kw):
        return self.frame.oplot(x,y,**kw)

    def set_title(self,s):
        self.frame.set_title(s)

    def write_message(self,msg,**kw):
        return self.frame.write_message(msg, **kw)

    def run(self):
        self.frame.Show()
        self.frame.Raise()
        self.app.MainLoop()
