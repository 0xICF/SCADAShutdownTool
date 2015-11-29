# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"SCADA Shutdown Tool v1.0 Beta - Powered by 0xICF", pos = wx.DefaultPosition, size = wx.Size( 1020,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		self.m_menubar = wx.MenuBar( 0 )
		self.file = wx.Menu()
		self.exit = wx.MenuItem( self.file, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.AppendItem( self.exit )
		
		self.m_menubar.Append( self.file, u"File" ) 
		
		self.help = wx.Menu()
		self.about = wx.MenuItem( self.help, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.help.AppendItem( self.about )
		
		self.m_menubar.Append( self.help, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar )
		
		main_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		banner_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"images/banner.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		banner_bSizer.Add( self.m_bitmap1, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		main_bSizer.Add( banner_bSizer, 0, wx.ALL|wx.EXPAND, 5 )
		
		body_fgSizer = wx.FlexGridSizer( 0, 5, 0, 0 )
		body_fgSizer.SetFlexibleDirection( wx.BOTH )
		body_fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		target_sbSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Target" ), wx.VERTICAL )
		
		target_fgSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		target_fgSizer.SetFlexibleDirection( wx.BOTH )
		target_fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.ip_staticText = wx.StaticText( target_sbSizer.GetStaticBox(), wx.ID_ANY, u"IP Address", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ip_staticText.Wrap( -1 )
		target_fgSizer.Add( self.ip_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.ip = wx.TextCtrl( target_sbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		target_fgSizer.Add( self.ip, 0, wx.ALL, 5 )
		
		self.port_staticText = wx.StaticText( target_sbSizer.GetStaticBox(), wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.port_staticText.Wrap( -1 )
		target_fgSizer.Add( self.port_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.port = wx.TextCtrl( target_sbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		target_fgSizer.Add( self.port, 0, wx.ALL, 5 )
		
		self.unit_staticText = wx.StaticText( target_sbSizer.GetStaticBox(), wx.ID_ANY, u"Unit ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.unit_staticText.Wrap( -1 )
		target_fgSizer.Add( self.unit_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.unit_id = wx.TextCtrl( target_sbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		target_fgSizer.Add( self.unit_id, 0, wx.ALL, 5 )
		
		
		target_sbSizer.Add( target_fgSizer, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		body_fgSizer.Add( target_sbSizer, 0, wx.EXPAND|wx.ALL, 5 )
		
		register_sbSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Register types" ), wx.VERTICAL )
		
		register_fgSizer = wx.FlexGridSizer( 0, 3, 0, 0 )
		register_fgSizer.SetFlexibleDirection( wx.BOTH )
		register_fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.coil_outputs = wx.CheckBox( register_sbSizer.GetStaticBox(), wx.ID_ANY, u"Coil Outputs", wx.DefaultPosition, wx.DefaultSize, 0 )
		register_fgSizer.Add( self.coil_outputs, 0, wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( register_sbSizer.GetStaticBox(), wx.ID_ANY, u"Offset range: 0 -", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		register_fgSizer.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.co_offset = wx.TextCtrl( register_sbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		register_fgSizer.Add( self.co_offset, 0, wx.ALL, 5 )
		
		self.digital_inputs = wx.CheckBox( register_sbSizer.GetStaticBox(), wx.ID_ANY, u"Digital Inputs", wx.DefaultPosition, wx.DefaultSize, 0 )
		register_fgSizer.Add( self.digital_inputs, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( register_sbSizer.GetStaticBox(), wx.ID_ANY, u"Offset range: 0 -", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		register_fgSizer.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.di_offset = wx.TextCtrl( register_sbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		register_fgSizer.Add( self.di_offset, 0, wx.ALL, 5 )
		
		self.analogue_inputs = wx.CheckBox( register_sbSizer.GetStaticBox(), wx.ID_ANY, u"Analogue Inputs", wx.DefaultPosition, wx.DefaultSize, 0 )
		register_fgSizer.Add( self.analogue_inputs, 0, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( register_sbSizer.GetStaticBox(), wx.ID_ANY, u"Offset range: 0 -", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		register_fgSizer.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.ai_offset = wx.TextCtrl( register_sbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		register_fgSizer.Add( self.ai_offset, 0, wx.ALL, 5 )
		
		self.holding_registers = wx.CheckBox( register_sbSizer.GetStaticBox(), wx.ID_ANY, u"Holding Registers", wx.DefaultPosition, wx.DefaultSize, 0 )
		register_fgSizer.Add( self.holding_registers, 0, wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( register_sbSizer.GetStaticBox(), wx.ID_ANY, u"Offset range: 0 -", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		register_fgSizer.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.hr_offset = wx.TextCtrl( register_sbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		register_fgSizer.Add( self.hr_offset, 0, wx.ALL, 5 )
		
		self.extended_registers = wx.CheckBox( register_sbSizer.GetStaticBox(), wx.ID_ANY, u"Extended Registers", wx.DefaultPosition, wx.DefaultSize, 0 )
		register_fgSizer.Add( self.extended_registers, 0, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( register_sbSizer.GetStaticBox(), wx.ID_ANY, u"Offset range: 0 -", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		register_fgSizer.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self.er_offset = wx.TextCtrl( register_sbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		register_fgSizer.Add( self.er_offset, 0, wx.ALL, 5 )
		
		
		register_sbSizer.Add( register_fgSizer, 1, wx.EXPAND, 5 )
		
		
		body_fgSizer.Add( register_sbSizer, 0, wx.EXPAND|wx.ALL, 5 )
		
		option_sbSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Options" ), wx.VERTICAL )
		
		self.safe_mode = wx.RadioButton( option_sbSizer.GetStaticBox(), wx.ID_ANY, u"Safe-mode (read only non-zero values)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.safe_mode.SetValue( True ) 
		option_sbSizer.Add( self.safe_mode, 0, wx.ALL, 5 )
		
		self.real_mode = wx.RadioButton( option_sbSizer.GetStaticBox(), wx.ID_ANY, u"Real-mode (rewrite only non-zero values)", wx.DefaultPosition, wx.DefaultSize, 0 )
		option_sbSizer.Add( self.real_mode, 0, wx.ALL, 5 )
		
		self.aggressive_mode = wx.RadioButton( option_sbSizer.GetStaticBox(), wx.ID_ANY, u"Aggresive mode (rewrite all registers)", wx.DefaultPosition, wx.DefaultSize, 0 )
		option_sbSizer.Add( self.aggressive_mode, 0, wx.ALL, 5 )
		
		shutdown_value_fgSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		shutdown_value_fgSizer.SetFlexibleDirection( wx.BOTH )
		shutdown_value_fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.sd_val_staticText = wx.StaticText( option_sbSizer.GetStaticBox(), wx.ID_ANY, u"Shutdown value:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sd_val_staticText.Wrap( -1 )
		shutdown_value_fgSizer.Add( self.sd_val_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.sd_val = wx.TextCtrl( option_sbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		shutdown_value_fgSizer.Add( self.sd_val, 0, wx.ALL, 5 )
		
		
		option_sbSizer.Add( shutdown_value_fgSizer, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		body_fgSizer.Add( option_sbSizer, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.shutdown = wx.Button( self, wx.ID_ANY, u"Shutdown", wx.Point( 100,-1 ), wx.Size( 100,-1 ), 0 )
		body_fgSizer.Add( self.shutdown, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		main_bSizer.Add( body_fgSizer, 0, wx.EXPAND|wx.ALL, 5 )
		
		console_sbSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Console" ), wx.VERTICAL )
		
		self.console = wx.richtext.RichTextCtrl( console_sbSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		console_sbSizer.Add( self.console, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		main_bSizer.Add( console_sbSizer, 1, wx.EXPAND|wx.ALL, 5 )
		
		
		self.SetSizer( main_bSizer )
		self.Layout()
		self.sb = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.exitFunc, id = self.exit.GetId() )
		self.Bind( wx.EVT_MENU, self.aboutFunc, id = self.about.GetId() )
		self.shutdown.Bind( wx.EVT_BUTTON, self.start )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def exitFunc( self, event ):
		event.Skip()
	
	def aboutFunc( self, event ):
		event.Skip()
	
	def start( self, event ):
		event.Skip()
	

