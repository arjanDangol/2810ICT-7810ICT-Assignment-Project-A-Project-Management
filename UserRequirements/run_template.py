#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx

from template_frame import IntroductionFrame as MyFrame


class IntroFrame(MyFrame):
    def __init__(self):
        super().__init__(None)

        self.Show()

    def ListingOnButtonClick(self, event):
        event.Skip()

    def PricebuttonOnButtonClick(self, event):
        event.Skip()

    def ReviewbuttonOnButtonClick(self, event):
        event.Skip()

    def RoomUsebuttonOnButtonClick(self, event):
        event.Skip()

    def KeywordtextboxOnText(self, event):
        current_evt = event.GetEventObject()
        label = current_evt.GetLabel()
        keyword_text = self.Keywordtextbox.GetValue()
        print("Keyword text: ", keyword_text)
        return keyword_text

    def SuburbchoiceOnChoice(self, event):
        current_evt = event.GetEventObject()
        label = current_evt.GetLabel()
        suburb = self.suburb.GetStringSelection()
        print("Keyword text: ", suburb)

    def SearchbuttonOnButtonClick(self, event):
        event.Skip()

    def FROMDATE2OnDateChanged(self, event):
        event.Skip()

    def TODATEPicker3OnDateChanged(self, event):
        event.Skip()


if __name__ == "__main__":

    app = wx.App(False)
    frame = IntroFrame()
    app.MainLoop()
