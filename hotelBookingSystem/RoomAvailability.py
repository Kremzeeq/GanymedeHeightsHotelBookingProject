

from HotelBookingDB import HotelBookingDB
import datetime
from datetime import datetime, timedelta

class RoomAvailability(object):
    def __init__(self):
        HotelBookingDB.initialize()
        self.initRoomBookingDateRange()
        #self.saveRoomAvailabilityToMongo()

    def initRoomBookingDateRange(self):
        roomBookingPeriodStartDate = datetime(2018, 1, 1)
        roomBookingPeriodStartDate = datetime.combine(roomBookingPeriodStartDate,datetime.min.time())
        roomBookingPeriodEndDate = datetime(2020, 1, 1)
        roomBookingPeriodEndDate = datetime.combine(roomBookingPeriodEndDate,datetime.min.time())
        self.bookingEndDate = datetime.combine(roomBookingPeriodEndDate, datetime.min.time())
        daysBetweenRoomBookingDates = (roomBookingPeriodEndDate +
                                       timedelta(days=1) - roomBookingPeriodStartDate).days
        datesBetweenRoomBookingDates = [roomBookingPeriodStartDate +
                                        timedelta(days=aDate) for aDate in range(daysBetweenRoomBookingDates)]
        return datesBetweenRoomBookingDates

    def getHotelBookingsCursor(self):
        #if HotelBookingDB.checkIfCollectionExists("HotelBookings") == False:
         #   print("HotelBookings collection does not exist")
        #else:
            # show bookings roomnumbers, startdate and enddate
        return HotelBookingDB.find("HotelBookings", {})

    def showAllHotelBookings(self):
        cursor = self.getHotelBookingsCursor()
        for doc in cursor:
            print(doc)



        #return HotelBookingDB.HotelBookings.find({})
        #{"CheckOutDate" : {"$gte" : datetime.today()}})
        #This returns all docs in the collection

   # def initRoomAvailabilityJson(self):
        #self.roomAvailabilityList = {}
        #self.roomAvailability = 'Y'
    #    id = 1
     #   for date in self.initRoomBookingDateRange():
      #      for roomNumber in range(1, 22):
       #         newDate = {"Date": date, "RoomNumber": roomNumber, "RoomAvailability": self.roomAvailability}
        #        self.roomAvailabilityList[str(id)] = newDate
         #       id += 1
        #return self.roomAvailabilityList

    #def saveRoomAvailabilityToMongo(self):
     #   HotelBookingDB.insert(collection='RoomAvailability', data=self.initRoomAvailabilityJson())



    #def updateRoomAvailabilityTo_N_
    # This will update the room availability to N for a defined date range, and room number

    #def cancelRoomBooking
    #This will update the room availability to Y for a defined date range due to a cancellation


