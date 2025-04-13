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
                  CREATE TABLE IF NOT EXISTS Teachers (id TEXT NOT NULL PRIMARY KEY UNIQUE, name TEXT, weekMax INTEGER, weekMin INTEGER, dayMax INTEGER, dayMin INTEGER);
                  CREATE TABLE IF NOT EXISTS Subjects (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, subjectName TEXT UNIQUE);
                  CREATE TABLE IF NOT EXISTS Classes (id INNTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, grade INTEGER, section TEXT);
                  CREATE TABLE IF NOT EXISTS TeacherSubjects (teacherId TEXT, subjectId INTEGER, PRIMARY KEY(teacherId, dubjectId));
                  CREATE TABLE IF NOT EXISTS SubjectClasses (classId INTEGER, subjectId INTEGER, teacherId TEXT, weekPeriods INTEGER, dayPeriods INTEGERS, PRIMARY KEY(classId, subjectId, teacherId));
                  ''')