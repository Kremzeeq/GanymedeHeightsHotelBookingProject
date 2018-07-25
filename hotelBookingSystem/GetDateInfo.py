# python GetDateInfo.py

import datetime
import calendar
 
class GetDateInfo():

    def __init__(self):
        self.now = datetime.datetime.now()
        self.dateNow =datetime.date.today()
        self.currentDay = self.now.day
        self.currentMonth = self.now.month
        self.currentYear = self.now.year
        self.dateNow = datetime.date.today()

    def datetimeDatetimeObForNow(self):
        # make the datetime object set with 0, 0,0 for minutes etc.
        return datetime.datetime(self.currentYear,self.currentMonth,self.currentDay,0,0,0)

    def yearList(self):
        nextYear = self.currentYear + 1
        self.yearsToSelect = [self.currentYear,nextYear]
        return self.yearsToSelect

    def getMonthListForCurrentYear(self):
        return [month for month in calendar.month_name[self.currentMonth:]]

    def getMonthListForNextYear(self):
        return [month for month in calendar.month_name[1:]]
 
    def getDaysForCurrentYearAndSelectedMonth(self,selectedYear,selectedMonth):
        self.monthsInYear = self.getMonthListForNextYear()
        selectedMonthInt = self.monthsInYear.index(selectedMonth) + 1

        if selectedYear == int(self.now.year) and selectedMonthInt == int(self.now.month):
            firstDayOfMonth = self.now.day
        else:
            firstDayOfMonth = 1

        calendarMonthRange = calendar.monthrange(int(selectedYear),selectedMonthInt)     
        lastDayOfMonth = calendarMonthRange[1]
        
        daysToSelect = list(range(firstDayOfMonth,int(lastDayOfMonth)+1))
        daysToSelect1 = '\n'.join(str(x) for x in daysToSelect)
        return str(daysToSelect1)

    def getDateForSelectedDayMonthandYear(self, selectedYear, selectedMonth, selectedDay):
        monthsInYear = self.getMonthListForNextYear()
        selectedMonthInt = monthsInYear.index(selectedMonth) + 1
        return datetime.date(int(selectedYear), selectedMonthInt, int(selectedDay))

    def convertDateObjectToUKFormat(self, userDefinedDate):
        self.userDefinedDate = userDefinedDate
        self.userDefinedDate = str(datetime.datetime.date(self.userDefinedDate))
        return datetime.datetime.strptime(self.userDefinedDate, "%Y-%m-%d").strftime("%d/%m/%Y")
