import wxpython_GUi
import wx
import train
import settings,utils
from PIL import Image, ImageTk
import threading
import os
import time
from threading import Thread
from pubsub import pub


class TestThread(Thread):
    """线程类."""
    # ----------------------------------------------------------------------
    def __init__(self):
        """初试化."""
        Thread.__init__(self)
        self.start()  # start the thread
    # ----------------------------------------------------------------------
    def run(self):
        """重构线程包中的Run方法，包括执行动作."""
        # This is the code executing in the new thread.
        utils.width = settings.WIDTH
        utils.height = settings.HEIGHT
        train.train()


########################################################################
class gauageThread(Thread):
    def __init__(self):
        # 线程实例化时立即启动
        Thread.__init__(self)
        self.start()

    def run(self):
        # 线程执行的代码
        while (True):
            time.sleep(1)
            wx.CallAfter(pub.sendMessage, "update", msg=settings.had_trained, epo=settings.had_epoched)

########################################################################
class NSTapp(wxpython_GUi.MyFrame1):
    def __init__(self, parent):
        wxpython_GUi.MyFrame1.__init__(self, parent)

    def show_content( self, event ):
        filesFilter = "All files (*.*)|*.*"
        fileDialog = wx.FileDialog(None, message="Choose a directory:", wildcard=filesFilter,
                                   style=wx.FD_OPEN | wx.FD_MULTIPLE)
        dialogResult = fileDialog.ShowModal()
        if dialogResult != wx.ID_OK:
            pass
        settings.CONTENT_IMAGE_PATH = ''.join(fileDialog.GetPaths())    # 把对话框获得的列表转化为string
        img = Image.open(settings.CONTENT_IMAGE_PATH)  # 为获得size打开图片
        settings.WIDTH = img.size[0]
        settings.HEIGHT = img.size[1]
        self.wid_text.SetValue(str(img.size[0]))
        self.hei_text.SetValue(str(img.size[1]))
        if (img.size[0]>img.size[1]):
            image = wx.Image(settings.CONTENT_IMAGE_PATH, wx.BITMAP_TYPE_JPEG).Rescale(400,int(
                img.size[1] * 400 / img.size[0])).ConvertToBitmap()
        else:
            image = wx.Image(settings.CONTENT_IMAGE_PATH, wx.BITMAP_TYPE_JPEG).Rescale(int(
                img.size[0] * 400 / img.size[1]), 400).ConvertToBitmap()
        self.content_pic.SetBitmap(wx.BitmapFromImage(image))
        self.m_panel1.Refresh()

    def show_style( self, event ):
        filesFilter = "All files (*.*)|*.*"
        fileDialog = wx.FileDialog(None, message="Choose a directory:", wildcard=filesFilter,
                                   style=wx.FD_OPEN | wx.FD_MULTIPLE)
        dialogResult = fileDialog.ShowModal()
        if dialogResult != wx.ID_OK:
            pass
        settings.STYLE_IMAGE_PATH = ''.join(fileDialog.GetPaths())    # 把对话框获得的列表转化为string
        img = Image.open(settings.STYLE_IMAGE_PATH)  # 为获得size打开图片
        if (img.size[0]>img.size[1]):
            image1 = wx.Image(settings.STYLE_IMAGE_PATH, wx.BITMAP_TYPE_JPEG).Rescale(400,int(
                img.size[1] * 400 / img.size[0])).ConvertToBitmap()
        else:
            image1 = wx.Image(settings.STYLE_IMAGE_PATH, wx.BITMAP_TYPE_JPEG).Rescale(int(
                img.size[0] * 400 / img.size[1]), 400).ConvertToBitmap()
        self.style_pic.SetBitmap(wx.BitmapFromImage(image1))
        self.m_panel1.Refresh()


    def ronghe( self, event ):
        """
        Runs the thread
        """
        settings.WIDTH = int(self.wid_text.GetValue())
        settings.HEIGHT = int(self.hei_text.GetValue())
        settings.EPOCHS = int(int(self.epo_text.GetValue())/100)
        TestThread()
        gauageThread()
        self.fuse_but = event.GetEventObject()
        self.fuse_but.Disable()

    def updateDisplay(self, msg, epo):
        settings.timed += 1
        hour = int(settings.timed / 3600)
        minute = int(settings.timed / 60) - hour * 60
        second = settings.timed % 60
        t = msg%100
        s = int(msg/settings.EPOCHS)
        self.time_SText.SetLabel('%02d:%02d:%02d' % (hour, minute, second))
        self.step_gauge.SetValue(t)
        self.train_SText.SetLabel("%s%%" % t)
        self.epo_gague.SetValue(s)
        self.epoch_SText.SetLabel("%s%%" % s)
        if(epo>0 and (self.jadge_epoch_update_noisepic != epo) ):
            self.jadge_epoch_update_noisepic+=1
            noise_path = 'output/{}.jpg'.format(epo)
            img = Image.open(noise_path)  # 为获得size打开图片
            if (img.size[0] > img.size[1]):
                image = wx.Image(noise_path, wx.BITMAP_TYPE_JPEG).Rescale(400, int(
                    img.size[1] * 400 / img.size[0])).ConvertToBitmap()
            else:
                image = wx.Image(noise_path, wx.BITMAP_TYPE_JPEG).Rescale(int(
                    img.size[0] * 400 / img.size[1]), 400).ConvertToBitmap()
            self.noise_pic.SetBitmap(wx.BitmapFromImage(image))
            self.m_panel1.Refresh()

app = wx.App(False)
frame = NSTapp(None)
frame.Show()
app.MainLoop()
