import sqlite3, os, json, time
from datetime import datetime

DATABASE='data/poolheight.db'

def connect_db():
    return sqlite3.connect(DATABASE)

def select_last_statement(tablename='first_pool', line_number = 1):
    return '''select * from {0} order by id desc limit {1}'''.format(tablename, line_number)

def db_query():
    db = connect_db()
    database_cursor = db.cursor()
    database_cursor.execute(select_last_statement('first_pool', 10))
    #data_group is a list whose items are [id, measure_time,height]
    data_group = database_cursor.fetchall()
    # id, measure_time, height
    #time_object = time.strftime("%Y %m %d,%H:%M:%S",\
    #            time.strptime(measure_time, '%Y-%m-%d %H:%M:%S')\
    #    )
    db.close()
    return data_group

if __name__=='__main__':
    db_query()