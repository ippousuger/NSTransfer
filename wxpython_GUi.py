# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from pubsub import pub

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1345,770 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 251, 248, 232 ) )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		#self.m_panel2.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)
		self.m_panel2.SetBackgroundColour( wx.Colour( 251, 248, 232 ) )

		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText17 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"图像风格迁移系统", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		self.m_staticText17.SetFont( wx.Font( 18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Senty小丸子" ) )
		self.m_staticText17.SetBackgroundColour( wx.Colour( 251, 248, 232 ) )

		gbSizer3.Add( self.m_staticText17, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_panel1 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.content_pic = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 400,400 ), 0 )
		self.content_pic.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		gbSizer2.Add( self.content_pic, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText9 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 33,60 ), 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 42, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "黑体" ) )

		gbSizer2.Add( self.m_staticText9, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.style_pic = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 400,400 ), 0 )
		self.style_pic.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		self.style_pic.SetMaxSize( wx.Size( 400,-1 ) )

		gbSizer2.Add( self.style_pic, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.noise_pic = wx.StaticBitmap( self.m_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 400,400 ), 0 )
		self.noise_pic.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		gbSizer2.Add( self.noise_pic, wx.GBPosition( 1, 6 ), wx.GBSpan( 1, 2 ), wx.ALL, 5 )

		self.m_staticText91 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"→", wx.DefaultPosition, wx.Size( 35,30 ), 0 )
		self.m_staticText91.Wrap( -1 )

		self.m_staticText91.SetFont( wx.Font( 24, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "黑体" ) )

		gbSizer2.Add( self.m_staticText91, wx.GBPosition( 1, 5 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel1.SetSizer( gbSizer2 )
		self.m_panel1.Layout()
		gbSizer2.Fit( self.m_panel1 )
		gbSizer3.Add( self.m_panel1, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 7 ), wx.EXPAND |wx.ALL, 5 )

		self.content_but = wx.Button( self.m_panel2, wx.ID_ANY, u"原始图像", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.content_but.SetFont( wx.Font( 11, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Senty小丸子" ) )

		gbSizer3.Add( self.content_but, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fuse_but = wx.Button( self.m_panel2, wx.ID_ANY, u"开始迁移", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.fuse_but.SetFont( wx.Font( 11, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Senty小丸子" ) )

		gbSizer3.Add( self.fuse_but, wx.GBPosition( 2, 6 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.style_but = wx.Button( self.m_panel2, wx.ID_ANY, u"融入风格", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.style_but.SetFont( wx.Font( 11, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Senty小丸子" ) )

		gbSizer3.Add( self.style_but, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText16 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"        图像宽度：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetFont( wx.Font( 11, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Senty小丸子" ) )

		gbSizer3.Add( self.m_staticText16, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )

		self.wid_text = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( -1,30 ), 0 )
		self.wid_text.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "黑体" ) )

		gbSizer3.Add( self.wid_text, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"J:/workspace/卒業デザイン/DeepLearningExamples-master/tf2-neural-style-transfer/output", wx.Point( -1,-1 ), wx.Size( 450,30 ), 0 )
		self.m_textCtrl4.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "黑体" ) )

		gbSizer3.Add( self.m_textCtrl4, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"当前轮次进度：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( 11, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Senty小丸子" ) )

		gbSizer3.Add( self.m_staticText21, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.train_SText = wx.StaticText( self.m_panel2, wx.ID_ANY, u"0%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.train_SText.Wrap( -1 )

		self.train_SText.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "黑体" ) )

		gbSizer3.Add( self.train_SText, wx.GBPosition( 5, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.time_SText = wx.StaticText( self.m_panel2, wx.ID_ANY, u"00:00:00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.time_SText.Wrap( -1 )

		self.time_SText.SetFont( wx.Font( 15, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "黑体" ) )

		gbSizer3.Add( self.time_SText, wx.GBPosition( 5, 6 ), wx.GBSpan( 2, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.epoch_SText = wx.StaticText( self.m_panel2, wx.ID_ANY, u"0%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.epoch_SText.Wrap( -1 )

		self.epoch_SText.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "黑体" ) )

		gbSizer3.Add( self.epoch_SText, wx.GBPosition( 6, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText22 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"总训练进度：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetFont( wx.Font( 11, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Senty小丸子" ) )

		gbSizer3.Add( self.m_staticText22, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.step_gauge = wx.Gauge( self.m_panel2, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 450,28 ), wx.GA_HORIZONTAL )
		self.step_gauge.SetValue( 0 )
		gbSizer3.Add( self.step_gauge, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )

		self.epo_gague = wx.Gauge( self.m_panel2, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 450,28 ), wx.GA_HORIZONTAL )
		self.epo_gague.SetValue( 0 )
		gbSizer3.Add( self.epo_gague, wx.GBPosition( 6, 2 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )

		self.get_path = wx.Button( self.m_panel2, wx.ID_ANY, u"选择路径", wx.DefaultPosition, wx.Size( -1,33 ), 0 )
		self.get_path.SetFont( wx.Font( 11, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Senty小丸子" ) )

		gbSizer3.Add( self.get_path, wx.GBPosition( 4, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"      图像高度：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		self.m_staticText18.SetFont( wx.Font( 11, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Senty小丸子" ) )

		gbSizer3.Add( self.m_staticText18, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.hei_text = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		self.hei_text.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "黑体" ) )

		gbSizer3.Add( self.hei_text, wx.GBPosition( 3, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"训练次数：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		self.m_staticText19.SetFont( wx.Font( 11, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Senty小丸子" ) )

		gbSizer3.Add( self.m_staticText19, wx.GBPosition( 3, 5 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.epo_text = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"500", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		self.epo_text.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "黑体" ) )

		gbSizer3.Add( self.epo_text, wx.GBPosition( 3, 6 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"输出路径：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		self.m_staticText20.SetFont( wx.Font( 11, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Senty小丸子" ) )

		gbSizer3.Add( self.m_staticText20, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )


		self.m_panel2.SetSizer( gbSizer3 )
		self.m_panel2.Layout()
		gbSizer3.Fit( self.m_panel2 )
		gbSizer1.Add( self.m_panel2, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( gbSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.content_but.Bind( wx.EVT_BUTTON, self.show_content )
		self.fuse_but.Bind( wx.EVT_BUTTON, self.ronghe )
		self.style_but.Bind( wx.EVT_BUTTON, self.show_style )

		# ***************自加*******************
		pub.subscribe(self.updateDisplay, "update")
		self.jadge_epoch_update_noisepic = 0
		# ***************自加*******************

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def show_content( self, event ):
		event.Skip()

	def ronghe( self, event ):
		event.Skip()

	def show_style( self, event ):
		event.Skip()

	# ***************自加*******************
	def updateDisplay(self, msg, epo):
		event.Skip()
	# ***************自加*******************
