import sqlite3
import sqlite3 as sl
from sqlite3 import Error

conn = sqlite3.connect('database.db')

c = conn.cursor()


c.execute('''CREATE TABLE teams
             (name text)''')

conn.commit()
newteams = ('TISA')

c.executemany('INSERT INTO teams VALUES (?)', newteams)


conn.commit()

conn.close()
