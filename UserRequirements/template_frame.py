# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.grid

###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sydney Airbnb Dataset Analysis Tool", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class IntroductionFrame
###########################################################################

class IntroductionFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sydney Airbnb Dataset Analysis Tool", pos = wx.DefaultPosition, size = wx.Size( 588,372 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		Uppermenu = wx.GridBagSizer( 0, 0 )
		Uppermenu.SetFlexibleDirection( wx.BOTH )
		Uppermenu.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.Listingbutton = wx.Button( self, wx.ID_ANY, u"Listings", wx.DefaultPosition, wx.DefaultSize, 0 )
		Uppermenu.Add( self.Listingbutton, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.Pricebutton = wx.Button( self, wx.ID_ANY, u"Price Chart", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Pricebutton.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )
		self.Pricebutton.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		Uppermenu.Add( self.Pricebutton, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.Reviewbutton = wx.Button( self, wx.ID_ANY, u"Reviews", wx.DefaultPosition, wx.DefaultSize, 0 )
		Uppermenu.Add( self.Reviewbutton, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.RoomUsebutton = wx.Button( self, wx.ID_ANY, u"Room Usage", wx.DefaultPosition, wx.DefaultSize, 0 )
		Uppermenu.Add( self.RoomUsebutton, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		Pagebuttons = wx.GridBagSizer( 0, 0 )
		Pagebuttons.SetFlexibleDirection( wx.BOTH )
		Pagebuttons.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

		self.Keywordtextbox = wx.TextCtrl( self, wx.ID_ANY, u"hjkkk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Keywordtextbox.SetMaxLength( 10 )
		self.Keywordtextbox.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.Keywordtextbox.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		Pagebuttons.Add( self.Keywordtextbox, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		suburbChoices = [ u"Bondi Beach", u"bondi beach", wx.EmptyString ]
		self.suburb = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, suburbChoices, 0 )
		self.suburb.SetSelection( 1 )
		Pagebuttons.Add( self.suburb, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.Searchbutton = wx.Button( self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		Pagebuttons.Add( self.Searchbutton, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_datePicker2 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		Pagebuttons.Add( self.m_datePicker2, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"From", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )

		Pagebuttons.Add( self.m_staticText1, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_datePicker3 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		Pagebuttons.Add( self.m_datePicker3, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"To", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetBackgroundColour( wx.Colour( 206, 153, 193 ) )

		Pagebuttons.Add( self.m_staticText2, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		Uppermenu.Add( Pagebuttons, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 3 ), wx.EXPAND, 5 )


		self.SetSizer( Uppermenu )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Listingbutton.Bind( wx.EVT_BUTTON, self.ListingOnButtonClick )
		self.Pricebutton.Bind( wx.EVT_BUTTON, self.PricebuttonOnButtonClick )
		self.Reviewbutton.Bind( wx.EVT_BUTTON, self.ReviewbuttonOnButtonClick )
		self.RoomUsebutton.Bind( wx.EVT_BUTTON, self.RoomUsebuttonOnButtonClick )
		self.Keywordtextbox.Bind( wx.EVT_TEXT, self.KeywordtextboxOnText )
		self.suburb.Bind( wx.EVT_CHOICE, self.SuburbchoiceOnChoice )
		self.Searchbutton.Bind( wx.EVT_BUTTON, self.SearchbuttonOnButtonClick )
		self.m_datePicker2.Bind( wx.adv.EVT_DATE_CHANGED, self.FROMDATE2OnDateChanged )
		self.m_datePicker3.Bind( wx.adv.EVT_DATE_CHANGED, self.TODATEPicker3OnDateChanged )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def ListingOnButtonClick( self, event ):
		event.Skip()

	def PricebuttonOnButtonClick( self, event ):
		event.Skip()

	def ReviewbuttonOnButtonClick( self, event ):
		event.Skip()

	def RoomUsebuttonOnButtonClick( self, event ):
		event.Skip()

	def KeywordtextboxOnText( self, event ):
		event.Skip()

	def SuburbchoiceOnChoice( self, event ):
		event.Skip()

	def SearchbuttonOnButtonClick( self, event ):
		event.Skip()

	def FROMDATE2OnDateChanged( self, event ):
		event.Skip()

	def TODATEPicker3OnDateChanged( self, event ):
		event.Skip()


###########################################################################
## Class Listing TAble
###########################################################################

class ListingTAble ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sydney Airbnb Dataset Analysis Tool", pos = wx.DefaultPosition, size = wx.Size( 617,504 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.UpperMenu = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.UpperMenu.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.Listingbutton = wx.Button( self.UpperMenu, wx.ID_ANY, u"Listings", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Listingbutton.SetLabelMarkup( u"Listings" )
		self.Listingbutton.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )

		wSizer1.Add( self.Listingbutton, 0, wx.ALL, 5 )

		self.PriceButton = wx.Button( self.UpperMenu, wx.ID_ANY, u"Price Chart", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.PriceButton, 0, wx.ALL, 5 )

		self.Reviewbutton = wx.Button( self.UpperMenu, wx.ID_ANY, u"Reviews", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.Reviewbutton, 0, wx.ALL, 5 )

		self.Roomusebutton = wx.Button( self.UpperMenu, wx.ID_ANY, u"Room Usage", wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.Roomusebutton, 0, wx.ALL, 5 )


		self.UpperMenu.SetSizer( wSizer1 )
		self.UpperMenu.Layout()
		wSizer1.Fit( self.UpperMenu )
		bSizer1.Add( self.UpperMenu, 1, wx.EXPAND |wx.ALL, 5 )

		self.Selectarea = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Selectarea.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		gbSizer6 = wx.GridBagSizer( 0, 0 )
		gbSizer6.SetFlexibleDirection( wx.BOTH )
		gbSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.Inputbox = wx.TextCtrl( self.Selectarea, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.Inputbox, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		SuburblistChoices = []
		self.Suburblist = wx.Choice( self.Selectarea, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, SuburblistChoices, 0 )
		self.Suburblist.SetSelection( 0 )
		gbSizer6.Add( self.Suburblist, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.Fromdate = wx.StaticText( self.Selectarea, wx.ID_ANY, u"From", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Fromdate.Wrap( -1 )

		gbSizer6.Add( self.Fromdate, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_datePicker3 = wx.adv.DatePickerCtrl( self.Selectarea, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gbSizer6.Add( self.m_datePicker3, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.TOdate = wx.StaticText( self.Selectarea, wx.ID_ANY, u"To", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TOdate.Wrap( -1 )

		gbSizer6.Add( self.TOdate, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_datePicker4 = wx.adv.DatePickerCtrl( self.Selectarea, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gbSizer6.Add( self.m_datePicker4, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.Searchbutton = wx.Button( self.Selectarea, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.Searchbutton, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.Selectarea.SetSizer( gbSizer6 )
		self.Selectarea.Layout()
		gbSizer6.Fit( self.Selectarea )
		bSizer1.Add( self.Selectarea, 1, wx.EXPAND |wx.ALL, 5 )

		self.Listingtablearea = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Listingtablearea.SetFont( wx.Font( 16, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Cambria" ) )
		self.Listingtablearea.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		gbSizer5 = wx.GridBagSizer( 0, 0 )
		gbSizer5.SetFlexibleDirection( wx.BOTH )
		gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.tabletext = wx.StaticText( self.Listingtablearea, wx.ID_ANY, u"Texttodisplay", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tabletext.Wrap( -1 )

		self.tabletext.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )

		gbSizer5.Add( self.tabletext, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.Listingtablearea.SetSizer( gbSizer5 )
		self.Listingtablearea.Layout()
		gbSizer5.Fit( self.Listingtablearea )
		bSizer1.Add( self.Listingtablearea, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer11 = wx.GridBagSizer( 0, 0 )
		gbSizer11.SetFlexibleDirection( wx.BOTH )
		gbSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_grid1 = wx.grid.Grid( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid1.CreateGrid( 5, 5 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		gbSizer11.Add( self.m_grid1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.m_panel10.SetSizer( gbSizer11 )
		self.m_panel10.Layout()
		gbSizer11.Fit( self.m_panel10 )
		bSizer1.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Listingbutton.Bind( wx.EVT_BUTTON, self.ListingbuttonOnButtonClick )
		self.PriceButton.Bind( wx.EVT_BUTTON, self.PriceChartOnButtonClick )
		self.Reviewbutton.Bind( wx.EVT_BUTTON, self.ReviewbuttonOnButtonClick )
		self.Roomusebutton.Bind( wx.EVT_BUTTON, self.RoomusebuttonOnButtonClick )
		self.Inputbox.Bind( wx.EVT_TEXT, self.InputboxOnText )
		self.Inputbox.Bind( wx.EVT_TEXT_ENTER, self.InputboxOnTextEnter )
		self.Inputbox.Bind( wx.EVT_TEXT_MAXLEN, self.InputboxOnTextMaxLen )
		self.Inputbox.Bind( wx.EVT_TEXT_URL, self.InputboxOnTextURL )
		self.Suburblist.Bind( wx.EVT_CHOICE, self.SuburblistOnChoice )
		self.m_datePicker3.Bind( wx.adv.EVT_DATE_CHANGED, self.m_datePicker3OnDateChanged )
		self.m_datePicker4.Bind( wx.adv.EVT_DATE_CHANGED, self.m_datePicker4OnDateChanged )
		self.Searchbutton.Bind( wx.EVT_BUTTON, self.SearchbuttonOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def ListingbuttonOnButtonClick( self, event ):
		event.Skip()

	def PriceChartOnButtonClick( self, event ):
		event.Skip()

	def ReviewbuttonOnButtonClick( self, event ):
		event.Skip()

	def RoomusebuttonOnButtonClick( self, event ):
		event.Skip()

	def InputboxOnText( self, event ):
		event.Skip()

	def InputboxOnTextEnter( self, event ):
		event.Skip()

	def InputboxOnTextMaxLen( self, event ):
		event.Skip()

	def InputboxOnTextURL( self, event ):
		event.Skip()

	def SuburblistOnChoice( self, event ):
		event.Skip()

	def m_datePicker3OnDateChanged( self, event ):
		event.Skip()

	def m_datePicker4OnDateChanged( self, event ):
		event.Skip()

	def SearchbuttonOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Reviewframe
###########################################################################

class Reviewframe ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sydney Airbnb Dataset Analysis Tool", pos = wx.DefaultPosition, size = wx.Size( 500,378 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.Uppermenu = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Uppermenu.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		gbSizer11 = wx.GridBagSizer( 0, 0 )
		gbSizer11.SetFlexibleDirection( wx.BOTH )
		gbSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.Listingbutton = wx.Button( self.Uppermenu, wx.ID_ANY, u"Listings", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer11.Add( self.Listingbutton, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.Price = wx.Button( self.Uppermenu, wx.ID_ANY, u"Price Chart", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer11.Add( self.Price, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.Reviewbutton = wx.Button( self.Uppermenu, wx.ID_ANY, u"Reviews", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer11.Add( self.Reviewbutton, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.Roomusagebutton = wx.Button( self.Uppermenu, wx.ID_ANY, u"Room Usage", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer11.Add( self.Roomusagebutton, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.Uppermenu.SetSizer( gbSizer11 )
		self.Uppermenu.Layout()
		gbSizer11.Fit( self.Uppermenu )
		bSizer3.Add( self.Uppermenu, 1, wx.EXPAND |wx.ALL, 5 )

		self.Selectarea = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Selectarea.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		gbSizer12 = wx.GridBagSizer( 0, 0 )
		gbSizer12.SetFlexibleDirection( wx.BOTH )
		gbSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.Inputbox = wx.TextCtrl( self.Selectarea, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer12.Add( self.Inputbox, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		SuburbChoices = []
		self.Suburb = wx.Choice( self.Selectarea, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, SuburbChoices, 0 )
		self.Suburb.SetSelection( 0 )
		gbSizer12.Add( self.Suburb, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.Fromdate = wx.StaticText( self.Selectarea, wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Fromdate.Wrap( -1 )

		gbSizer12.Add( self.Fromdate, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.FROMdate = wx.adv.DatePickerCtrl( self.Selectarea, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gbSizer12.Add( self.FROMdate, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.ToDAte = wx.StaticText( self.Selectarea, wx.ID_ANY, u"To:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ToDAte.Wrap( -1 )

		gbSizer12.Add( self.ToDAte, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.ToDAte = wx.adv.DatePickerCtrl( self.Selectarea, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gbSizer12.Add( self.ToDAte, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.Selectarea.SetSizer( gbSizer12 )
		self.Selectarea.Layout()
		gbSizer12.Fit( self.Selectarea )
		bSizer3.Add( self.Selectarea, 1, wx.EXPAND |wx.ALL, 5 )

		self.Reviewarea = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Reviewarea.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		gbSizer13 = wx.GridBagSizer( 0, 0 )
		gbSizer13.SetFlexibleDirection( wx.BOTH )
		gbSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.Roomname = wx.TextCtrl( self.Reviewarea, wx.ID_ANY, u"Room Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer13.Add( self.Roomname, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.RoomDescription = wx.TextCtrl( self.Reviewarea, wx.ID_ANY, u"Room Description", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer13.Add( self.RoomDescription, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.Reviewarea.SetSizer( gbSizer13 )
		self.Reviewarea.Layout()
		gbSizer13.Fit( self.Reviewarea )
		bSizer3.Add( self.Reviewarea, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Listingbutton.Bind( wx.EVT_BUTTON, self.ListingbuttonOnButtonClick )
		self.Price.Bind( wx.EVT_BUTTON, self.PriceOnButtonClick )
		self.Reviewbutton.Bind( wx.EVT_BUTTON, self.ReviewbuttonOnButtonClick )
		self.Roomusagebutton.Bind( wx.EVT_BUTTON, self.RoomusagebuttonOnButtonClick )
		self.Suburb.Bind( wx.EVT_CHOICE, self.SuburbOnChoice )
		self.FROMdate.Bind( wx.adv.EVT_DATE_CHANGED, self.FROMdateOnDateChanged )
		self.ToDAte.Bind( wx.adv.EVT_DATE_CHANGED, self.ToDAteOnDateChanged )
		self.RoomDescription.Bind( wx.EVT_TEXT, self.RoomDescriptionOnText )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def ListingbuttonOnButtonClick( self, event ):
		event.Skip()

	def PriceOnButtonClick( self, event ):
		event.Skip()

	def ReviewbuttonOnButtonClick( self, event ):
		event.Skip()

	def RoomusagebuttonOnButtonClick( self, event ):
		event.Skip()

	def SuburbOnChoice( self, event ):
		event.Skip()

	def FROMdateOnDateChanged( self, event ):
		event.Skip()

	def ToDAteOnDateChanged( self, event ):
		event.Skip()

	def RoomDescriptionOnText( self, event ):
		event.Skip()


###########################################################################
## Class Roomusagescreen
###########################################################################

class Roomusagescreen ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sydney Airbnb Dataset Analysis Tool", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.Uppermenu = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Uppermenu.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		gbSizer15 = wx.GridBagSizer( 0, 0 )
		gbSizer15.SetFlexibleDirection( wx.BOTH )
		gbSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.Listingbutton = wx.Button( self.Uppermenu, wx.ID_ANY, u"Listings", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer15.Add( self.Listingbutton, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.Pricebutton = wx.Button( self.Uppermenu, wx.ID_ANY, u"Price Chart", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer15.Add( self.Pricebutton, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.Reviewbutton = wx.Button( self.Uppermenu, wx.ID_ANY, u"Reviews", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer15.Add( self.Reviewbutton, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.Roomusagebutton = wx.Button( self.Uppermenu, wx.ID_ANY, u"Room Usage", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer15.Add( self.Roomusagebutton, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.Uppermenu.SetSizer( gbSizer15 )
		self.Uppermenu.Layout()
		gbSizer15.Fit( self.Uppermenu )
		bSizer5.Add( self.Uppermenu, 1, wx.EXPAND |wx.ALL, 5 )

		self.Selectarea = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Selectarea.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		gbSizer16 = wx.GridBagSizer( 0, 0 )
		gbSizer16.SetFlexibleDirection( wx.BOTH )
		gbSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.Inputbox = wx.TextCtrl( self.Selectarea, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer16.Add( self.Inputbox, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		SuburbChoices = []
		self.Suburb = wx.Choice( self.Selectarea, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, SuburbChoices, 0 )
		self.Suburb.SetSelection( 0 )
		gbSizer16.Add( self.Suburb, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.Fromdate = wx.StaticText( self.Selectarea, wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Fromdate.Wrap( -1 )

		gbSizer16.Add( self.Fromdate, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.FROMdate = wx.adv.DatePickerCtrl( self.Selectarea, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gbSizer16.Add( self.FROMdate, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.ToDate = wx.StaticText( self.Selectarea, wx.ID_ANY, u"To:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ToDate.Wrap( -1 )

		gbSizer16.Add( self.ToDate, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.Todate = wx.adv.DatePickerCtrl( self.Selectarea, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gbSizer16.Add( self.Todate, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.Selectarea.SetSizer( gbSizer16 )
		self.Selectarea.Layout()
		gbSizer16.Fit( self.Selectarea )
		bSizer5.Add( self.Selectarea, 1, wx.EXPAND |wx.ALL, 5 )

		self.Roomusearea = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Roomusearea.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		gbSizer17 = wx.GridBagSizer( 0, 0 )
		gbSizer17.SetFlexibleDirection( wx.BOTH )
		gbSizer17.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.Roomname = wx.TextCtrl( self.Roomusearea, wx.ID_ANY, u"Room Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer17.Add( self.Roomname, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.RoomUsagedescription = wx.TextCtrl( self.Roomusearea, wx.ID_ANY, u"Room Usage", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer17.Add( self.RoomUsagedescription, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.Roomusearea.SetSizer( gbSizer17 )
		self.Roomusearea.Layout()
		gbSizer17.Fit( self.Roomusearea )
		bSizer5.Add( self.Roomusearea, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Listingbutton.Bind( wx.EVT_BUTTON, self.ListingbuttonOnButtonClick )
		self.Pricebutton.Bind( wx.EVT_BUTTON, self.PricebuttonOnButtonClick )
		self.Reviewbutton.Bind( wx.EVT_BUTTON, self.ReviewbuttonOnButtonClick )
		self.Roomusagebutton.Bind( wx.EVT_BUTTON, self.RoomusagebuttonOnButtonClick )
		self.Inputbox.Bind( wx.EVT_TEXT, self.InputboxOnText )
		self.Inputbox.Bind( wx.EVT_TEXT_ENTER, self.InputboxOnTextEnter )
		self.Suburb.Bind( wx.EVT_CHOICE, self.SuburbOnChoice )
		self.FROMdate.Bind( wx.adv.EVT_DATE_CHANGED, self.FROMdateOnDateChanged )
		self.Todate.Bind( wx.adv.EVT_DATE_CHANGED, self.TodateOnDateChanged )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def ListingbuttonOnButtonClick( self, event ):
		event.Skip()

	def PricebuttonOnButtonClick( self, event ):
		event.Skip()

	def ReviewbuttonOnButtonClick( self, event ):
		event.Skip()

	def RoomusagebuttonOnButtonClick( self, event ):
		event.Skip()

	def InputboxOnText( self, event ):
		event.Skip()

	def InputboxOnTextEnter( self, event ):
		event.Skip()

	def SuburbOnChoice( self, event ):
		event.Skip()

	def FROMdateOnDateChanged( self, event ):
		event.Skip()

	def TodateOnDateChanged( self, event ):
		event.Skip()


