
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

def scraper_count():
    try:
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT COUNT(DataSourceID) AS All_Scrapers, (SELECT COUNT(DataSourceID) FROM scraperschedule WHERE isActive IN ('y','Y')) AS active_status,(SELECT COUNT(DataSourceID) FROM scraperschedule WHERE isActive IN ('y','Y') AND Taskstatus NOT IN ('Idle','Error')) AS running_status,(SELECT COUNT(DataSourceID) FROM scraperschedule WHERE isActive IN ('y','Y') AND Taskstatus NOT IN ('Error')) AS error_status,(SELECT COUNT(DataSourceID)  FROM scraperschedule WHERE isActive IN ('n','N')) AS inactive_status FROM scraperschedule")
        row_headers = [x[0] for x in cursor.description]
        rv = cursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        print(json_data)
        return json.dumps(json_data)

    except Exception as e:
        print('Error:dashboard_data:',e)
        return False

def dashboard_data():
    try:
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT DataSourceID, DataSourceName,MarketName,ScraperPriority,TaskStatus,DATE_FORMAT(ExecutionStartDateTime, '%d-%m-%Y %H:%i:%s') AS ExecutionStartDateTime,DATE_FORMAT(ExecutionEndDateTime, '%d-%m-%Y %H:%i:%s') AS ExecutionEndDateTime,ExecutionFrequencyMinutes,DATE_FORMAT(NextExecutionStartDateTime, '%d-%m-%Y %H:%i:%s') AS NextExecutionStartDateTime FROM scraperschedule")
        row_headers = [x[0] for x in cursor.description]
        rv = cursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        return json.dumps(json_data)

    except Exception as e:
        print('Error:dashboard_data:',e)
        return False

def active_status():
    try:
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT DataSourceID, DataSourceName,MarketName,ScraperPriority,TaskStatus,DATE_FORMAT(ExecutionStartDateTime, '%d-%m-%Y %H:%i:%s') AS ExecutionStartDateTime,DATE_FORMAT(ExecutionEndDateTime, '%d-%m-%Y %H:%i:%s') AS ExecutionEndDateTime,ExecutionFrequencyMinutes,DATE_FORMAT(NextExecutionStartDateTime, '%d-%m-%Y %H:%i:%s') AS NextExecutionStartDateTime  FROM scraperschedule WHERE isActive IN ('y','Y')")
        row_headers = [x[0] for x in cursor.description]
        rv = cursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        return json.dumps(json_data)

    except Exception as e:
        print('Error:active_status:',e)
        return False


def running_status():
    try:
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT DataSourceID, DataSourceName,MarketName,ScraperPriority,TaskStatus,DATE_FORMAT(ExecutionStartDateTime, '%d-%m-%Y %H:%i:%s') AS ExecutionStartDateTime,DATE_FORMAT(ExecutionEndDateTime, '%d-%m-%Y %H:%i:%s') AS ExecutionEndDateTime,ExecutionFrequencyMinutes,DATE_FORMAT(NextExecutionStartDateTime, '%d-%m-%Y %H:%i:%s') AS NextExecutionStartDateTime  FROM scraperschedule WHERE isActive IN ('y','Y') AND Taskstatus NOT IN ('Idle','Error')")
        row_headers = [x[0] for x in cursor.description]
        rv = cursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        return json.dumps(json_data)

    except Exception as e:
        print('Error:running_status:',e)
        return False

def error_status():
    try:
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT DataSourceID, DataSourceName,MarketName,ScraperPriority,TaskStatus,DATE_FORMAT(ExecutionStartDateTime, '%d-%m-%Y %H:%i:%s') AS ExecutionStartDateTime,DATE_FORMAT(ExecutionEndDateTime, '%d-%m-%Y %H:%i:%s') AS ExecutionEndDateTime,ExecutionFrequencyMinutes,DATE_FORMAT(NextExecutionStartDateTime, '%d-%m-%Y %H:%i:%s') AS NextExecutionStartDateTime  FROM scraperschedule WHERE isActive IN ('y','Y') AND Taskstatus NOT IN ('Error')")
        row_headers = [x[0] for x in cursor.description]
        rv = cursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        return json.dumps(json_data)

    except Exception as e:
        print('Error:error_status:',e)
        return False

def inactive_status():
    try:
        cursor = mysql.connect().cursor()
        cursor.execute("SELECT DataSourceID, DataSourceName,MarketName,ScraperPriority,TaskStatus,DATE_FORMAT(ExecutionStartDateTime, '%d-%m-%Y %H:%i:%s') AS ExecutionStartDateTime,DATE_FORMAT(ExecutionEndDateTime, '%d-%m-%Y %H:%i:%s') AS ExecutionEndDateTime,ExecutionFrequencyMinutes,DATE_FORMAT(NextExecutionStartDateTime, '%d-%m-%Y %H:%i:%s') AS NextExecutionStartDateTime  FROM scraperschedule WHERE isActive IN ('n','N')")
        row_headers = [x[0] for x in cursor.description]
        rv = cursor.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        return json.dumps(json_data)

    except Exception as e:
        print('Error:inactive_status:',e)
        return False

