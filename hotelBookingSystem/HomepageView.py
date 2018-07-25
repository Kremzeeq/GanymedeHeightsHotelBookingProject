# python HomepageView.py

import tkinter
from tkinter import *
#from tkinter import ttk

from PIL import Image, ImageTk

class HomepageView():

    def __init__(self, parent):
        self.parent = parent
        self.initHomepageWindow()
        self.parent.wm_state('zoomed') 
        self.initHomepageHeaderFrame()
        self.initHotelImageFrame()
        self.initHotelIntroFrame()
        self.initBookingButtonFrame()
        self.homepageActionOnMakeABooking = lambda : 1

    def initHomepageWindow(self):
        self.parent.title("Ganymede Heights | Homepage")
        self.parent.configure(background='deep sky blue')
        self.parent.columnconfigure(0, weight=10)

    def initHomepageHeaderFrame(self):
        self.homepageHeaderFrame = tkinter.Frame(self.parent)
        self.homepageHeaderImageFile = "hotelBookingSystem\\images\\canvaGanymedeHeightsBanner.png"
        self.homepageHeaderImage = ImageTk.PhotoImage(Image.open(self.homepageHeaderImageFile))
        self.homepageHeaderImageLabel = Label(self.homepageHeaderFrame, image=self.homepageHeaderImage)
        self.homepageHeaderImageLabel.configure(background="deep sky blue")

        self.homepageHeaderFrame.grid(row=0, column=0, sticky=N+S+E+W)
        self.homepageHeaderImageLabel.pack(side="top", fill="both", expand="yes")
        
    def initHotelImageFrame(self):
        self.hotelImageFrame = tkinter.Frame(self.parent)
        self.homepageHotelImageFile = "hotelBookingSystem\\images\\canvaGanymedeHeightsHotelfront.png"
        self.homepageHotelImage = ImageTk.PhotoImage(Image.open(self.homepageHotelImageFile))
        self.homepageHotelImageLabel = Label(self.hotelImageFrame, image=self.homepageHotelImage)
        self.homepageHotelImageLabel.configure(background="deep sky blue")

        self.hotelImageFrame.grid(row=1, column=0, sticky=N+S+E+W)
        self.homepageHotelImageLabel.pack(side="top", fill="both", expand="yes")

    def initHotelIntroFrame(self):
        self.hotelIntroFrame = Frame(self.parent)
        self.homepageIntroImageFile = "hotelBookingSystem\\images\\hotelIntroduction.png"
        self.homepageIntroImage = ImageTk.PhotoImage(Image.open(self.homepageIntroImageFile))
        self.homepageIntroImageLabel =  Label(self.hotelIntroFrame, image=self.homepageIntroImage)
        self.homepageIntroImageLabel.configure(background="deep sky blue")

        self.hotelIntroFrame.grid(row=2, column=0, sticky=N+S+E+W)
        self.homepageIntroImageLabel.pack(side="top", fill="both", expand="yes")

    def pressedMakeABooking(self):
        funcToCall = self.homepageActionOnMakeABooking
        funcToCall()

    def initMakeABookingButton(self):
        return Button(self.hotelBookingButtonFrame, text="Make a Booking",
                      command=lambda:self.pressedMakeABooking(), padx=20, bg="ivory1")

    def initBookingButtonFrame(self):
        self.hotelBookingButtonFrame = Frame(self.parent)
        self.hotelBookingButtonFrame.configure(background="deep sky blue")
        self.bookingPageOpeningButton = self.initMakeABookingButton()
        
        self.hotelBookingButtonFrame.grid(row=3, column=0, sticky=N+S+E+W)
        self.bookingPageOpeningButton.pack(pady=20, padx=20)
