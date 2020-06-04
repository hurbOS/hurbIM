import sqlite3
import settings

class AddressDatabase(object):
    def __init__(self):
        db = sqlite3.connect(settings.db2)
        c = db.cursor()
        c.execute(
        "CREATE TABLE IF NOT EXISTS records\
            ( record_internal_id INTEGER PRIMARY KEY, \
              user_name     TEXT \
              )" \
            )
        db.commit()
        c.close()

    def add_record(self, user_name = ''):
        db = sqlite3.connect(settings.db2)
        c = db.cursor()
        c.execute('INSERT INTO records(user_name) \
                    VALUES(?)', (user_name, ))
        db.commit()
        c.close()

    def delete_record(self, record_id):
        db = sqlite3.connect(settings.db2)
        c = db.cursor()
        c.execute('DELETE FROM records where record_internal_id=?', (record_id,))
        db.commit()
        c.close()

    def list_all_records(self):
        db = sqlite3.connect(settings.db2)
        c = db.cursor()
        c.execute('SELECT * from records')
        records = c.fetchall()
        c.close()
        return records

    def user_get_record(self, record_id):
        db = sqlite3.connect(settings.db2)
        c = db.cursor()
        c.execute('SELECT user_name from records WHERE record_internal_id=?', (record_id,))
        records = c.fetchall()
        c.close()
        return records[0]
