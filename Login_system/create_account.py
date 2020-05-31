import sqlite3
from validation import *

db = sqlite3.connect("users.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS users (name TEXT PRIMARY KEY NOT NULL, password TEXT NOT NULL)")


class log_or_sig(object):
    def __init__(self, name=input("Please enter your user name: "), password=input("Now enter your password: ")):
        cursor = db.execute("SELECT * FROM users WHERE (name = ?) AND (password = ?)", (name, password))
        row = cursor.fetchone()

        if row:
            self.name, self._password = row
            print("Welcome {}, you logged in.".format(self.name), end='')
        else:
            self.name = name
            self._password = password
            if Authentication(name and password):
                cursor.execute("INSERT INTO users VALUES(?, ?)", (name, password))
                cursor.connection.commit()
                print("Account created for {}. ".format(self.name), end='')
            else:
                print("Account error")



ismael = log_or_sig()


db.close()
