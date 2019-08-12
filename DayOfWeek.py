import unittest
import csv

def convertMonthToDays(month, year):
    # Days per month in regular year
    # Months are shifted so correct sum can be returned
    regYear = [0,31,59,90,120,151,181,212,243,273,304,334]
    sum = regYear[month-1]
    # check if year is a leap year
    if(year % 4 == 0 and month > 2):
        return sum + 1
    return sum

def formatDate(dayString):
    # formtat is "June 19, 2018"
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    comps = dayString.split(" ")
    for i in range(0,12):
        # Get month index
        if months[i] == comps[0]:
            # Keep entries consistent strings
            comps[0] = str(i + 1)
            break
    # Remove comma from string
    temp = comps[1].split(",")
    comps[1] = temp[0]
    return comps

def getDayOfWeek(dayString):
    dateComp = dayString.split("/")
    if(len(dateComp) == 1):
        dateComp = formatDate(dayString)
    # to compute, convert date to number of days (taking into account leap days)
    days = int(dateComp[1])
    monthDays = convertMonthToDays(int(dateComp[0]),int(dateComp[2]))
    yearDays = int(dateComp[2])
    # Check if there are less than 4 digits
    if(int(dateComp[2]) < 1000):
        yearDays = yearDays + 2000 
    yearDays = int(yearDays * 365.25)
    sum = yearDays + days + monthDays
    DayOfWk = ["Friday","Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday"]
    # Before february comes up a day later
    # After february comes a day too late
    year = int(dateComp[2])
    # if in a leap year
    if(year % 4 == 0):
        sum-=1
    index = sum % 7
    return DayOfWk[index]

def convertDates(dateArray):
    dayOfWeekArray = []
    for row in dateArray:
        dayOfWeekArray.append(getDayOfWeek(row[1]))
    return dayOfWeekArray

class TestStringMethods(unittest.TestCase):

    def test_getDayOfWeek(self):
        #["Friday","Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday"]
        
        self.assertEqual(getDayOfWeek("December 17, 1995"), "Sunday")
        self.assertEqual(getDayOfWeek("12/10/1995"), "Sunday")
        self.assertEqual(getDayOfWeek("12/11/1995"), "Monday")
        self.assertEqual(getDayOfWeek("12/12/1995"), "Tuesday")
        self.assertEqual(getDayOfWeek("12/13/1995"), "Wednesday")
        self.assertEqual(getDayOfWeek("12/14/1995"), "Thursday")
        self.assertEqual(getDayOfWeek("12/15/1995"), "Friday")
        self.assertEqual(getDayOfWeek("12/16/1995"), "Saturday")
        self.assertEqual(getDayOfWeek("12/17/1995"), "Sunday")
        self.assertEqual(getDayOfWeek("12/12/11"), "Monday")
        
        # Leap years returns day after?
        self.assertEqual(getDayOfWeek("March 17, 1992"), "Tuesday")
        self.assertEqual(getDayOfWeek("2/17/1992"), "Monday")
        self.assertEqual(getDayOfWeek("12/17/1992"), "Thursday")
        self.assertEqual(getDayOfWeek("12/12/12"), "Wednesday")
        self.assertEqual(getDayOfWeek("12/12/16"), "Monday")
        self.assertEqual(getDayOfWeek("2/12/16"), "Friday")


    def test_convertMonthsToDays(self):
        self.assertEqual(convertMonthToDays(1,1999), 0)
        self.assertEqual(convertMonthToDays(2,1999), 31)
        self.assertEqual(convertMonthToDays(3,1999), 59)
        self.assertEqual(convertMonthToDays(4,1999), 90)
        self.assertEqual(convertMonthToDays(5,1999), 120)
        self.assertEqual(convertMonthToDays(6,1999), 151)
        self.assertEqual(convertMonthToDays(7,1999), 181)
        self.assertEqual(convertMonthToDays(8,1999), 212)
        self.assertEqual(convertMonthToDays(9,1999), 243)
        self.assertEqual(convertMonthToDays(10,1999), 273)
        self.assertEqual(convertMonthToDays(11,1999), 304)
        self.assertEqual(convertMonthToDays(12,1999), 334)

        self.assertEqual(convertMonthToDays(1,2000), 0)
        self.assertEqual(convertMonthToDays(2,2000), 31)
        self.assertEqual(convertMonthToDays(3,2000), 60)
        self.assertEqual(convertMonthToDays(4,2000), 91)
        self.assertEqual(convertMonthToDays(5,2000), 121)
        self.assertEqual(convertMonthToDays(6,2000), 152)
        self.assertEqual(convertMonthToDays(7,2000), 182)
        self.assertEqual(convertMonthToDays(8,2000), 213)
        self.assertEqual(convertMonthToDays(9,2000), 244)
        self.assertEqual(convertMonthToDays(10,2000), 274)
        self.assertEqual(convertMonthToDays(11,2000), 305)
        self.assertEqual(convertMonthToDays(12,2000), 335)

    def test_FormatDate(self):
        self.assertEqual(formatDate("January 19, 2018"), ["1","19","2018"])
        self.assertEqual(formatDate("February 19, 2018"), ["2","19","2018"])
        self.assertEqual(formatDate("March 19, 2018"), ["3","19","2018"])
        self.assertEqual(formatDate("April 19, 2018"), ["4","19","2018"])
        self.assertEqual(formatDate("May 19, 2018"), ["5","19","2018"])
        self.assertEqual(formatDate("June 19, 2018"), ["6","19","2018"])
        self.assertEqual(formatDate("July 19, 2018"), ["7","19","2018"])
        self.assertEqual(formatDate("August 19, 2018"), ["8","19","2018"])
        self.assertEqual(formatDate("September 19, 2018"), ["9","19","2018"])
        self.assertEqual(formatDate("October 19, 2018"), ["10","19","2018"])
        self.assertEqual(formatDate("November 19, 2018"), ["11","19","2018"])
        self.assertEqual(formatDate("December 19, 2018"), ["12","19","2018"])


if __name__ == '__main__':
    unittest.main()
    '''
    with open('data1.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        #skip first line for headers
        next(readCSV)
        test = convertDates(readCSV)
        wtr = csv.writer(open ('out.csv', 'w'), delimiter=',', lineterminator='\n')
        for x in test : wtr.writerow ([x])  
        '''