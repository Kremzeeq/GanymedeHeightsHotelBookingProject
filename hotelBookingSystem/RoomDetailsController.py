# python RoomDetailsController.py

from tkinter import *
from PIL import ImageGrab
import uuid
from hotelBookingSystem.RoomDetailsView import RoomDetailsView
from hotelBookingSystem.HotelBooking import HotelBooking
from hotelBookingSystem.RoomAvailability import RoomAvailability

class RoomDetailsController():

    def __init__(self,bookingPage,userBookingChoices,roomTypeList,bookingRoomNumber):
        self.bookingPage = bookingPage
        self.userBookingChoices = userBookingChoices
        self.roomTypeList = roomTypeList
        self.bookingRoomNumber = bookingRoomNumber
        self.openRoomDetailsWindow()
        self.roomDetailsPageActionOnConfirmingDates()
        self.roomDetailsPageActionOnSavingBookingDetails()
        self.bookingPage.wm_withdraw()
    
    def returnRoomPrice(self):
        self.roomPricePerNightForOneAdultOneRoom = {"Single":60, "Double": 120, "King": 160, "Queen - Penthouse": 200}
        self.roomPricesPerNightForTwoAdultsOneRoom = {"Double": 200, "King": 160, "Queen - Penthouse": 320}

        self.numberOfAdultsChoice = self.userBookingChoices.get("NumberOfAdultsChoice")
        self.roomTypeChoice = self.userBookingChoices.get("RoomTypeChoice")

        if self.numberOfAdultsChoice == "One Adult, One Room":
            self.roomPricePerNight = self.roomPricePerNightForOneAdultOneRoom.get(self.roomTypeChoice)
            return self.roomPricePerNight
        elif self.numberOfAdultsChoice == "Two Adults, One Room" and self.roomTypeChoice == "Single":
            pass
        else:
            self.roomPricePerNight = self.roomPricesPerNightForTwoAdultsOneRoom.get(self.roomTypeChoice)
            return self.roomPricePerNight

    def openRoomDetailsWindow(self):
        self.roomDetailsPage = Toplevel(self.bookingPage)
        numberOfNights = self.userBookingChoices.get("NumberOfNights")
        roomPricePerNight = self.returnRoomPrice()
        roomPriceForNumberOfNights = self.roomPricePerNight * numberOfNights

        self.roomPriceInfo = {"RoomPricePerNight": roomPricePerNight,
                              "RoomPricePerNightForNumberOfNights": roomPriceForNumberOfNights}
        
        self.hotelRoomDetailsView = RoomDetailsView(self.roomDetailsPage,self.userBookingChoices,self.roomTypeList,
                                                    self.roomPriceInfo)

    def processPaymentAndReturnRoomNumber(self):
        bookingRefID = str(uuid.uuid4().hex.upper())
        bookingRefID = bookingRefID[8:17]
        self.hotelRoomDetailsView.initBookingPaymentMessage(self.bookingRoomNumber, bookingRefID)
        self.hotelRoomDetailsView.initSaveBookingDetailsFrame()
        newHotelBooking = HotelBooking(bookingRefID,self.bookingRoomNumber,self.userBookingChoices)
        newHotelBooking.saveBookingToMongo()
        self.roomAvailability = RoomAvailability()
        print("Here are all the bookings in the Hotel Booking DB:")
        return self.roomAvailability.showAllHotelBookings()

    def roomDetailsPageActionOnConfirmingDates(self):
        self.hotelRoomDetailsView.actionOnConfirmingPayment = self.processPaymentAndReturnRoomNumber
    
    def processBookingDetailsScreenGrabForImageFile(self):
        self.bookingDetailsImage = ImageGrab.grab().save("bookingDetails.png", "PNG")
        self.hotelRoomDetailsView.initImageGrabFrame()
        print("Booking Details have been saved in bookingDetails.png file")
        self.roomDetailsPage.destroy()
        self.roomDetailsPage.mainloop()

    def roomDetailsPageActionOnSavingBookingDetails(self):
        self.hotelRoomDetailsView.actionOnSavingDetails = self.processBookingDetailsScreenGrabForImageFile