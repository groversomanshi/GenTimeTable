from enum import Enum

#enumerated list containing the days of the week
class Days(Enum):
    Monday=1
    Tuesday=2
    Wednesday=3
    Thursday=4
    Friday=5
    Saturday=6
    Sunday=7

#class containing data about the school's week structure
class schoolStructure:
    def __init__(self, weekTotal, numDays):
        self.__weekTotal = int(weekTotal) #total periods in a week
        self.__numDays = int(numDays) #workings days per week
        self.__dayTotal = self.__weekTotal // self.__numDays #number of periods in a day

    def getWeekTotal(self):
        return(self.__weekTotal)
    
    def getNumDays(self):
        return(self.__numDays)
    
    def getDayTotal(self):
        return(self.__dayTotal)