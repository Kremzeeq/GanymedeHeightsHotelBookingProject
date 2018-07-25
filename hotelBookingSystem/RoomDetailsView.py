# python RoomDetailsController.py

import tkinter
from tkinter import *
from PIL import Image, ImageTk
from hotelBookingSystem.GetDateInfo import GetDateInfo

class RoomDetailsView():

    def __init__(self,roomDetailsWindow,userBookingChoices,roomTypeList,roomPriceInfo):
        self.roomDetailsWindow = roomDetailsWindow
        self.roomDetailsWindow.wm_state('zoomed') 
        self.actionOnConfirmingPayment = lambda: 1
        self.actionOnSavingDetails = lambda: 1
        self.initRoomDetailsPage()
        self.initRoomDetailsHeaderFrame()
        self.initRoomDetailsOutputFrame()
        self.userBookingChoices = userBookingChoices
        self.roomTypeList = roomTypeList
        self.initRoomImageInRoomDetailsOutputFrame()
        self.initSpacingLabel()
        self.initSearchResultsHeadingLabel()
        self.roomPriceInfo = roomPriceInfo
        self.initRoomPriceInfoLabel()
        self.initPaymentConfirmationFrame()

    def initRoomDetailsPage(self):
        self.roomDetailsWindow.title("Ganymede Heights | Confirm Room Details")
        self.roomDetailsWindow.configure(background="deep sky blue")
        self.roomDetailsWindow.columnconfigure(0, weight=1)
      
    def initRoomDetailsHeaderFrame(self):
        self.roomDetailsHeaderFrame = tkinter.Frame(self.roomDetailsWindow)
        self.roomDetailsHeaderFrame.grid(row=0, column=0, sticky=N+S+E+W)

        self.roomDetailsHeaderImageFile = "hotelBookingSystem\\images\\canvaMakeABookingBanner.png"
        self.roomDetailsHeaderImage = ImageTk.PhotoImage(Image.open(self.roomDetailsHeaderImageFile))
        self.roomDetailsHeaderImageLabel = Label(self.roomDetailsHeaderFrame, image=self.roomDetailsHeaderImage)
        
        self.roomDetailsHeaderImageLabel.pack(side="top", fill="both", expand="yes")
        self.roomDetailsHeaderImageLabel.configure(background="deep sky blue")

    def initRoomDetailsOutputFrame(self):
        print("In Room Details Output frame")
        self.roomDetailsOutputFrame = tkinter.Frame(self.roomDetailsWindow)
        self.roomDetailsOutputFrame.grid(row=1, column=0, sticky=N+S+E+W)

        self.roomDetailsBackgroundImageFilename  = ImageTk.PhotoImage(Image.open("hotelBookingSystem\\images\\roomDetailsBackground.png"))
        self.roomDetailsBackgroundLabel = tkinter.Label(self.roomDetailsOutputFrame, image=self.roomDetailsBackgroundImageFilename)
        self.roomDetailsBackgroundLabel.configure(background='deep sky blue')
        self.roomDetailsBackgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)

    def returnRoomImageFileName(self):
        self.roomImageFiles = ["single.png","double.png","king.png","penthouse.png"]
        self.roomTypeChoice = self.userBookingChoices.get("RoomTypeChoice")
        imageFileLocation = "hotelBookingSystem\\images\\"
        imageCounter = 0
        
        for roomType in self.roomTypeList:
            if roomType == self.roomTypeChoice:
                return imageFileLocation + self.roomImageFiles[imageCounter]
            imageCounter += 1

    def initRoomImageInRoomDetailsOutputFrame(self):
        roomImageFile = self.returnRoomImageFileName()
        self.roomDetailsRoomImageFilename  = ImageTk.PhotoImage(Image.open(roomImageFile))
        self.roomDetailsRoomImageLabel = tkinter.Label(self.roomDetailsOutputFrame, image=self.roomDetailsRoomImageFilename)
        self.roomDetailsRoomImageLabel.pack(side=LEFT,padx=180, pady=10)

    def initSearchResultsHeadingLabel(self):
        self.numberOfAdultsChoice = self.userBookingChoices.get("NumberOfAdultsChoice")
        self.roomTypeChoice = self.userBookingChoices.get("RoomTypeChoice")
        self.numberOfNights = self.userBookingChoices.get("NumberOfNights")
        bookingStartDate= self.userBookingChoices.get("CheckInDate")
        bookingEndDate = self.userBookingChoices.get("CheckOutDate")
        self.getDateInfo = GetDateInfo()
        self.ukFormatBookingStartDate = self.getDateInfo.convertDateObjectToUKFormat(bookingStartDate)
        self.ukFormatBookingEndDate = self.getDateInfo.convertDateObjectToUKFormat(bookingEndDate)

        self.roomDetailsSearchResultsHeadingLabel = Label(self.roomDetailsOutputFrame, text=
        "\n   SEARCH RESULTS   \n\n"  "   Number of Adults: %s   |  Room Type: %s   \n\n   Number of Nights: %s  \t\t\t\t\t\t"
        "   Check In: %s   |   Check Out: %s   \t\t\t\t\t\t\t\n" % (self.numberOfAdultsChoice, self.roomTypeChoice,
                                                      self.numberOfNights,self.ukFormatBookingStartDate,
                                                      self.ukFormatBookingEndDate),bg='ivory1', fg="ivory4")
        self.roomDetailsSearchResultsHeadingLabel.config(font=("Helvetica", "12"))
        self.roomDetailsSearchResultsHeadingLabel.pack(side=TOP,padx=80, pady=10, fill=BOTH)

    def initRoomPriceInfoLabel(self):
        self.roomPricePerNight = self.roomPriceInfo.get("RoomPricePerNight")
        self.roomPriceForNumberOfNights = self.roomPriceInfo.get("RoomPricePerNightForNumberOfNights")
        self.roomDetailsPriceInfoLabel = Label(self.roomDetailsOutputFrame, text= "\n   Room Price per Night: £%s   |  Total Cost: £%s   \n" % (self.roomPricePerNight, self.roomPriceForNumberOfNights ),bg='ivory1', fg="ivory4")
        self.roomDetailsPriceInfoLabel.config(font=("Helvetica", "12"))
        self.roomDetailsPriceInfoLabel.pack(side=BOTTOM,padx=80, pady=10, fill=BOTH)

    def initSpacingLabel(self):
        self.spacingLabel = Label(self.roomDetailsOutputFrame, text="\t\t\t",background ="deep sky blue")
        self.spacingLabel.pack(side=RIGHT)

    def pressedConfirmPayment(self):    
        funcToCall = self.actionOnConfirmingPayment
        funcToCall()

    def hotelPaymentConfirmationButton(self,frame):
        return Button(frame, text="Confirm Booking and Payment", command=lambda:
        self.pressedConfirmPayment(), padx=20, bg="ivory1")
    
    def initPaymentConfirmationFrame(self):
        self.roomDetailsConfirmationFrame = tkinter.Frame(self.roomDetailsWindow)
        self.roomDetailsConfirmationFrame.configure(background="deep sky blue")
        self.paymentConfirmationButton=self.hotelPaymentConfirmationButton(self.roomDetailsConfirmationFrame)

        self.roomDetailsConfirmationFrame.grid(row=2, column=0, sticky=N+S+E+W)
        self.paymentConfirmationButton.pack(pady=20, padx=20)

    def initBookingPaymentMessage(self,bookingRoomNumber,bookingReferenceID):
        self.paymentConfirmationMessageLabel = Label(
            self.roomDetailsConfirmationFrame, text= "\n Thank you for your booking. "
                                                     "Here are the Check-In Details: \n\n Room number: %s "
                                                     "\tBooking Reference: %s \n" %
                                                     (bookingRoomNumber, bookingReferenceID), bg='ivory1', fg="ivory4")
        self.paymentConfirmationMessageLabel.config(font=("Helvetica", "12"))
        self.paymentConfirmationMessageLabel.pack(side=TOP, padx=170, pady=10, fill=BOTH, expand=YES)

    def pressedSaveBookingDetails(self):
        funcToCall = self.actionOnSavingDetails
        funcToCall()

    def saveHotelBookingDetailsButton(self,frame):
        return Button(frame, text="Save Booking Details",
                      command=lambda : self.pressedSaveBookingDetails(), padx=20, bg="ivory1")

    def initSaveBookingDetailsFrame(self):
        self.saveBookingDetailsFrame = tkinter.Frame(self.roomDetailsWindow)
        self.saveBookingDetailsFrame.configure(background = "deep sky blue")
        self.saveBookingDetailsButton = self.saveHotelBookingDetailsButton(self.saveBookingDetailsFrame)

        self.saveBookingDetailsFrame.grid(row=3, column=0, sticky=N+S+E+W)
        self.saveBookingDetailsButton.pack(pady=20, padx=20)

    def initImageGrabFrame(self):
        self.imageGrabMessageFrame = tkinter.Frame(self.roomDetailsWindow)
        self.imageGrabMessageFrame.configure(background="deep sky blue" )
        self.imageGrabMessageLabel = Label(self.imageGrabMessageFrame, text=
        "\n Booking details have been saved in a bookingDetails.png file\n",
                                           bg='ivory1', fg="ivory4")
        self.imageGrabMessageLabel.config(font=("Helvetica", "12"))

        self.imageGrabMessageFrame.grid(row=4, column=0, sticky=N+S+E+W)
        self.imageGrabMessageLabel.pack(side=TOP, padx=170, pady=10, fill=BOTH, expand=YES)

    
