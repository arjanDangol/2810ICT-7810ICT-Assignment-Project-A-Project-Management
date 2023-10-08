#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg

from template_frame import IntroductionFrame as IntroFrame
from template_frame import ListingTAble as ListingFrame
from template_frame import Reviewframe as ReviewFrame
from template_frame import Roomusagescreen as RoomUsageFrame
from template_frame import UserSpecificFrame as UserSpecificFrame
from template_frame import PriceFrame as PriceFrame

from r1_airbnb_lisitng_report import list_airbnb_listing
from r2_property_price_distribution import show_plot
from r3_keyword_search import retrieve_keyword_specific_listing
from r4_cleanliness_analysis import retrieve_reviews_listing
from r5_room_usage_analysis import retrieve_room_usage_listings


class IntroFrameScreen(IntroFrame):
    def __init__(self):
        super().__init__(None)

        self.Show()

    def ListingButtonOnButtonClick(self, event):
        listing_frame = ListingFrameScreen(suburb=None, from_date=None, to_date=None, listing_result=None)
        listing_frame.SetTitle("Listing Page")
        listing_frame.Show()
        self.Hide()

    def PriceButtonOnButtonClick(self, event):
        price_frame = PriceFrameScreen()
        price_frame.SetTitle("Price Chart Page")
        price_frame.Show()
        self.Hide()

    def ReviewButtonOnButtonClick(self, event):
        review_frame = ReviewFrameScreen()
        review_frame.SetTitle("Review Page")
        review_frame.Show()
        self.Hide()

    def RoomusebuttonOnButtonClick(self, event):
        room_use_frame = RoomUsageFrameScreen()
        room_use_frame.SetTitle("Room Usage Page")
        room_use_frame.Show()
        self.Hide()

    def UserSpecificButtonOnButtonClick(self, event):
        user_specific_frame = UserSpecificFrameScreen()
        user_specific_frame.SetTitle("User Specific Page")
        user_specific_frame.Show()
        self.Hide()

    def GetSuburb(self, event=None):
        suburb = self.Suburblist.GetStringSelection()
        return suburb

    def GetFromDate(self, event=None):
        from_date = self.Fromdate.GetValue()
        formatted_from_date = from_date.Format("%Y-%m-%d")
        return formatted_from_date

    def GetToDate(self, event=None):
        to_date = self.Todate.GetValue()
        formatted_to_date = to_date.Format("%Y-%m-%d")
        return formatted_to_date

    def SuburblistOnChoice(self, event):
        suburb = self.GetSuburb(event)
        return suburb

    def FromdateOnDateChanged(self, event):
        from_date = self.GetFromDate(event)
        return from_date

    def TodateOnDateChanged(self, event):
        to_date = self.GetToDate(event)
        return to_date

    def SearchbuttonOnButtonClick(self, event):
        self.TriggerSearchButtonClick()

    def TriggerSearchButtonClick(self):
        suburb = self.GetSuburb()
        from_date = self.GetFromDate()
        to_date = self.GetToDate()
        listing_result = list_airbnb_listing(suburb, from_date, to_date)

        listing_frame = ListingFrameScreen(suburb, from_date, to_date, listing_result)
        listing_frame.SetTitle("Listing Page")
        listing_frame.Show()
        self.Hide()


