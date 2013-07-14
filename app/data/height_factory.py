import os, sqlite3, time
from datetime import datetime

#a little bigger than the size of a line in the csv
READ_BULKSIZE = 40

#same as the write interval in simulator.py
READ_INTERVAL = 30

#dbname
DATABASENAME = 'poolheight'
TABLENAME = 'first_pool'

#if there exists multiple tables, these statements should be modified to funcitons
#db insert statement
INSERT_STATEMENT = ''.join(['INSERT INTO ', TABLENAME, ' (datetime, height) VALUES (?,?)'])

#db create table statement
CREATE_STATEMENT = ''.join(['CREATE TABLE ', TABLENAME, 
    ' (id integer primary key autoincrement, datetime text, height real)'])

#db select statement
SELECT_STATEMENT = ''.join(['SELECT datetime, height FROM ', TABLENAME])

#the database path
DBPATH = os.path.abspath(''.join([DATABASENAME, '.db']))

#the csv file path
FILEPATH = os.path.abspath('egg.csv')

class height_factory():
    '''height_factory reads the last line of the csv file on FILEPATH 
    and write it to the database on DBPATH.'''
    
    #read the last line of the file
    #the list returned consists of a datetime object and a string
    def csvfilereader(self, filepath=FILEPATH, read_size=READ_BULKSIZE):
        with open(filepath, 'rb') as csvfile:
            csvfile.seek(-read_size,2)
            #last line eg. 18/04/2013 13:28,178.301
            bottom_lines = csvfile.read(read_size)
            last_line = bottom_lines.split(b'\n')[1]
            measure_time, height = last_line.strip().split(b',')
            #datetime object eg. datetime.datetime(2013, 4, 18, 13, 28)
            #TODO: %S to be removed in production
            time_cleaned = datetime.strptime(measure_time.decode('utf-8'), '%d/%m/%Y %H:%M:%S')
            height_cleaned = height.decode('utf-8')
            return time_cleaned, height_cleaned
        
    #push the data into a database, sqlite3 for now
    def sqlite3_writer(self, measure_time=datetime.now(), height=0.0, dbpath=DBPATH):
        #time eg. '16/04/2013 15:16'
        #TODO: %S to be removed in production
        #create a string object of format 'yyyy-mm-dd hh:mm:ss' suited to the format of mysql
        time_cleaned = datetime.strftime(measure_time, '%Y-%m-%d %H:%M:%S')
        conn = sqlite3.connect(dbpath)
        c = conn.cursor()
        try:
            c.execute(CREATE_STATEMENT)
        except:
            pass
        c.execute(INSERT_STATEMENT, 
                  (time_cleaned, height))
        conn.commit()
        c.close()
        
if __name__=='__main__':
    ht_gen = height_factory()
    try:
        while True:
            measure_time, height = ht_gen.csvfilereader()
            ht_gen.sqlite3_writer(measure_time, height)
            conn = sqlite3.connect(DBPATH)
            c = conn.cursor()
            c.execute(SELECT_STATEMENT)
            a = c.fetchone()
            c.close()
            print(a)
            time.sleep(READ_INTERVAL)
    except KeyboardInterrupt:
        c.close()
        print('stop')
    