# python HomepageController.py

import tkinter
from hotelBookingSystem.HomepageView import HomepageView
from hotelBookingSystem.BookingPageController import BookingPageController

class HomepageController():

	def __init__ (self):
		print("Homepage Controller Initiated")
		self.homepage = tkinter.Tk()
		self.initHomepageView()
		self.homepageActionOnMakeABooking()

	def initHomepageView(self):
		print("Homepage View Initiated")
		self.hotelHomepageView = HomepageView(self.homepage)

	def initBookingPageWindow(self):
		self.homepage.after(50,self.homepage.wm_withdraw())
		print("Booking Page Initiated")
		self.hotelBookingPageController = BookingPageController(self.homepage)
		
	def homepageActionOnMakeABooking(self):
		print("Homepage 'Make a Booking' Button Pressed")
		self.hotelHomepageView.homepageActionOnMakeABooking = self.initBookingPageWindow
		self.homepage.mainloop()