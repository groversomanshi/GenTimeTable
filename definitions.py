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
    def __init__(self, numDays, weekTotal):
        self.__numDays = int(numDays) #workings days per week
        self.__weekTotal = int(weekTotal) #total periods in a week
        self.__dayTotal = self.__weekTotal // self.__numDays #number of periods in a day

    #getter functions
    def getNumDays(self):
        return self.__numDays

    def getWeekTotal(self):
        return self.__weekTotal
    
    def getDayTotal(self):
        return self.__dayTotal

#class containing data about a teacher
class teacher:
    def __init__(self, name, employeeId, weekMax, weekMin, dayMax, dayMin):
        self.__name = name #teacher's name
        self.__employeeId = employeeId #teacher's employee id
        self.__subjects = list() #list to contain all subjects taught by the teacher
        self.__gradeSections = list() #list to contain all the grades and sections taught by the teacher
        self.__gradeSubjectPairs = dict() #dictionary to contain all the subjects taught for each class
        self.__weekMax = int(weekMax) #maximum periods allowed to be allotted in a week
        self.__weekMin = int(weekMin) #minimum periods allowed to be allotted in a week
        self.__dayMax = int(dayMax) #maximum periods allowed to be allotted in a day
        self.__dayMin = int(dayMin) #minimum periods allowed to be allotted in a day

    def __del__(self):
        print('Teacher with name', self.__name, 'deleted')

    #getter functions
    def getName(self):
        return self.__name
    
    def getEmployeeId(self):
        return self.__employeeId
    
    def getSubjects(self):
        return self.__subjects
    
    def getGradeSections(self):
        return self.__gradeSections
    
    def getGradeSubjectPairs(self):
        return self.__gradeSubjectPairs
    
    def getWeekMax(self):
        return self.__weekMax
    
    def getWeekMin(self):
        return self.__weekMin
    
    def getDayMax(self):
        return self.__dayMax
    
    def getDayMin(self):
        return self.__dayMin
    
    #setter functions
    def addNewSubject(self, newSubject):
        self.__subjects.append(newSubject)

    def addNewGradeSection(self, newGradeSection):
        self.__gradeSections.append(newGradeSection)

    def addNewGradeSubjectPair(self, newSubject, newGradeSection):
        self.__gradeSubjectPairs[newGradeSection] = newSubject