class ListingFrameScreen(ListingFrame):
    def __init__(self, suburb, from_date, to_date, listing_result):
        super().__init__(None)
        self.listing_result = listing_result
        if self.listing_result is not None and not self.listing_result.empty:
            self.UpdateGrid()  # Call the method only if listing_result has data

            # Set values to GUI elements
            self.Suburblist.SetStringSelection(suburb)

            # Parse date strings to wx.DateTime objects and set them to the date pickers
            from_date_dt = wx.DateTime()
            from_date_dt.ParseFormat(from_date, "%Y-%m-%d")
            self.Fromdate.SetValue(from_date_dt)

            to_date_dt = wx.DateTime()
            to_date_dt.ParseFormat(to_date, "%Y-%m-%d")
            self.Todate.SetValue(to_date_dt)

        self.Show()

    def UpdateGrid(self):
        print(self.listing_result)
        num_rows, num_cols = self.listing_result.shape

        # Set the grid size based on the number of rows and columns in the data
        self.Listtable.ClearGrid()
        self.Listtable.DeleteRows(0, self.Listtable.GetNumberRows())
        self.Listtable.DeleteCols(0, self.Listtable.GetNumberCols())
        self.Listtable.AppendRows(num_rows)
        self.Listtable.AppendCols(num_cols)

        # Set column labels
        column_labels = ['Listing Id', 'Suburb', 'Description', 'Name', 'Street', 'State', 'Zipcode']
        for col_idx, label in enumerate(column_labels):
            self.Listtable.SetColLabelValue(col_idx, label)

        # Update cell values with data
        for row_idx in range(num_rows):
            for col_idx in range(num_cols):
                value = str(self.listing_result.iloc[row_idx, col_idx])
                self.Listtable.SetCellValue(row_idx, col_idx, value)

    def ListingbuttonOnButtonClick(self, event):
        listing_frame = ListingFrameScreen(suburb=None, from_date=None, to_date=None, listing_result=None)
        listing_frame.SetTitle("Listing Page")
        listing_frame.Show()
        self.Hide()

    def PriceButtonOnButtonClick(self, event):
        price_frame = PriceFrameScreen()
        price_frame.SetTitle("Price Chart Page")
        price_frame.Show()
        self.Hide()

    def ReviewbuttonOnButtonClick(self, event):
        review_frame = ReviewFrameScreen()
        review_frame.SetTitle("Review Page")
        review_frame.Show()
        self.Hide()

    def RoomusebuttonOnButtonClick(self, event):
        room_use_frame = RoomUsageFrameScreen()
        room_use_frame.SetTitle("Room Usage Page")
        room_use_frame.Show()
        self.Hide()

    def UserSpecificButtonOnButtonClick(self, event):
        user_specific_frame = UserSpecificFrameScreen()
        user_specific_frame.SetTitle("User Specific Page")
        user_specific_frame.Show()
        self.Hide()

    def GetSuburb(self, event=None):
        suburb = self.Suburblist.GetStringSelection()
        return suburb

    def GetFromDate(self, event=None):
        from_date = self.Fromdate.GetValue()
        formatted_from_date = from_date.Format("%Y-%m-%d")
        return formatted_from_date

    def GetToDate(self, event=None):
        to_date = self.Todate.GetValue()
        formatted_to_date = to_date.Format("%Y-%m-%d")
        return formatted_to_date

    def SuburblistOnChoice(self, event):
        suburb = self.GetSuburb(event)
        return suburb

    def FromdateOnDateChanged(self, event):
        from_date = self.GetFromDate(event)
        return from_date

    def TodateOnDateChanged(self, event):
        to_date = self.GetToDate(event)
        return to_date

    def SearchbuttonOnButtonClick(self, event):
        self.TriggerSearchButtonClick()

    def TriggerSearchButtonClick(self):
        suburb = self.GetSuburb()
        from_date = self.GetFromDate()
        to_date = self.GetToDate()
        self.listing_result = list_airbnb_listing(suburb, from_date, to_date)
        self.UpdateGrid()

