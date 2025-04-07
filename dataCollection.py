from definitions import schoolStructure
import sqlite3
import re

while True:
    print('Enter the database file name')
    fileName = input('Only alphanumeric characters and underscore allowed: ').strip().lower()
    if re.fullmatch(r'\w+', fileName) is not None:
        break
file = fileName + '.sqlite'
