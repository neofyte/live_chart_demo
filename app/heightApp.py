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

def last_line_statement(tablename='first_pool'):
    return '''select * from {0} order by id desc limit 1'''.format(tablename)

def db_query():
    g.db = connect_db()
    database_cursor = g.db.cursor()
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

@app.route('/data')
def data_push():
    if request.method == 'GET':
        data = db_query()
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
        return response

if __name__ == '__main__':
    app.run()