class ReviewFrameScreen(ReviewFrame):
    def __init__(self):
        super().__init__(None)
        self.review_listing = None

        self.Show()

    def UpdateGrid(self):
        print(self.review_listing)
        num_rows, num_cols = self.review_listing.shape

        # Set the grid size based on the number of rows and columns in the data
        self.ReviewTable.ClearGrid()
        self.ReviewTable.DeleteRows(0, self.ReviewTable.GetNumberRows())
        self.ReviewTable.DeleteCols(0, self.ReviewTable.GetNumberCols())
        self.ReviewTable.AppendRows(num_rows)
        self.ReviewTable.AppendCols(num_cols)

        # Set column labels
        column_labels = ['Listing Id', 'Id', 'Date', 'Reviewer Id', 'Reviewer Name', 'Comments', 'Keywords Included']
        for col_idx, label in enumerate(column_labels):
            self.ReviewTable.SetColLabelValue(col_idx, label)

        # Update cell values with data
        for row_idx in range(num_rows):
            for col_idx in range(num_cols):
                value = str(self.review_listing.iloc[row_idx, col_idx])
                self.ReviewTable.SetCellValue(row_idx, col_idx, value)


    def ListingbuttonOnButtonClick(self, event):
        listing_frame = ListingFrameScreen(suburb=None, from_date=None, to_date=None, listing_result=None)
        listing_frame.SetTitle("Listing Page")
        listing_frame.Show()
        self.Hide()

    def PriceOnButtonClick(self, event):
        price_frame = PriceFrameScreen()
        price_frame.SetTitle("Price Chart Page")
        price_frame.Show()
        self.Hide()

    def ReviewbuttonOnButtonClick(self, event):
        review_frame = ReviewFrameScreen()
        review_frame.SetTitle("Review Page")
        review_frame.Show()
        self.Hide()

    def RoomusagebuttonOnButtonClick(self, event):
        room_use_frame = RoomUsageFrameScreen()
        room_use_frame.SetTitle("Room Usage Page")
        room_use_frame.Show()
        self.Hide()

    def UserSpecificbuttonOnButtonClick(self, event):
        user_specific_frame = UserSpecificFrameScreen()
        user_specific_frame.SetTitle("User Specific Page")
        user_specific_frame.Show()
        self.Hide()

    def GetFromDate(self, event=None):
        from_date = self.FromDate.GetValue()
        formatted_from_date = from_date.Format("%Y-%m-%d")
        return formatted_from_date

    def GetToDate(self, event=None):
        to_date = self.ToDate.GetValue()
        formatted_to_date = to_date.Format("%Y-%m-%d")
        return formatted_to_date

    def FromdateOnDateChanged(self, event):
        from_date = self.GetFromDate(event)
        return from_date

    def TodateOnDateChanged(self, event):
        to_date = self.GetToDate(event)
        return to_date

    def SearcButtonOnButtonClick(self, event):
        self.TriggerSearchButtonClick()

    def TriggerSearchButtonClick(self):
        from_date = self.GetFromDate()
        to_date = self.GetToDate()
        print(from_date, to_date)
        self.review_listing = retrieve_reviews_listing(from_date, to_date)
        self.UpdateGrid()


