from sqlite3 import dbapi2 as sqlite3

def connect_db():
    return sqlite3.connect('memo.db')