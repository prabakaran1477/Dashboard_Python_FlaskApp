from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import jsonify,json
import os
import time
from argus_v1.FlaskApp.helper import Authenticate,dashboard_data

app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if session.get('logged_in'):
            mydata  = json.loads(dashboard_data())
            # return render_template('dashboard.html',mydata = mydata)
            return render_template('data_publisher.html',mydata = mydata)
            # return render_template('dashboard.html')
        else:
            home()


@app.route('/login', methods=['POST'])
def do_admin_login():
    mycrd_user = request.form['uname']
    mycrd_pass = request.form['pword']
    login_confirmation = Authenticate(mycrd_user,mycrd_pass)
    if login_confirmation:
        if login_confirmation[1] == str(mycrd_user) and login_confirmation[2] == str(mycrd_pass):
            session['logged_in'] = True

            # result = request.form
            # return render_template("data_publisher.html", result=result)

        else:
            flash('Looks like entered worng password!!!')

    else:
        flash('Looks like entered worng password!!')

    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)

