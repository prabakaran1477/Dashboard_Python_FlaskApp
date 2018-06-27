from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import jsonify,json
from flask_login import LoginManager
import os
import time
from argus_v1.FlaskApp.helper import *

app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        session.clear()
        return render_template('login.html')
    else:
        mydata = json.loads(dashboard_data())
        return render_template('data_publisher.html',mydata = mydata)
        # return render_template('dashboard.html')



def home_page():
    if not session.get('logged_in'):
        return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    mycrd_user = request.form['uname']
    mycrd_pass = request.form['pword']
    login_confirmation = Authenticate(mycrd_user,mycrd_pass)

    if login_confirmation:
        # if login_confirmation[1] == str(mycrd_user) and login_confirmation[2] == str(mycrd_pass):
        session['logged_in'] = True
        session['username'] = request.form['uname']

        headers = {'content-type': 'application/json'}
        # result = request.form
        # return render_template("data_publisher.html", result=result)
        # else:
        #     flash('Access Denied, Contact Admin!!!')
    else:
        flash('Access Denied, Contact Admin!!')
    return home()

@app.route("/menu1", methods=['POST','GET'])
def dashboard_data_tabs1():
    try:
        if session.get('logged_in'):
            mydata = json.loads(active_status())
            return render_template('tab1.html', active_status=mydata)
            # return render_template('dashboard.html')
        else:
            home_page()
    except Exception as e:
        print('dashboard_data_tabs1:',e)
        home_page()

@app.route("/menu2", methods=['POST','GET'])
def dashboard_data_tabs2():
    try:
        if session.get('logged_in'):
            mydata = json.loads(running_status())
            return render_template('tab2.html', running_status=mydata)
            # return render_template('dashboard.html')
        else:
            home_page()
    except Exception as e:
        print('dashboard_data_tabs2:',e)
        home_page()

@app.route("/menu3", methods=['POST','GET'])
def dashboard_data_tabs3():
    try:
        if session.get('logged_in'):
            mydata = json.loads(error_status())
            return render_template('tab3.html', error_status=mydata)
            # return render_template('dashboard.html')
        else:
            home_page()
    except Exception as e:
        print('dashboard_data_tabs3:',e)
        home_page()

@app.route("/menu4", methods=['POST','GET'])
def dashboard_data_tabs4():
    try:
        if session.get('logged_in'):
            mydata = json.loads(inactive_status())
            return render_template('tab4.html', inactive_status=mydata)
            # return render_template('dashboard.html')
        else:
            home_page()
    except Exception as e:
        print('dashboard_data_tabs4:',e)
        home_page()

@app.route("/logout")
def logout():
    session.pop('uname', None)
    session['logged_in'] = False
    session.clear()
    return home_page()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=False)

