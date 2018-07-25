# python BookingPageController.py

from tkinter import *
import datetime
from datetime import datetime
from hotelBookingSystem.GetDateInfo import GetDateInfo
from hotelBookingSystem.BookingPageView import BookingPageView
from hotelBookingSystem.RoomDetailsController import RoomDetailsController
from hotelBookingSystem.RoomAvailability import RoomAvailability

class BookingPageController():

    def __init__(self,homepage):
        self.homepage = homepage
        self.bookingPage = Toplevel(self.homepage)
        self.hotelBookingPageView = BookingPageView(self.bookingPage,self.getRoomTypeList())
        self.getDateInfo = GetDateInfo()
        self.getBookingStartDate()
        self.getBookingEndDate()
        self.roomDetailsTrigger = False
        self.bookingPageActionOnConfirmingDates()

    def getBookingStartDate(self):
        userStartDateYearsChoice = self.hotelBookingPageView.startDateYearsToSelectChoice()
        userStartDateMonthsChoice= self.hotelBookingPageView.startDateMonthsToSelectChoice()
        userStartDateDaysChoice = self.hotelBookingPageView.startDateDaysToSelectChoice()

        # Obtain initial datetime.date object
        bookingStartDate = self.getDateInfo.getDateForSelectedDayMonthandYear(
            userStartDateYearsChoice, userStartDateMonthsChoice, userStartDateDaysChoice)

        # Obtain datetime.datetime object
        bookingStartDate = datetime.combine(bookingStartDate, datetime.min.time())
        return bookingStartDate

    def getBookingEndDate(self):

        userEndDateYearsChoice = self.hotelBookingPageView.endDateYearsToSelectChoice()
        userEndDateMonthsChoice= self.hotelBookingPageView.endDateMonthsToSelectChoice()
        userEndDateDaysChoice = self.hotelBookingPageView.endDateDaysToSelectChoice()

        # Obtain initial datetime.date object
        bookingEndDate = self.getDateInfo.getDateForSelectedDayMonthandYear(userEndDateYearsChoice, 
        userEndDateMonthsChoice, userEndDateDaysChoice)

        # Obtain datetime.datetime object
        bookingEndDate = datetime.combine(bookingEndDate, datetime.min.time())
        return bookingEndDate

    def initRoomAvailabilityOb(self):
        self.hotelRoomAvailability = RoomAvailability()
        return self.hotelRoomAvailability

    def getRoomTypeList(self):
        self.roomTypes = ["Single", "Double", "King", "Queen - Penthouse"]
        return self.roomTypes

    def getRoomNumbersToCheck(self):
        self.roomTypes = self.getRoomTypeList()

        if self.hotelBookingPageView.roomTypeChoice() == self.roomTypes[0]:
            return list(range(1,6))

        elif self.hotelBookingPageView.roomTypeChoice() == self.roomTypes[1]:
            return list(range(6,16))

        elif self.hotelBookingPageView.roomTypeChoice() == self.roomTypes[2]:
            return list(range(16,21))

        elif self.hotelBookingPageView.roomTypeChoice() == self.roomTypes[3]:
            return list(range(21,22))

    def checkRoomAvailability(self):
        self.initRoomAvailabilityOb()
        self.roomNumbersToCheck = self.getRoomNumbersToCheck()
        # Obtain hotel booking docs stored in HotelBookings collection in MongoDB
        self.hotelBookingsList = self.hotelRoomAvailability.getHotelBookingsCursor()

        for doc in self.hotelBookingsList:
            if doc["CheckOutDate"] > self.getBookingStartDate() and \
                    doc["CheckInDate"] < self.getBookingEndDate() and \
                    doc["RoomNumber"] in self.roomNumbersToCheck:
                self.roomNumbersToCheck.remove(doc["RoomNumber"])
        return self.roomNumbersToCheck
        # Returned list provides remaining room numbers available for the user defined date range

    def initBookingParameters(self):
        self.numberOfAdultsChoice = self.hotelBookingPageView.numberOfAdultsChoice()
        self.roomTypeChoice = self.hotelBookingPageView.roomTypeChoice()
        self.bookingStartDate = self.getBookingStartDate()
        self.bookingEndDate = self.getBookingEndDate()
        numberOfNights = self.bookingEndDate - self.bookingStartDate
        self.numberOfNightsInDays = numberOfNights.days

    def getMessageBoxText(self):
        self.bookingStartDate = self.getBookingStartDate()
        self.bookingEndDate = self.getBookingEndDate()
        self.bookingRoomNumberAvailability = self.checkRoomAvailability()

        if self.bookingStartDate < self.getDateInfo.datetimeDatetimeObForNow():
            return "Please ensure Booking Start Date is later than today's date"

        elif self.bookingStartDate >= self.bookingEndDate:
            return "Please ensure Booking End Date is later than Booking Start Date"
        
        elif self.hotelBookingPageView.numberOfAdultsChoice() == "Two Adults, One Room"\
                and self.hotelBookingPageView.roomTypeChoice() == "Single":
            return "Please reselect a room type, this option is not available"

        elif len(self.roomNumbersToCheck) == 0:
            return "Please select another date or room type, this option is not available"

        else:
            self.roomDetailsTrigger = True
            return "Processing Booking Details"
            print("Processing Booking Details")
            #self.processBookingDatesAndOpenRoomAvailability()

    def processBookingDatesAndOpenRoomAvailability(self):
        self.hotelBookingPageView.messageBox = self.hotelBookingPageView.\
            bookingDateMessageBox(self.getMessageBoxText())

        if self.roomDetailsTrigger == True:
            self.initBookingParameters()
            self.bookingRoomNumber = self.roomNumbersToCheck[0]
            self.userBookingChoices = {"NumberOfAdultsChoice": self.numberOfAdultsChoice, "RoomTypeChoice": self.roomTypeChoice,
                                       "CheckInDate": self.bookingStartDate,"CheckOutDate": self.bookingEndDate, "NumberOfNights": self.numberOfNightsInDays}
            print("Room Details Controller Initiated")
            self.hotelRoomDetailsPageController = RoomDetailsController(self.bookingPage, self.userBookingChoices, self.roomTypes,
                                                                        self.bookingRoomNumber)

    def bookingPageActionOnConfirmingDates(self):
        print("Booking Page 'Check Booking Dates' Button pressed")
        self.hotelBookingPageView.actionOnConfirmingDates = self.processBookingDatesAndOpenRoomAvailability
        self.bookingPage.mainloop()
