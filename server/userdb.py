import sqlite3
import configure
class UserDatabase(object):
    def __init__(self):
        db = sqlite3.connect(configure.dbfilename2)
        c = db.cursor()
        c.execute(
        "CREATE TABLE IF NOT EXISTS records\
            ( record_internal_id INTEGER PRIMARY KEY, \
              user          TEXT, \
              passw         TEXT  \
              )" \
            )
        db.commit()
        c.close()

    def add_record(user='', passw=''):
        db = sqlite3.connect(configure.dbfilename2)
        c = db.cursor()
        c.execute('INSERT INTO records(user,passw) \
                    VALUES(?,?)', (user,passw))
        db.commit()
        c.close()

    def get_record(username):
        db = sqlite3.connect(configure.dbfilename2)
        c = db.cursor()
        c.execute('SELECT user,passw from records WHERE user=?', (username, ))
        records = c.fetchall()
        c.close()
        return records

    def get_precord(password):
        db = sqlite3.connect(configure.dbfilename2)
        c = db.cursor()
        c.execute('SELECT user,passw from records WHERE passw=?', (password, ))
        records = c.fetchall()
        c.close()
        return records

    def get_records():
        db = sqlite3.connect(configure.dbfilename2)
        c = db.cursor()
        c.execute('SELECT * from records')
        records = c.fetchall()
        c.close()
        return records
