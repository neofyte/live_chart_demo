import sqlite3, os, json, time
from datetime import datetime
from flask import Flask, request, g, redirect, url_for, abort, render_template, flash, make_response

DATABASE='data/poolheight.db'
DEBUG=True

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template')
#stc_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

app = Flask(__name__, template_folder=tmpl_dir)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

<<<<<<< HEAD
def last_line_statement(tablename='first_pool'):
    return '''select * from {0} order by id desc limit 1'''.format(tablename)
=======
def select_last_statement(tablename='first_pool', line_number = 1):
    return '''select * from {0} order by id desc limit {1}'''.format(tablename, line_number)
>>>>>>> 2444afc9fd6cf72e9ff2ac190207ace364e5d16c

def db_query():
    g.db = connect_db()
    database_cursor = g.db.cursor()
<<<<<<< HEAD
    database_cursor.execute(last_line_statement('first_pool'))
    id, measure_time, height = database_cursor.fetchone()
    time_object = time.strftime("%Y %m %d,%H:%M:%S",\
                time.strptime(measure_time, '%Y-%m-%d %H:%M:%S')\
        )
    g.db.close()
    return [time_object, height]


@app.route('/')
def main():
    return render_template('main.html')
=======
    database_cursor.execute(select_last_statement('first_pool', 10))
    #data_group is a list whose items are [id, measure_time,height]
    data_group = database_cursor.fetchall()
    data_cleaned = []

    for item in data_group:
        id, measure_time, height = item
        time_object = time.strftime("%b %d %Y %H:%M:%S",
                    time.strptime(measure_time, '%Y-%m-%d %H:%M:%S')
        )
        measure_time = time_object
        data_cleaned.append([id, measure_time, height])

    g.db.close()
    return data_cleaned

@app.route('/')
def main():
    return render_template('main_highcharts.html')
>>>>>>> 2444afc9fd6cf72e9ff2ac190207ace364e5d16c

@app.route('/data')
def data_push():
    if request.method == 'GET':
        data = db_query()
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
        return response

if __name__ == '__main__':
<<<<<<< HEAD
    app.run()
=======
    app.run(host='0.0.0.0')
>>>>>>> 2444afc9fd6cf72e9ff2ac190207ace364e5d16c