class RoomUsageFrameScreen(RoomUsageFrame):
    def __init__(self):
        super().__init__(None)
        self.room_usage_listing = None

        self.Show()

    def UpdateGrid(self):
        print(self.room_usage_listing)
        # Check if there are rows in the grid
        if self.room_usage_listing.empty:
            print("No data to display.")
            return
        num_rows, num_cols = self.room_usage_listing.shape

        # Set the grid size based on the number of rows and columns in the data
        self.RoomUsageTable.ClearGrid()
        self.RoomUsageTable.DeleteRows(0, self.RoomUsageTable.GetNumberRows())
        self.RoomUsageTable.DeleteCols(0, self.RoomUsageTable.GetNumberCols())
        self.RoomUsageTable.AppendRows(num_rows)
        self.RoomUsageTable.AppendCols(num_cols)

        # Set column labels
        column_labels = ['Listing Id', 'Usage Count']
        for col_idx, label in enumerate(column_labels):
            self.RoomUsageTable.SetColLabelValue(col_idx, label)

        # Update cell values with data
        for row_idx in range(num_rows):
            for col_idx in range(num_cols):
                value = str(self.room_usage_listing.iloc[row_idx, col_idx])
                self.RoomUsageTable.SetCellValue(row_idx, col_idx, value)

    def ListingbuttonOnButtonClick(self, event):
        listing_frame = ListingFrameScreen(suburb=None, from_date=None, to_date=None, listing_result=None)
        listing_frame.SetTitle("Listing Page")
        listing_frame.Show()
        self.Hide()

    def PricebuttonOnButtonClick(self, event):
        price_frame = PriceFrameScreen()
        price_frame.SetTitle("Price Chart Page")
        price_frame.Show()
        self.Hide()

    def ReviewbuttonOnButtonClick(self, event):
        review_frame = ReviewFrameScreen()
        review_frame.SetTitle("Review Page")
        review_frame.Show()
        self.Hide()

    def RoomusagebuttonOnButtonClick(self, event):
        room_use_frame = RoomUsageFrameScreen()
        room_use_frame.SetTitle("Room Usage Page")
        room_use_frame.Show()
        self.Hide()

    def UserSpecificButtonOnButtonClick(self, event):
        user_specific_frame = UserSpecificFrameScreen()
        user_specific_frame.SetTitle("User Specific Page")
        user_specific_frame.Show()
        self.Hide()

    def GetFromDate(self, event=None):
        from_date = self.FromDate.GetValue()
        formatted_from_date = from_date.Format("%Y-%m-%d")
        return formatted_from_date

    def GetToDate(self, event=None):
        to_date = self.ToDate.GetValue()
        formatted_to_date = to_date.Format("%Y-%m-%d")
        return formatted_to_date

    def FromDateOnDateChanged(self, event):
        from_date = self.GetFromDate(event)
        return from_date

    def ToDateOnDateChanged(self, event):
        to_date = self.GetToDate(event)
        return to_date

    def SearchButtonOnButtonClick(self, event):
        self.TriggerSearchButtonClick()

    def TriggerSearchButtonClick(self):
        from_date = self.GetFromDate()
        to_date = self.GetToDate()
        self.room_usage_listing = retrieve_room_usage_listings(from_date, to_date)
        self.UpdateGrid()


class UserSpecificFrameScreen(UserSpecificFrame):
    def __init__(self):
        super().__init__(None)
        self.keyword_specific_listing = None

        self.Show()

    def UpdateGrid(self):
        print(self.keyword_specific_listing)
        # Check if there are rows in the grid
        if self.keyword_specific_listing.empty:
            print("No data to display.")
            return
        num_rows, num_cols = self.keyword_specific_listing.shape

        # Set the grid size based on the number of rows and columns in the data
        self.OutputTable.ClearGrid()
        self.OutputTable.DeleteRows(0, self.OutputTable.GetNumberRows())
        self.OutputTable.DeleteCols(0, self.OutputTable.GetNumberCols())
        self.OutputTable.AppendRows(num_rows)
        self.OutputTable.AppendCols(num_cols)

        # Set column labels
        column_labels = ['Listing Id', 'Name', 'Summary', 'Space', 'Description', 'Notes', 'House Rules', 'Amenities']
        for col_idx, label in enumerate(column_labels):
            self.OutputTable.SetColLabelValue(col_idx, label)

        # Update cell values with data
        for row_idx in range(num_rows):
            for col_idx in range(num_cols):
                value = str(self.keyword_specific_listing.iloc[row_idx, col_idx])
                self.OutputTable.SetCellValue(row_idx, col_idx, value)


    def ListingbuttonOnButtonClick(self, event):
        listing_frame = ListingFrameScreen(suburb=None, from_date=None, to_date=None, listing_result=None)
        listing_frame.SetTitle("Listing Page")
        listing_frame.Show()
        self.Hide()

    def PricebuttonOnButtonClick(self, event):
        price_frame = PriceFrameScreen()
        price_frame.SetTitle("Price Page")
        price_frame.Show()
        self.Hide()

    def ReviewbuttonOnButtonClick(self, event):
        review_frame = ReviewFrameScreen()
        review_frame.SetTitle("Review Page")
        review_frame.Show()
        self.Hide()

    def RoomusagebuttonOnButtonClick(self, event):
        room_use_frame = RoomUsageFrameScreen()
        room_use_frame.SetTitle("Room Usage Page")
        room_use_frame.Show()
        self.Hide()

    def UserSpecificbuttonOnButtonClick(self, event):
        user_specific_frame = UserSpecificFrameScreen()
        user_specific_frame.SetTitle("User Specific Page")
        user_specific_frame.Show()
        self.Hide()

    def GetKeyword(self, event=None):
        keyword = self.Inputbox.GetValue()
        return keyword

    def GetFromDate(self, event=None):
        from_date = self.FROMdate.GetValue()
        formatted_from_date = from_date.Format("%Y-%m-%d")
        return formatted_from_date

    def GetToDate(self, event=None):
        to_date = self.ToDate.GetValue()
        formatted_to_date = to_date.Format("%Y-%m-%d")
        return formatted_to_date

    def InputChanged(self, event):
        keyword = self.GetKeyword(event)
        return keyword

    def FromDateOnDateChanged(self, event):
        from_date = self.GetFromDate(event)
        return from_date

    def ToDateOnDateChanged(self, event):
        to_date = self.GetToDate(event)
        return to_date

    def SearchButtonOnButtonClick(self, event):
        self.TriggerSearchButtonClick()

    def TriggerSearchButtonClick(self):
        keyword = self.GetKeyword()
        from_date = self.GetFromDate()
        to_date = self.GetToDate()
        self.keyword_specific_listing = retrieve_keyword_specific_listing(keyword, from_date, to_date)
        self.UpdateGrid()


