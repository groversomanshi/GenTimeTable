from definitions import schoolStructure
import sqlite3
import re

#user inputs a file name for the database that can only contain alphanumeric characterics and underscores
while True:
    print('Enter the database file name')
    fileName = input('Only alphanumeric characters and underscores allowed: ').strip().lower()
    if re.fullmatch(r'\w+', fileName) is not None:
        break
file = fileName + '.sqlite'

#connecting to the database, creating a cursor to accss the database, and creating all the required tables
conn = sqlite3.connect(file)
cur = conn.cursor()
cur.executescript('''
                  CREATE TABLE IF NOT EXISTS SchoolStructure (numDays INTEGER, weekTotal INTEGER, dayTotal INTEGER);
                  CREATE TABLE IF NOT EXISTS Teachers (id TEXT NOT NULL PRIMARY KEY UNIQUE, name TEXT, weekMax INTEGER, weekMin INTEGER, dayMax INTEGER, dayMin INTEGER);
                  CREATE TABLE IF NOT EXISTS Subjects (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, subjectName TEXT UNIQUE);
                  CREATE TABLE IF NOT EXISTS Classes (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, grade INTEGER, section TEXT);
                  CREATE TABLE IF NOT EXISTS TeacherSubjects (teacherId TEXT, subjectId INTEGER, PRIMARY KEY(teacherId, dubjectId));
                  CREATE TABLE IF NOT EXISTS SubjectClasses (classId INTEGER, subjectId INTEGER, teacherId TEXT, weekPeriods INTEGER, dayPeriods INTEGERS, PRIMARY KEY(classId, subjectId, teacherId));
                  ''')

#adding new School Structure as an object of class schoolStructure and in the database table
if input('Type YES to fill School Structure: ').strip() == 'YES'.upper():
    cur.execute('SELECT COUNT(*) FROM SchoolStructure')
    if cur.fetchone()[0] > 0:
        print('Error. SchoolStructure already exists.')
    else:
        print('Enter numDays, weekTotal')
        numDays, weekTotal = map(int, input('E.g. 5, 40: ').split(','))
        structure = schoolStructure(numDays, weekTotal)
        cur.execute('INSERT INTO SchoolStructure (numDays, weekTotal, dayTotal) VALUES (?, ?, ?)', (structure.getNumDays(), structure.getWeekTotal(), structure.getNumDays()))