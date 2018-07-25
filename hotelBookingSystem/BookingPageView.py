# python BookingPageView.py

import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from hotelBookingSystem.GetDateInfo import GetDateInfo

class BookingPageView():

    def __init__(self,bookingWindow,roomTypes):
        self.bookingWindow = bookingWindow
        self.roomTypes = roomTypes
        self.bookingWindow.wm_state('zoomed') 
        self.getDateInfo = GetDateInfo()
        self.actionOnConfirmingDates = lambda: 1
        self.initBookingPage()
        self.initBookingPageHeaderFrame()
        self.initRoomTypeSelectionFrame()
        self.initStartDateSelectionFrame()
        self.initEndDateSelectionFrame()
        self.initBookingDatesButtonFrame()
        self.bindStartDateComboBoxesForMonthsAndYears()
        self.bindEndDateComboBoxesForMonthsAndYears()
        self.initBookingDatesButtonFrame()
        self.initMessageBoxFrame()
        self.messageBoxText = "Please select booking details"
        self.messageBox = self.bookingDateMessageBox(self.messageBoxText)
    
    def initBookingPage(self):
        self.bookingWindow.title("Ganymede Heights | Make A Booking")
        self.bookingWindow.configure(background='deep sky blue')
        self.bookingWindow.columnconfigure(0, weight=10)

    def initBookingPageHeaderFrame(self):
        self.bookingPageHeaderFrame = tkinter.Frame(self.bookingWindow)
        self.bookingPageHeaderImageFile = "hotelBookingSystem\\images\\canvaMakeABookingBanner.png"
        self.bookingPageHeaderImage = ImageTk.PhotoImage(Image.open(self.bookingPageHeaderImageFile))
        self.bookingPageHeaderImageLabel =  Label(self.bookingPageHeaderFrame, image=self.bookingPageHeaderImage)
        self.bookingPageHeaderImageLabel.configure(background="deep sky blue")

        self.bookingPageHeaderFrame.grid(row=0, column=0, sticky=N+S+E+W)
        self.bookingPageHeaderImageLabel.pack(side="top", fill="both", expand="yes")
        
    def createNewLinesInFrame(self,bookingPageFrame):
        return tkinter.Label(bookingPageFrame, text="\n\n\n\n", background='deep sky blue' )
        
    def createSpaceInFrame(self,bookingPageFrame):
        return tkinter.Label(bookingPageFrame, text="\t\t\t\t\t",background='deep sky blue' )
        
    def initRoomTypeSelectionFrame(self):
        print("In Room Type frame")
        self.roomTypeFrame = tkinter.Frame(self.bookingWindow)
        # Don't move this. This is for creating 'transparent labels'
        tabSpacesForRoomTypeFrame = self.createSpaceInFrame(self.roomTypeFrame)
        newLinesForRoomTypeFrame = self.createNewLinesInFrame(self.roomTypeFrame)
        self.roomOptionsBackgroundImageFilename  = ImageTk.PhotoImage(Image.open(
            "hotelBookingSystem\\images\\selectRoomOptions.png"))
        self.roomOptionBackgroundLabel = tkinter.Label(self.roomTypeFrame,
                                                       image=self.roomOptionsBackgroundImageFilename)
        self.roomOptionBackgroundLabel.configure(background='deep sky blue')

        self.numberOfAdultsLabel = tkinter.Label(self.roomTypeFrame,
                                                 text="Select Number of Adults:", bg="ivory1" )
        self.numberOfAdultsComboBox = ttk.Combobox(self.roomTypeFrame, state='readonly')
        self.numberOfAdultsComboBox['values'] = ["One Adult, One Room", "Two Adults, One Room"]
        self.numberOfAdultsComboBox.current(0)

        self.roomTypesLabel = tkinter.Label(self.roomTypeFrame, text="Select Room Type:", bg="ivory1" )
        self.roomTypesComboBox = ttk.Combobox(self.roomTypeFrame, state='readonly')
        self.roomTypesComboBox['values'] = self.roomTypes
        self.roomTypesComboBox.current(0)

        self.roomTypeFrame.grid(row=1, column=0,sticky=N+S+E+W)
        newLinesForRoomTypeFrame.pack(side=LEFT)
        self.roomOptionBackgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)
        tabSpacesForRoomTypeFrame.pack(side=RIGHT)
        self.roomTypesComboBox.pack(side=RIGHT)
        self.roomTypesLabel.pack(side=RIGHT)
        self.numberOfAdultsComboBox.pack(side=RIGHT)
        self.numberOfAdultsLabel.pack(side=RIGHT)
        
    def initStartDateSelectionFrame(self):
        print("In Start Date Selection frame")
        self.startDateFrame = tkinter.Frame(self.bookingWindow)
        self.startDateFrame.grid(row=2, column=0, sticky=N+S+E+W)

        tabSpacesForStartDateFrame = self.createSpaceInFrame(self.startDateFrame)
        newLinesForStartDateFrame = self.createNewLinesInFrame(self.startDateFrame)

        self.startDateBackgroundImageFilename  = ImageTk.\
            PhotoImage(Image.open("hotelBookingSystem\\images\\selectStartDate.png"))
        self.startDateBackgroundLabel = tkinter.Label(self.startDateFrame,
                                                      image=self.startDateBackgroundImageFilename)
        self.startDateBackgroundLabel.configure(background = 'deep sky blue')
        
        self.startDateYearsToSelectLabel = tkinter.Label(self.startDateFrame,
                                                         text="Select Year:", bg="ivory1")
        self.startDateYearsToSelectComboBox = ttk.Combobox(self.startDateFrame, state='readonly')
        self.startDateYearsToSelectComboBox['values'] = self.getDateInfo.yearList()
        self.startDateYearsToSelectComboBox.current(0)

        self.startDateMonthsToSelectLabel = tkinter.Label(self.startDateFrame,
                                                          text="Select Month:", bg="ivory1")
        self.startDateMonthsToSelectComboBox = ttk.Combobox(self.startDateFrame, state='readonly')
        self.startDateMonthsToSelectComboBox['values'] = self.getDateInfo.getMonthListForCurrentYear()
        self.startDateMonthsToSelectComboBox.current(0)

        self.startDateDaysToSelectLabel = tkinter.Label(self.startDateFrame,
                                                        text="Select Day:", bg="ivory1")
        self.startDateDaysToSelectComboBox = ttk.Combobox(self.startDateFrame, state='readonly')
        self.startDateDaysToSelectComboBox['values'] = self.getDateInfo.getDaysForCurrentYearAndSelectedMonth(
            self.getDateInfo.now.year,self.startDateMonthsToSelectComboBox.get())
        self.startDateDaysToSelectComboBox.current(0)

        newLinesForStartDateFrame.pack(side=LEFT)
        self.startDateBackgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)
        tabSpacesForStartDateFrame.pack(side=RIGHT)
        self.startDateYearsToSelectComboBox.pack(side=RIGHT)
        self.startDateYearsToSelectLabel.pack(side=RIGHT)
        self.startDateMonthsToSelectComboBox.pack(side=RIGHT)
        self.startDateMonthsToSelectLabel.pack(side=RIGHT)
        self.startDateDaysToSelectComboBox.pack(side=RIGHT)
        self.startDateDaysToSelectLabel.pack(side=RIGHT)
        
    def initEndDateSelectionFrame(self):
        print("In End Date Selection frame")
        self.endDateFrame = tkinter.Frame(self.bookingWindow)
        self.endDateFrame.grid(row=4, column=0, sticky=N+S+E+W)

        tabSpacesForEndDateFrame = self.createSpaceInFrame(self.endDateFrame)
        newLinesForEndDateFrame = self.createNewLinesInFrame(self.endDateFrame)

        self.endDateBackgroundImageFilename  = ImageTk.PhotoImage(Image.open(
            "hotelBookingSystem\\images\\selectEndDate.png"))
        self.endDateBackgroundLabel = tkinter.Label(self.endDateFrame, image=self.endDateBackgroundImageFilename)
        self.endDateBackgroundLabel.configure(background='deep sky blue')
        
        self.endDateYearsToSelectLabel = tkinter.Label(self.endDateFrame, text="Select Year:", bg="ivory1")
        self.endDateYearsToSelectComboBox = ttk.Combobox(self.endDateFrame, state='readonly')
        self.endDateYearsToSelectComboBox['values'] = self.getDateInfo.yearList()
        self.endDateYearsToSelectComboBox.current(0)

        self.endDateMonthsToSelectLabel = tkinter.Label(self.endDateFrame, text="Select Month:", bg="ivory1")
        self.endDateMonthsToSelectComboBox = ttk.Combobox(self.endDateFrame, state='readonly')
        self.endDateMonthsToSelectComboBox['values'] = self.getDateInfo.getMonthListForCurrentYear()
        self.endDateMonthsToSelectComboBox.current(0)

        self.endDateDaysToSelectLabel = tkinter.Label(self.endDateFrame, text="Select Day:", bg="ivory1")
        self.endDateDaysToSelectComboBox = ttk.Combobox(self.endDateFrame, state='readonly')
        self.endDateDaysToSelectComboBox['values'] =  self.getDateInfo.getDaysForCurrentYearAndSelectedMonth(
            self.getDateInfo.now.year, self.endDateMonthsToSelectComboBox.get())
        self.endDateDaysToSelectComboBox.current(0)

        newLinesForEndDateFrame.pack(side=LEFT)
        self.endDateBackgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)
        tabSpacesForEndDateFrame.pack(side=RIGHT)
        self.endDateYearsToSelectComboBox.pack(side=RIGHT)
        self.endDateYearsToSelectLabel.pack(side=RIGHT)
        self.endDateMonthsToSelectComboBox.pack(side=RIGHT)
        self.endDateMonthsToSelectLabel.pack(side=RIGHT)
        self.endDateDaysToSelectComboBox.pack(side=RIGHT)
        self.endDateDaysToSelectLabel.pack(side=RIGHT)

    def numberOfAdultsChoice(self):
        return self.numberOfAdultsComboBox.get()
        
    def roomTypeChoice(self):
        return self.roomTypesComboBox.get()

    def startDateYearsToSelectChoice(self):
        return self.startDateYearsToSelectComboBox.get()
        
    def endDateYearsToSelectChoice(self):
        return self.endDateYearsToSelectComboBox.get()

    def startDateMonthsToSelectChoice(self):
        return self.startDateMonthsToSelectComboBox.get()

    def endDateMonthsToSelectChoice(self):
        return self.endDateMonthsToSelectComboBox.get()

    def startDateDaysToSelectChoice(self):
        return self.startDateDaysToSelectComboBox.get()
        
    def endDateDaysToSelectChoice(self):
        return self.endDateDaysToSelectComboBox.get()

    def changeStartDateMonthsAccordingToYear(self,event):
        print("Start Date Year has been changed.")
        self.startDateMonthsToSelectComboBox.set('') # clear the months combo box
        print(self.startDateYearsToSelectChoice())
        print(self.getDateInfo.yearsToSelect[0])

         # Add entries to months combo box for the selected year
        if self.startDateYearsToSelectChoice() == str(self.getDateInfo.yearsToSelect[0]):
            self.startDateMonthsToSelectComboBox['values'] = self.getDateInfo.getMonthListForCurrentYear()
            self.startDateMonthsToSelectComboBox.current(0)
        elif self.startDateYearsToSelectChoice() == str(self.getDateInfo.yearsToSelect[1]):
            self.startDateMonthsToSelectComboBox['values'] = self.getDateInfo.getMonthListForNextYear()
            self.startDateMonthsToSelectComboBox.current(0)
        else:
            self.startDateMonthsToSelectComboBox['values'] = []

    def changeEndDateMonthsAccordingToYear(self,event):
                    
        print("End Date Year has been changed.")
        self.endDateMonthsToSelectComboBox.set('') # Clears the months combo box
        print(self.endDateYearsToSelectChoice())
        print(self.getDateInfo.yearsToSelect[0])

        # Add entries to months combo box for the selected year
        if self.endDateYearsToSelectChoice() == str(self.getDateInfo.yearsToSelect[0]):
            self.endDateMonthsToSelectComboBox['values'] = self.getDateInfo.getMonthListForCurrentYear()
            self.endDateMonthsToSelectComboBox.current(0)
        elif self.endDateYearsToSelectChoice() == str(self.getDateInfo.yearsToSelect[1]):
            self.endDateMonthsToSelectComboBox['values'] = self.getDateInfo.getMonthListForNextYear()
            self.endDateMonthsToSelectComboBox.current(0)
        else:
            self.startDateMonthsToSelectComboBox['values'] = []

    def changeStartDateDaysAccordingToYearAndMonth(self,event):
        print("Start Date Month has changed")
        self.startDateDaysToSelectComboBox.set('') #Clear the days combo box
        # Add entries to months combo box for the selected month and year
        self.startDateDaysToSelectComboBox['values'] = self.getDateInfo.getDaysForCurrentYearAndSelectedMonth(
            self.startDateYearsToSelectChoice(),self.startDateMonthsToSelectChoice())
        self.startDateDaysToSelectComboBox.current(0)

    def changeEndDateDaysAccordingToYearAndMonth(self,event):
        print("End Date Month has changed")
        self.endDateDaysToSelectComboBox.set('') # Clear the days combo box
        # Add entries to months combo box for the selected month and year
        self.endDateDaysToSelectComboBox['values'] = self.getDateInfo.getDaysForCurrentYearAndSelectedMonth(
            self.endDateYearsToSelectChoice(),self.endDateMonthsToSelectChoice())
        self.endDateDaysToSelectComboBox.current(0)
        
    def bindStartDateComboBoxesForMonthsAndYears(self):
        self.startDateYearsToSelectComboBox.bind("<<ComboboxSelected>>", self.changeStartDateMonthsAccordingToYear)
        self.startDateMonthsToSelectComboBox.bind("<<ComboboxSelected>>", self.changeStartDateDaysAccordingToYearAndMonth)

    def bindEndDateComboBoxesForMonthsAndYears(self):
        self.endDateYearsToSelectComboBox.bind("<<ComboboxSelected>>", self.changeEndDateMonthsAccordingToYear)
        self.endDateMonthsToSelectComboBox.bind("<<ComboboxSelected>>", self.changeEndDateDaysAccordingToYearAndMonth)
        
    def hotelBookingDatesButton(self):
        return Button(self.bookingDatesButtonFrame, text="Check Booking Dates",
                      command=lambda: self.pressedConfirmBookingDates(), padx=20, bg="ivory1")

    def initBookingDatesButtonFrame(self):
        self.bookingDatesButtonFrame = tkinter.Frame(self.bookingWindow)
        self.bookingDatesButtonFrame.configure(background ="deep sky blue")
        self.datesConfirmationButton = self.hotelBookingDatesButton()

        self.bookingDatesButtonFrame.grid(row=6, column=0, sticky=N+S+E+W)
        self.datesConfirmationButton.pack(pady=20, padx=20)
    
    def pressedConfirmBookingDates(self):
        func_to_call = self.actionOnConfirmingDates
        func_to_call()

    def initMessageBoxFrame(self):
        self.bookingDateMessageFrame = tkinter.Frame(self.bookingWindow)
        self.bookingDateMessageFrame.configure(background="deep sky blue")

        self.bookingDateMessageFrame.grid(row=5, column=0)
        self.bookingDateMessageFrame.grid_rowconfigure(0, weight=1)
        self.bookingDateMessageFrame.grid_columnconfigure(0, weight=1)

    def bookingDateMessageBox(self,messageBoxText):
        self.bookingDateMessageBoxLabel = tkinter.Label(self.bookingDateMessageFrame,
                                                        text=messageBoxText, bg="ivory1", fg='red')
        self.bookingDateMessageBoxLabel.grid(row=0, column= 0, sticky=N+S+E+W)
 