class PriceFrameScreen(PriceFrame):
    def __init__(self):
        super().__init__(None)
        self.plot_data = None

        self.Show()

    def UpdatePlot(self):
        print(self.plot_data)
        h, w = self.CanvasPanel.GetSize()
        self.plot_data.set_size_inches(h / self.plot_data.get_dpi(), w / self.plot_data.get_dpi())

        canvas = FigureCanvasWxAgg(self.CanvasPanel, -1, self.plot_data)
        canvas.SetSize(self.CanvasPanel.GetSize())

        self.Layout()

    def ListingbuttonOnButtonClick(self, event):
        listing_frame = ListingFrameScreen(suburb=None, from_date=None, to_date=None, listing_result=None)
        listing_frame.SetTitle("Listing Page")
        listing_frame.Show()
        self.Hide()

    def PricebuttonOnButtonClick(self, event):
        price_frame = PriceFrameScreen()
        price_frame.SetTitle("Price Page")
        price_frame.Show()
        self.Hide()

    def ReviewbuttonOnButtonClick(self, event):
        review_frame = ReviewFrameScreen()
        review_frame.SetTitle("Review Page")
        review_frame.Show()
        self.Hide()

    def RoomusagebuttonOnButtonClick(self, event):
        room_use_frame = RoomUsageFrameScreen()
        room_use_frame.SetTitle("Room Page")
        room_use_frame.Show()
        self.Hide()

    def UserSpecificbuttonOnButtonClick(self, event):
        user_specific_frame = UserSpecificFrameScreen()
        user_specific_frame.SetTitle("User Specific Page")
        user_specific_frame.Show()
        self.Hide()

    def GetFromDate(self, event=None):
        from_date = self.FROMdate.GetValue()
        formatted_from_date = from_date.Format("%Y-%m-%d")
        return formatted_from_date

    def GetToDate(self, event=None):
        to_date = self.ToDate1.GetValue()
        formatted_to_date = to_date.Format("%Y-%m-%d")
        return formatted_to_date

    def FromDateOnDateChanged(self, event):
        from_date = self.GetFromDate(event)
        return from_date

    def ToDateOnDateChanged(self, event):
        to_date = self.GetToDate(event)
        return to_date

    def CreateChartButtonOnButtonClick(self, event):
        self.TriggerSearchButtonClick()

    def TriggerSearchButtonClick(self):
        from_date = self.GetFromDate()
        to_date = self.GetToDate()
        self.plot_data = show_plot(from_date, to_date)
        self.UpdatePlot()


if __name__ == "__main__":
    app = wx.App(False)
    frame = IntroFrameScreen()
    app.MainLoop()
