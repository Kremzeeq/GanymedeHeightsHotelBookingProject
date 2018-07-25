# python HotelBooking.py

from HotelBookingDB import HotelBookingDB

class HotelBooking(object):
    def __init__(self, bookingRefID, bookingRoomNumber, userBookingChoices):
        self.bookingRefID = bookingRefID
        self.bookingRoomNumber = bookingRoomNumber
        self.userBookingChoices = userBookingChoices
        HotelBookingDB.initialize()

    def newBookingJson(self):
        newBooking = {"BookingRefID": self.bookingRefID,
                      "RoomNumber": self.bookingRoomNumber}
        newBooking.update(self.userBookingChoices)
        return newBooking

    def saveBookingToMongo(self):
        HotelBookingDB.insert(collection='HotelBookings', data=self.newBookingJson())


