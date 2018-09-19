# Ganymede Heights: Hotel Booking Project

<h1 align="center">
  <img src="https://github.com/Kremzeeq/GanymedeHeightsHotelBookingProject/blob/master/hotelBookingSystem/images/portfolio_prototype_image.png" alt="Prototype_intro" />
</h1>

**Ganymede Heights** is an example of front and back-end python development with an integrated Mongo DB database. 
The application simulates a user-browser experience from the point of homepage discovery for a fictional ice hotel website based in Antarctica

## Front-end Features

**1) Hotel Homepage**: Clicking the ‘Make a Booking’ button  takes the user to the booking page

**2) Hotel Booking Page**: Here, the user can select various booking choices. Clicking ‘Check Booking Dates’ prompts various checks e.g. if the booking end date is earlier than the start date, the warning box message will change

**3) Room Details Page**: On this page the user can review booking choices and proceed to press ‘Confirm Booking and Payment’. This prompts a new message box with the room number and booking reference.  The user can also save a png image of the booking

-Disclaimer: There is no integrated Flask module for an online database development environment. The application does not harvest any personally identifiable information nor does it process any real-life payment transactions.

## Prototype Demo

- An Adobe XDCC Demo of the application, simulating the user journey for booking a hotel is available here:
https://adobe.ly/2LkmfkB

## Poster

- Click <a href="https://github.com/Kremzeeq/GanymedeHeightsHotelBookingProject/blob/master/GanymedeHeightsPoster.pdf">here</a> to view project poster with pictorial ReadMe information and project challenges e.g. through using TKinter.

## Project Tools
 
 <h2 align="center">
  <img src="https://github.com/Kremzeeq/GanymedeHeightsHotelBookingProject/blob/master/hotelBookingSystem/images/wordcloud.png" alt="Wordcloud" />
 </h2>

## Project Set-Up

- Module pre-requisites are found in the <a href="https://github.com/Kremzeeq/GanymedeHeightsHotelBookingProject/blob/master/requirements.txt">requirements.txt</a> file
- Opening the project in PyCharm should prompt for modules from the file to be installed
- Alternatively use **pip install** for requirements.txt in the command line

## MongoDB Database Set-Up

- Mongo DB Community Edition 4.0 was installed for this project
- Manual for installing MongoDB on Linux, macOS and Windows is available here:
https://docs.mongodb.com/manual/administration/install-community/

## Initialising the MongoDB Database

- Once MongoDB has been configured to preferences, ensure **mongod**, the MongoDB daemon, has been typed into the command line.
- In a separate command line, enter the following in order:
  1. mongo
  2. use HotelBookingDB
  3. db.createCollection(‘HotelBookings’)

-The ‘HotelBookings’ collection needs to be created prior to running the python application as it will query any precious bookings in the collection

## Initialising the Python application

- The application can be run from the hotelProjectMain.py file
- Please note that the JSON for the hotel booking is saved to the database at the point that the ‘Confirm Booking and Button’ payment is pressed. All bookings saved in the database will be displayed in the shell
- When the ‘Save Booking Details’ button is pressed a hotelBooking.png file is saved to the project root folder when the ‘Save Booking  Details’ button is pressed. This returns a screenshot of the page.

**Copyright: Sian Thompson (Kremzeeq)**

Author Email: sian.thompson@gmx.co.uk
