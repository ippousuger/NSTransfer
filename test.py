import wx


class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "My Frame", size=(400, 300),
                          style=wx.DEFAULT_FRAME_STYLE)
        self.panel = wx.Panel(self)
        self.panel.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)

    def OnEraseBack(self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap(r"C:\Users\王浩华\Desktop\毕业设计\图库\彩窗4.jpg")
        dc.DrawBitmap(bmp, 0, 0)


if __name__ == '__main__':
    app = wx.App()
    frame = Frame()
    frame.Show()
    app.MainLoop()