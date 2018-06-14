
from flask import Flask,request
from flaskext.mysql import MySQL

from datetime import datetime
from json import dumps
import json


app = Flask(__name__)
app.debug = True

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = '#y5ql@M!n@2017'
app.config['MYSQL_DATABASE_DB'] = 'fundalytics'
app.config['MYSQL_DATABASE_HOST'] = 'CH1030BD04'
mysql.init_app(app)


def Authenticate(uname,pword):
    try:
        username = uname
        password = pword
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "' limit 1")
        data = cursor.fetchone()
        if data is None:
            return False
        else:
            return data
    except Exception as e:
        print('Error::LineNo-29::Message-',e)
        return False

def dashboard_data():
    try:
        cursor = mysql.connect().cursor()
        cursor.execute(" SELECT DataSourceID, DataSourceName,MarketName,ScraperPriority,TaskStatus,IsActive FROM scraperschedule")
        row_headers = [x[0] for x in cursor.description]
        rv = cursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        return json.dumps(json_data)

    except Exception as e:
        print('Error::LineNo-45::Message-',e)
        return False

