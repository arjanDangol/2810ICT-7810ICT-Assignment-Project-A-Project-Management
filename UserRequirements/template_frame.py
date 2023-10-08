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
## Class IntroductionFrame
###########################################################################

class IntroductionFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Sydney Airbnb Dataset Analysis Tool",
                          pos=wx.DefaultPosition, size=wx.Size(534, 231),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.Uppermenu = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.Uppermenu.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        gbSizer16 = wx.GridBagSizer(0, 0)
        gbSizer16.SetFlexibleDirection(wx.BOTH)
        gbSizer16.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.ListingButton = wx.Button(self.Uppermenu, wx.ID_ANY, u"Listings", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer16.Add(self.ListingButton, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.PriceButton = wx.Button(self.Uppermenu, wx.ID_ANY, u"PriceChart", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer16.Add(self.PriceButton, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.ReviewButton = wx.Button(self.Uppermenu, wx.ID_ANY, u"Reviews", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer16.Add(self.ReviewButton, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Roomusebutton = wx.Button(self.Uppermenu, wx.ID_ANY, u"RoomUsage", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer16.Add(self.Roomusebutton, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.UserSpecificButton = wx.Button(self.Uppermenu, wx.ID_ANY, u"UserSpecific", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        gbSizer16.Add(self.UserSpecificButton, wx.GBPosition(0, 4), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Uppermenu.SetSizer(gbSizer16)
        self.Uppermenu.Layout()
        gbSizer16.Fit(self.Uppermenu)
        bSizer5.Add(self.Uppermenu, 1, wx.EXPAND | wx.ALL, 5)

        self.Selectarea = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.Selectarea.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        gbSizer17 = wx.GridBagSizer(0, 0)
        gbSizer17.SetFlexibleDirection(wx.BOTH)
        gbSizer17.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Suburb = wx.StaticText(self.Selectarea, wx.ID_ANY, u"Suburb:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Suburb.Wrap(-1)

        gbSizer17.Add(self.Suburb, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Fromdate = wx.StaticText(self.Selectarea, wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Fromdate.Wrap(-1)

        gbSizer17.Add(self.Fromdate, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Todate = wx.StaticText(self.Selectarea, wx.ID_ANY, u"To:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Todate.Wrap(-1)

        gbSizer17.Add(self.Todate, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        SuburblistChoices = [u"Pyrmont", u"Balgowlah", u"Darlinghurst", u"Balmain", u"Bellevue Hill", u"North Sydney",
                             u"North Bondi", u"Darlinghurst", u"Bondi Beach", u"North Bondi", u"Mosman",
                             u"Bondi Junction", u"Alexandria", u"Avalon", u"Sydney", u"Lane Cove West", u"Paddington",
                             wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString,
                             wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString,
                             wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString,
                             wx.EmptyString, wx.EmptyString]
        self.Suburblist = wx.Choice(self.Selectarea, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, SuburblistChoices,
                                    0)
        self.Suburblist.SetSelection(8)
        gbSizer17.Add(self.Suburblist, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Fromdate = wx.adv.DatePickerCtrl(self.Selectarea, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                              wx.DefaultSize, wx.adv.DP_DEFAULT)
        gbSizer17.Add(self.Fromdate, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Todate = wx.adv.DatePickerCtrl(self.Selectarea, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                            wx.DefaultSize, wx.adv.DP_DEFAULT)
        gbSizer17.Add(self.Todate, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Searchbutton = wx.Button(self.Selectarea, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer17.Add(self.Searchbutton, wx.GBPosition(4, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Selectarea.SetSizer(gbSizer17)
        self.Selectarea.Layout()
        gbSizer17.Fit(self.Selectarea)
        bSizer5.Add(self.Selectarea, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer5)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.ListingButton.Bind(wx.EVT_BUTTON, self.ListingButtonOnButtonClick)
        self.PriceButton.Bind(wx.EVT_BUTTON, self.PriceButtonOnButtonClick)
        self.ReviewButton.Bind(wx.EVT_BUTTON, self.ReviewButtonOnButtonClick)
        self.Roomusebutton.Bind(wx.EVT_BUTTON, self.RoomusebuttonOnButtonClick)
        self.UserSpecificButton.Bind(wx.EVT_BUTTON, self.UserSpecificButtonOnButtonClick)
        self.Suburblist.Bind(wx.EVT_CHOICE, self.SuburblistOnChoice)
        self.Fromdate.Bind(wx.adv.EVT_DATE_CHANGED, self.FromdateOnDateChanged)
        self.Todate.Bind(wx.adv.EVT_DATE_CHANGED, self.TodateOnDateChanged)
        self.Searchbutton.Bind(wx.EVT_BUTTON, self.SearchbuttonOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def ListingButtonOnButtonClick(self, event):
        event.Skip()

    def PriceButtonOnButtonClick(self, event):
        event.Skip()

    def ReviewButtonOnButtonClick(self, event):
        event.Skip()

    def RoomusebuttonOnButtonClick(self, event):
        event.Skip()

    def UserSpecificButtonOnButtonClick(self, event):
        event.Skip()

    def SuburblistOnChoice(self, event):
        event.Skip()

    def FromdateOnDateChanged(self, event):
        event.Skip()

    def TodateOnDateChanged(self, event):
        event.Skip()

    def SearchbuttonOnButtonClick(self, event):
        event.Skip()


###########################################################################
## Class Listing TAble
###########################################################################

class ListingTAble(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Sydney Airbnb Dataset Analysis Tool",
                          pos=wx.DefaultPosition, size=wx.Size(617, 355),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.UpperMenu = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.UpperMenu.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        wSizer1 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.Listingbutton = wx.Button(self.UpperMenu, wx.ID_ANY, u"Listings", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Listingbutton.SetLabelMarkup(u"Listings")
        self.Listingbutton.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTIONTEXT))

        wSizer1.Add(self.Listingbutton, 0, wx.ALL, 5)

        self.PriceButton = wx.Button(self.UpperMenu, wx.ID_ANY, u"PriceChart", wx.DefaultPosition, wx.DefaultSize, 0)
        wSizer1.Add(self.PriceButton, 0, wx.ALL, 5)

        self.Reviewbutton = wx.Button(self.UpperMenu, wx.ID_ANY, u"Reviews", wx.DefaultPosition, wx.DefaultSize, 0)
        wSizer1.Add(self.Reviewbutton, 0, wx.ALL, 5)

        self.Roomusebutton = wx.Button(self.UpperMenu, wx.ID_ANY, u"RoomUsage", wx.DefaultPosition, wx.DefaultSize, 0)
        wSizer1.Add(self.Roomusebutton, 0, wx.ALL, 5)

        self.UserSpecificButton = wx.Button(self.UpperMenu, wx.ID_ANY, u"UserSpecific", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        wSizer1.Add(self.UserSpecificButton, 0, wx.ALL, 5)

        self.UpperMenu.SetSizer(wSizer1)
        self.UpperMenu.Layout()
        wSizer1.Fit(self.UpperMenu)
        bSizer1.Add(self.UpperMenu, 1, wx.EXPAND | wx.ALL, 5)

        self.Selectarea = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.Selectarea.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        gbSizer6 = wx.GridBagSizer(0, 0)
        gbSizer6.SetFlexibleDirection(wx.BOTH)
        gbSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        SuburblistChoices = [u"Pyrmont", u"Balgowlah", u"Darlinghurst", u"Balmain", u"Bellevue Hill", u"North Sydney",
                             u"North Bondi", u"Darlinghurst", u"Bondi Beach", u"North Bondi", u"Mosman",
                             u"Bondi Junction", u"Alexandria", u"Avalon", u"Sydney", u"Lane Cove West", u"Paddington",
                             wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString,
                             wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString,
                             wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString,
                             wx.EmptyString, wx.EmptyString]
        self.Suburblist = wx.Choice(self.Selectarea, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, SuburblistChoices,
                                    0)
        self.Suburblist.SetSelection(8)
        gbSizer6.Add(self.Suburblist, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Suburb = wx.StaticText(self.Selectarea, wx.ID_ANY, u"Suburb:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Suburb.Wrap(-1)

        gbSizer6.Add(self.Suburb, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Fromdate = wx.StaticText(self.Selectarea, wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Fromdate.Wrap(-1)

        gbSizer6.Add(self.Fromdate, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Fromdate = wx.adv.DatePickerCtrl(self.Selectarea, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                              wx.DefaultSize, wx.adv.DP_DEFAULT)
        gbSizer6.Add(self.Fromdate, wx.GBPosition(1, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.TOdate = wx.StaticText(self.Selectarea, wx.ID_ANY, u"To:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.TOdate.Wrap(-1)

        gbSizer6.Add(self.TOdate, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Todate = wx.adv.DatePickerCtrl(self.Selectarea, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                            wx.DefaultSize, wx.adv.DP_DEFAULT)
        gbSizer6.Add(self.Todate, wx.GBPosition(2, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Searchbutton = wx.Button(self.Selectarea, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer6.Add(self.Searchbutton, wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Selectarea.SetSizer(gbSizer6)
        self.Selectarea.Layout()
        gbSizer6.Fit(self.Selectarea)
        bSizer1.Add(self.Selectarea, 1, wx.EXPAND | wx.ALL, 5)

        self.Listingtable = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                              wx.HSCROLL | wx.VSCROLL)
        self.Listingtable.SetScrollbars(1, 1, 1, 1)  # Enable scrollbars
        self.Listingtable.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        gbSizer11 = wx.GridBagSizer(0, 0)
        gbSizer11.SetFlexibleDirection(wx.BOTH)
        gbSizer11.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Listtable = wx.grid.Grid(self.Listingtable, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.Listtable.CreateGrid(5, 5)
        self.Listtable.EnableEditing(True)
        self.Listtable.EnableGridLines(True)
        self.Listtable.EnableDragGridSize(False)
        self.Listtable.SetMargins(0, 0)

        # Columns
        self.Listtable.EnableDragColMove(False)
        self.Listtable.EnableDragColSize(True)
        self.Listtable.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.Listtable.EnableDragRowSize(True)
        self.Listtable.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.Listtable.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        gbSizer11.Add(self.Listtable, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Listingtable.SetSizer(gbSizer11)
        self.Listingtable.Layout()
        gbSizer11.Fit(self.Listingtable)
        bSizer1.Add(self.Listingtable, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Listingbutton.Bind(wx.EVT_BUTTON, self.ListingbuttonOnButtonClick)
        self.PriceButton.Bind(wx.EVT_BUTTON, self.PriceButtonOnButtonClick)
        self.Reviewbutton.Bind(wx.EVT_BUTTON, self.ReviewbuttonOnButtonClick)
        self.Roomusebutton.Bind(wx.EVT_BUTTON, self.RoomusebuttonOnButtonClick)
        self.UserSpecificButton.Bind(wx.EVT_BUTTON, self.UserSpecificButtonOnButtonClick)
        self.Suburblist.Bind(wx.EVT_CHOICE, self.SuburblistOnChoice)
        self.Fromdate.Bind(wx.adv.EVT_DATE_CHANGED, self.FromdateOnDateChanged)
        self.Todate.Bind(wx.adv.EVT_DATE_CHANGED, self.TodateOnDateChanged)
        self.Searchbutton.Bind(wx.EVT_BUTTON, self.SearchbuttonOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def ListingbuttonOnButtonClick(self, event):
        event.Skip()

    def PriceButtonOnButtonClick(self, event):
        event.Skip()

    def ReviewbuttonOnButtonClick(self, event):
        event.Skip()

    def RoomusebuttonOnButtonClick(self, event):
        event.Skip()

    def UserSpecificButtonOnButtonClick(self, event):
        event.Skip()

    def SuburblistOnChoice(self, event):
        event.Skip()

    def FromdateOnDateChanged(self, event):
        event.Skip()

    def TodateOnDateChanged(self, event):
        event.Skip()

    def SearchbuttonOnButtonClick(self, event):
        event.Skip()


###########################################################################
## Class Reviewframe
###########################################################################

class Reviewframe(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Sydney Airbnb Dataset Analysis Tool",
                          pos=wx.DefaultPosition, size=wx.Size(500, 284),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.Uppermenu = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.Uppermenu.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        gbSizer11 = wx.GridBagSizer(0, 0)
        gbSizer11.SetFlexibleDirection(wx.BOTH)
        gbSizer11.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Listingbutton = wx.Button(self.Uppermenu, wx.ID_ANY, u"Listings", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer11.Add(self.Listingbutton, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Price = wx.Button(self.Uppermenu, wx.ID_ANY, u"PriceChart", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer11.Add(self.Price, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Reviewbutton = wx.Button(self.Uppermenu, wx.ID_ANY, u"Reviews", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer11.Add(self.Reviewbutton, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Roomusagebutton = wx.Button(self.Uppermenu, wx.ID_ANY, u"RoomUsage", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer11.Add(self.Roomusagebutton, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.UserSpecificbutton = wx.Button(self.Uppermenu, wx.ID_ANY, u"UserSpecifc", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        gbSizer11.Add(self.UserSpecificbutton, wx.GBPosition(0, 4), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Uppermenu.SetSizer(gbSizer11)
        self.Uppermenu.Layout()
        gbSizer11.Fit(self.Uppermenu)
        bSizer3.Add(self.Uppermenu, 1, wx.EXPAND | wx.ALL, 5)

        self.Selectarea = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.Selectarea.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        self.ReviewTableArea = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                              wx.HSCROLL | wx.VSCROLL)
        self.ReviewTableArea.SetScrollbars(1, 1, 1, 1)  # Enable scrollbars
        self.ReviewTableArea.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        gbSizer12 = wx.GridBagSizer(0, 0)
        gbSizer12.SetFlexibleDirection(wx.BOTH)
        gbSizer12.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # self.Suburb = wx.StaticText(self.Selectarea, wx.ID_ANY, u"Suburb:", wx.DefaultPosition, wx.DefaultSize, 0)
        # self.Suburb.Wrap(-1)
        #
        # gbSizer12.Add(self.Suburb, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)
        #
        # SuburblistChoices = [u"Pyrmont", u"Balgowlah", u"Darlinghurst", u"Balmain", u"Bellevue Hill", u"North Sydney",
        #                      u"North Bondi", u"Darlinghurst", u"Bondi Beach", u"North Bondi", u"Mosman",
        #                      u"Bondi Junction", u"Alexandria", u"Avalon", u"Sydney", u"Lane Cove West", u"Paddington",
        #                      wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString,
        #                      wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString,
        #                      wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString,
        #                      wx.EmptyString, wx.EmptyString]
        # self.Suburblist = wx.Choice(self.Selectarea, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, SuburblistChoices,
        #                             0)
        # self.Suburblist.SetSelection(11)
        # gbSizer12.Add(self.Suburblist, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Fromdate = wx.StaticText(self.Selectarea, wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Fromdate.Wrap(-1)

        gbSizer12.Add(self.Fromdate, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.FromDate = wx.adv.DatePickerCtrl(self.Selectarea, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                              wx.DefaultSize, wx.adv.DP_DEFAULT)
        gbSizer12.Add(self.FromDate, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Todate = wx.StaticText(self.Selectarea, wx.ID_ANY, u"To:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Todate.Wrap(-1)

        gbSizer12.Add(self.Todate, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.ToDate = wx.adv.DatePickerCtrl(self.Selectarea, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                            wx.DefaultSize, wx.adv.DP_DEFAULT)
        gbSizer12.Add(self.ToDate, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.SearcButton = wx.Button(self.Selectarea, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer12.Add(self.SearcButton, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Selectarea.SetSizer(gbSizer12)
        self.Selectarea.Layout()
        gbSizer12.Fit(self.Selectarea)
        bSizer3.Add(self.Selectarea, 1, wx.EXPAND | wx.ALL, 5)

        # self.Reviewarea = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        # self.Reviewarea.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        gbSizer13 = wx.GridBagSizer(0, 0)
        gbSizer13.SetFlexibleDirection(wx.BOTH)
        gbSizer13.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.ReviewTable = wx.grid.Grid(self.ReviewTableArea, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.ReviewTable.CreateGrid(5, 5)
        self.ReviewTable.EnableEditing(True)
        self.ReviewTable.EnableGridLines(True)
        self.ReviewTable.EnableDragGridSize(False)
        self.ReviewTable.SetMargins(0, 0)

        # Columns
        self.ReviewTable.EnableDragColMove(False)
        self.ReviewTable.EnableDragColSize(True)
        self.ReviewTable.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.ReviewTable.EnableDragRowSize(True)
        self.ReviewTable.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.ReviewTable.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        gbSizer13.Add(self.ReviewTable, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        # self.Roomname = wx.StaticText(self.Reviewarea, wx.ID_ANY, u"RoomName", wx.DefaultPosition, wx.DefaultSize, 0)
        # self.Roomname.Wrap(-1)
        #
        # self.Roomname.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))
        #
        # gbSizer13.Add(self.Roomname, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)
        #
        # self.RoomDescription = wx.StaticText(self.Reviewarea, wx.ID_ANY, u"RoomDescription", wx.DefaultPosition,
        #                                      wx.DefaultSize, 0)
        # self.RoomDescription.Wrap(-1)
        #
        # self.RoomDescription.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))
        #
        # gbSizer13.Add(self.RoomDescription, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.ReviewTableArea.SetSizer(gbSizer13)
        self.ReviewTableArea.Layout()
        gbSizer13.Fit(self.ReviewTableArea)
        bSizer3.Add(self.ReviewTableArea, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Listingbutton.Bind(wx.EVT_BUTTON, self.ListingbuttonOnButtonClick)
        self.Price.Bind(wx.EVT_BUTTON, self.PriceOnButtonClick)
        self.Reviewbutton.Bind(wx.EVT_BUTTON, self.ReviewbuttonOnButtonClick)
        self.Roomusagebutton.Bind(wx.EVT_BUTTON, self.RoomusagebuttonOnButtonClick)
        self.UserSpecificbutton.Bind(wx.EVT_BUTTON, self.UserSpecificbuttonOnButtonClick)
        # self.Suburblist.Bind(wx.EVT_CHOICE, self.SuburblistOnChoice)
        self.FromDate.Bind(wx.adv.EVT_DATE_CHANGED, self.FromDateOnDateChanged)
        self.ToDate.Bind(wx.adv.EVT_DATE_CHANGED, self.ToDateOnDateChanged)
        self.SearcButton.Bind(wx.EVT_BUTTON, self.SearcButtonOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def ListingbuttonOnButtonClick(self, event):
        event.Skip()

    def PriceOnButtonClick(self, event):
        event.Skip()

    def ReviewbuttonOnButtonClick(self, event):
        event.Skip()

    def RoomusagebuttonOnButtonClick(self, event):
        event.Skip()

    def UserSpecificbuttonOnButtonClick(self, event):
        event.Skip()

    # def SuburblistOnChoice(self, event):
    #     event.Skip()

    def FromDateOnDateChanged(self, event):
        event.Skip()

    def ToDateOnDateChanged(self, event):
        event.Skip()

    def SearcButtonOnButtonClick(self, event):
        event.Skip()


###########################################################################
## Class Roomusagescreen
###########################################################################

class Roomusagescreen(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Sydney Airbnb Dataset Analysis Tool",
                          pos=wx.DefaultPosition, size=wx.Size(500, 289),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.Uppermenu = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.Uppermenu.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        gbSizer15 = wx.GridBagSizer(0, 0)
        gbSizer15.SetFlexibleDirection(wx.BOTH)
        gbSizer15.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Listingbutton = wx.Button(self.Uppermenu, wx.ID_ANY, u"Listings", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer15.Add(self.Listingbutton, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Pricebutton = wx.Button(self.Uppermenu, wx.ID_ANY, u"PriceChart", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer15.Add(self.Pricebutton, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Reviewbutton = wx.Button(self.Uppermenu, wx.ID_ANY, u"Reviews", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer15.Add(self.Reviewbutton, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Roomusagebutton = wx.Button(self.Uppermenu, wx.ID_ANY, u"RoomUsage", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer15.Add(self.Roomusagebutton, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.UserSpecificButton = wx.Button(self.Uppermenu, wx.ID_ANY, u"UserSpecific", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        gbSizer15.Add(self.UserSpecificButton, wx.GBPosition(0, 4), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Uppermenu.SetSizer(gbSizer15)
        self.Uppermenu.Layout()
        gbSizer15.Fit(self.Uppermenu)
        bSizer5.Add(self.Uppermenu, 1, wx.EXPAND | wx.ALL, 5)

        self.Selectarea = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.Selectarea.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        gbSizer16 = wx.GridBagSizer(0, 0)
        gbSizer16.SetFlexibleDirection(wx.BOTH)
        gbSizer16.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # self.Suburb = wx.StaticText(self.Selectarea, wx.ID_ANY, u"Suburb:", wx.DefaultPosition, wx.DefaultSize, 0)
        # self.Suburb.Wrap(-1)
        #
        # gbSizer16.Add(self.Suburb, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        # SuburblistChoices = [u"Pyrmont", u"Balgowlah", u"Darlinghurst", u"Balmain", u"Bellevue Hill", u"North Sydney",
        #                      u"North Bondi", u"Darlinghurst", u"Bondi Beach", u"North Bondi", u"Mosman",
        #                      u"Bondi Junction", u"Alexandria", u"Avalon", u"Sydney", u"Lane Cove West", u"Paddington",
        #                      wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString,
        #                      wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString,
        #                      wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString,
        #                      wx.EmptyString, wx.EmptyString]
        # self.Suburblist = wx.Choice(self.Selectarea, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, SuburblistChoices,
        #                             0)
        # self.Suburblist.SetSelection(14)
        # gbSizer16.Add(self.Suburblist, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Fromdate = wx.StaticText(self.Selectarea, wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Fromdate.Wrap(-1)

        gbSizer16.Add(self.Fromdate, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.FromDate = wx.adv.DatePickerCtrl(self.Selectarea, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                              wx.DefaultSize, wx.adv.DP_DEFAULT)
        gbSizer16.Add(self.FromDate, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.ToDate = wx.StaticText(self.Selectarea, wx.ID_ANY, u"To:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ToDate.Wrap(-1)

        gbSizer16.Add(self.ToDate, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.ToDate = wx.adv.DatePickerCtrl(self.Selectarea, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                            wx.DefaultSize, wx.adv.DP_DEFAULT)
        gbSizer16.Add(self.ToDate, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.SearchButton = wx.Button(self.Selectarea, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer16.Add(self.SearchButton, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Selectarea.SetSizer(gbSizer16)
        self.Selectarea.Layout()
        gbSizer16.Fit(self.Selectarea)
        bSizer5.Add(self.Selectarea, 1, wx.EXPAND | wx.ALL, 5)

        self.Roomusearea = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.Roomusearea.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        gbSizer17 = wx.GridBagSizer(0, 0)
        gbSizer17.SetFlexibleDirection(wx.BOTH)
        gbSizer17.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.RoomName = wx.StaticText(self.Roomusearea, wx.ID_ANY, u"RoomName", wx.DefaultPosition, wx.DefaultSize, 0)
        self.RoomName.Wrap(-1)

        self.RoomName.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        gbSizer17.Add(self.RoomName, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.RoomUsage = wx.StaticText(self.Roomusearea, wx.ID_ANY, u"RoomUsage", wx.DefaultPosition, wx.DefaultSize, 0)
        self.RoomUsage.Wrap(-1)

        self.RoomUsage.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_SCROLLBAR))

        gbSizer17.Add(self.RoomUsage, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Roomusearea.SetSizer(gbSizer17)
        self.Roomusearea.Layout()
        gbSizer17.Fit(self.Roomusearea)
        bSizer5.Add(self.Roomusearea, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer5)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Listingbutton.Bind(wx.EVT_BUTTON, self.ListingbuttonOnButtonClick)
        self.Pricebutton.Bind(wx.EVT_BUTTON, self.PricebuttonOnButtonClick)
        self.Reviewbutton.Bind(wx.EVT_BUTTON, self.ReviewbuttonOnButtonClick)
        self.Roomusagebutton.Bind(wx.EVT_BUTTON, self.RoomusagebuttonOnButtonClick)
        self.UserSpecificButton.Bind(wx.EVT_BUTTON, self.UserSpecificButtonOnButtonClick)
        # self.Suburblist.Bind(wx.EVT_CHOICE, self.SuburblistOnChoice)
        self.FromDate.Bind(wx.adv.EVT_DATE_CHANGED, self.FromDateOnDateChanged)
        self.ToDate.Bind(wx.adv.EVT_DATE_CHANGED, self.ToDateOnDateChanged)
        self.SearchButton.Bind(wx.EVT_BUTTON, self.SearchButtonOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def ListingbuttonOnButtonClick(self, event):
        event.Skip()

    def PricebuttonOnButtonClick(self, event):
        event.Skip()

    def ReviewbuttonOnButtonClick(self, event):
        event.Skip()

    def RoomusagebuttonOnButtonClick(self, event):
        event.Skip()

    def UserSpecificButtonOnButtonClick(self, event):
        event.Skip()

    # def SuburblistOnChoice(self, event):
    #     event.Skip()

    def FromDateOnDateChanged(self, event):
        event.Skip()

    def ToDateOnDateChanged(self, event):
        event.Skip()

    def SearchButtonOnButtonClick(self, event):
        event.Skip()


###########################################################################
## Class UserSpecificFrame
###########################################################################

class UserSpecificFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Sydney Airbnb Dataset Analysis Tool",
                          pos=wx.DefaultPosition, size=wx.Size(500, 336),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.Uppermenu = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.Uppermenu.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        gbSizer13 = wx.GridBagSizer(0, 0)
        gbSizer13.SetFlexibleDirection(wx.BOTH)
        gbSizer13.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Listingbutton = wx.Button(self.Uppermenu, wx.ID_ANY, u"Listings", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer13.Add(self.Listingbutton, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Pricebutton = wx.Button(self.Uppermenu, wx.ID_ANY, u"PriceChart", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer13.Add(self.Pricebutton, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Reviewbutton = wx.Button(self.Uppermenu, wx.ID_ANY, u"Reviews", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer13.Add(self.Reviewbutton, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Roomusagebutton = wx.Button(self.Uppermenu, wx.ID_ANY, u"RoomUsage", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer13.Add(self.Roomusagebutton, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.UserSpecificbutton = wx.Button(self.Uppermenu, wx.ID_ANY, u"UserSpecific", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        gbSizer13.Add(self.UserSpecificbutton, wx.GBPosition(0, 4), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Uppermenu.SetSizer(gbSizer13)
        self.Uppermenu.Layout()
        gbSizer13.Fit(self.Uppermenu)
        bSizer4.Add(self.Uppermenu, 1, wx.EXPAND | wx.ALL, 5)

        self.Selectarea = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.Selectarea.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        gbSizer14 = wx.GridBagSizer(0, 0)
        gbSizer14.SetFlexibleDirection(wx.BOTH)
        gbSizer14.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Keyword = wx.StaticText(self.Selectarea, wx.ID_ANY, u"Keyword:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Keyword.Wrap(-1)
        gbSizer14.Add(self.Keyword, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Inputbox = wx.TextCtrl(self.Selectarea, wx.ID_ANY, u"Spa", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer14.Add(self.Inputbox, wx.GBPosition(0, 1), wx.GBSpan(1, 2), wx.ALL, 5)
        gbSizer14.AddGrowableCol(1)

        self.Fromdate = wx.StaticText(self.Selectarea, wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Fromdate.Wrap(-1)

        gbSizer14.Add(self.Fromdate, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.FROMdate = wx.adv.DatePickerCtrl(self.Selectarea, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                              wx.DefaultSize, wx.adv.DP_DEFAULT)
        gbSizer14.Add(self.FROMdate, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.ToDate = wx.StaticText(self.Selectarea, wx.ID_ANY, u"To:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ToDate.Wrap(-1)

        gbSizer14.Add(self.ToDate, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.ToDate = wx.adv.DatePickerCtrl(self.Selectarea, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                            wx.DefaultSize, wx.adv.DP_DEFAULT)
        gbSizer14.Add(self.ToDate, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.SearchButton = wx.Button(self.Selectarea, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer14.Add(self.SearchButton, wx.GBPosition(4, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        # self.Suburb = wx.StaticText( self.Selectarea, wx.ID_ANY, u"Suburb:", wx.DefaultPosition, wx.DefaultSize, 0 )
        # self.Suburb.Wrap( -1 )
        #
        # gbSizer14.Add( self.Suburb, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        #
        # SuburblistChoices = [ u"Pyrmont", u"Balgowlah", u"Darlinghurst", u"Balmain", u"Bellevue Hill", u"North Sydney", u"North Bondi", u"Darlinghurst", u"Bondi Beach", u"North Bondi", u"Mosman", u"Bondi Junction", u"Alexandria", u"Avalon", u"Sydney", u"Lane Cove West", u"Paddington", wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString, wx.EmptyString ]
        # self.Suburblist = wx.Choice( self.Selectarea, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, SuburblistChoices, 0 )
        # self.Suburblist.SetSelection( 15 )
        # gbSizer14.Add( self.Suburblist, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.Selectarea.SetSizer(gbSizer14)
        self.Selectarea.Layout()
        gbSizer14.Fit(self.Selectarea)
        bSizer4.Add(self.Selectarea, 1, wx.EXPAND | wx.ALL, 5)

        self.OutputScreen = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                              wx.HSCROLL | wx.VSCROLL)
        self.OutputScreen.SetScrollbars(1, 1, 1, 1)  # Enable scrollbars
        self.OutputScreen.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        gbSizer15 = wx.GridBagSizer(0, 0)
        gbSizer15.SetFlexibleDirection(wx.BOTH)
        gbSizer15.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.OutputTable = wx.grid.Grid(self.OutputScreen, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.OutputTable.CreateGrid(5, 5)
        self.OutputTable.EnableEditing(True)
        self.OutputTable.EnableGridLines(True)
        self.OutputTable.EnableDragGridSize(False)
        self.OutputTable.SetMargins(0, 0)

        # Columns
        self.OutputTable.EnableDragColMove(False)
        self.OutputTable.EnableDragColSize(True)
        self.OutputTable.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.OutputTable.EnableDragRowSize(True)
        self.OutputTable.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.OutputTable.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        gbSizer15.Add(self.OutputTable, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.OutputScreen.SetSizer(gbSizer15)
        self.OutputScreen.Layout()
        gbSizer15.Fit(self.OutputScreen)
        bSizer4.Add(self.OutputScreen, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Listingbutton.Bind(wx.EVT_BUTTON, self.ListingbuttonOnButtonClick)
        self.Pricebutton.Bind(wx.EVT_BUTTON, self.PricebuttonOnButtonClick)
        self.Reviewbutton.Bind(wx.EVT_BUTTON, self.ReviewbuttonOnButtonClick)
        self.Roomusagebutton.Bind(wx.EVT_BUTTON, self.RoomusagebuttonOnButtonClick)
        self.UserSpecificbutton.Bind(wx.EVT_BUTTON, self.UserSpecificbuttonOnButtonClick)
        self.Inputbox.Bind(wx.adv.EVT_DATE_CHANGED, self.InputChanged)
        self.FROMdate.Bind(wx.adv.EVT_DATE_CHANGED, self.FromDateOnDateChanged)
        self.ToDate.Bind(wx.adv.EVT_DATE_CHANGED, self.ToDateOnDateChanged)
        self.SearchButton.Bind(wx.EVT_BUTTON, self.SearchButtonOnButtonClick)

    # self.Suburblist.Bind( wx.EVT_CHOICE, self.SuburblistOnChoice )

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def ListingbuttonOnButtonClick(self, event):
        event.Skip()

    def PricebuttonOnButtonClick(self, event):
        event.Skip()

    def ReviewbuttonOnButtonClick(self, event):
        event.Skip()

    def RoomusagebuttonOnButtonClick(self, event):
        event.Skip()

    def UserSpecificbuttonOnButtonClick(self, event):
        event.Skip()

    def InputChanged(self, event):
        event.Skip()

    def FromDateOnDateChanged(self, event):
        event.Skip()

    def ToDateOnDateChanged(self, event):
        event.Skip()

    def SearchButtonOnButtonClick(self, event):
        event.Skip()

# def SuburblistOnChoice( self, event ):
# 	event.Skip()


###########################################################################
## Class PriceFrame
###########################################################################

class PriceFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Sydney Airbnb Dataset Analysis Tool",
                          pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.Uppermenu = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.Uppermenu.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        gbSizer18 = wx.GridBagSizer(0, 0)
        gbSizer18.SetFlexibleDirection(wx.BOTH)
        gbSizer18.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Listingbutton = wx.Button(self.Uppermenu, wx.ID_ANY, u"Listings", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer18.Add(self.Listingbutton, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Pricebutton = wx.Button(self.Uppermenu, wx.ID_ANY, u"PriceChart", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer18.Add(self.Pricebutton, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Reviewbutton = wx.Button(self.Uppermenu, wx.ID_ANY, u"Reviews", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer18.Add(self.Reviewbutton, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Roomusagebutton = wx.Button(self.Uppermenu, wx.ID_ANY, u"RoomUsage", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer18.Add(self.Roomusagebutton, wx.GBPosition(0, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.UserSpecificbutton = wx.Button(self.Uppermenu, wx.ID_ANY, u"UserSpecific", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        gbSizer18.Add(self.UserSpecificbutton, wx.GBPosition(0, 4), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Uppermenu.SetSizer(gbSizer18)
        self.Uppermenu.Layout()
        gbSizer18.Fit(self.Uppermenu)
        bSizer6.Add(self.Uppermenu, 1, wx.EXPAND | wx.ALL, 5)

        self.Selectarea = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.Selectarea.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        gbSizer19 = wx.GridBagSizer(0, 0)
        gbSizer19.SetFlexibleDirection(wx.BOTH)
        gbSizer19.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Fromdate = wx.StaticText(self.Selectarea, wx.ID_ANY, u"From:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Fromdate.Wrap(-1)

        gbSizer19.Add(self.Fromdate, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.FROMdate = wx.adv.DatePickerCtrl(self.Selectarea, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                              wx.DefaultSize, wx.adv.DP_DEFAULT)
        gbSizer19.Add(self.FROMdate, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.ToDate = wx.StaticText(self.Selectarea, wx.ID_ANY, u"To:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ToDate.Wrap(-1)

        gbSizer19.Add(self.ToDate, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.ToDate1 = wx.adv.DatePickerCtrl(self.Selectarea, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition,
                                             wx.DefaultSize, wx.adv.DP_DEFAULT)
        gbSizer19.Add(self.ToDate1, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.CreateChartButton = wx.Button(self.Selectarea, wx.ID_ANY, u"CreateChart", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        gbSizer19.Add(self.CreateChartButton, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Selectarea.SetSizer(gbSizer19)
        self.Selectarea.Layout()
        gbSizer19.Fit(self.Selectarea)
        bSizer6.Add(self.Selectarea, 1, wx.EXPAND | wx.ALL, 5)

        self.PriceTable = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.PriceTable.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_ACTIVECAPTION))

        gbSizer20 = wx.GridBagSizer(0, 0)
        gbSizer20.SetFlexibleDirection(wx.BOTH)
        gbSizer20.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_grid4 = wx.grid.Grid(self.PriceTable, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid4.CreateGrid(5, 5)
        self.m_grid4.EnableEditing(True)
        self.m_grid4.EnableGridLines(True)
        self.m_grid4.EnableDragGridSize(False)
        self.m_grid4.SetMargins(0, 0)

        # Columns
        self.m_grid4.EnableDragColMove(False)
        self.m_grid4.EnableDragColSize(True)
        self.m_grid4.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.m_grid4.EnableDragRowSize(True)
        self.m_grid4.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.m_grid4.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        gbSizer20.Add(self.m_grid4, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.PriceTable.SetSizer(gbSizer20)
        self.PriceTable.Layout()
        gbSizer20.Fit(self.PriceTable)
        bSizer6.Add(self.PriceTable, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Listingbutton.Bind(wx.EVT_BUTTON, self.ListingbuttonOnButtonClick)
        self.Pricebutton.Bind(wx.EVT_BUTTON, self.PricebuttonOnButtonClick)
        self.Reviewbutton.Bind(wx.EVT_BUTTON, self.ReviewbuttonOnButtonClick)
        self.Roomusagebutton.Bind(wx.EVT_BUTTON, self.RoomusagebuttonOnButtonClick)
        self.UserSpecificbutton.Bind(wx.EVT_BUTTON, self.UserSpecificbuttonOnButtonClick)
        self.ToDate1.Bind(wx.adv.EVT_DATE_CHANGED, self.ToDateOnDateChanged)
        self.CreateChartButton.Bind(wx.EVT_BUTTON, self.CreateChartButtonOnButtonClick)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def ListingbuttonOnButtonClick(self, event):
        event.Skip()

    def PricebuttonOnButtonClick(self, event):
        event.Skip()

    def ReviewbuttonOnButtonClick(self, event):
        event.Skip()

    def RoomusagebuttonOnButtonClick(self, event):
        event.Skip()

    def UserSpecificbuttonOnButtonClick(self, event):
        event.Skip()

    def ToDateOnDateChanged(self, event):
        event.Skip()

    def CreateChartButtonOnButtonClick(self, event):
        event.Skip()
