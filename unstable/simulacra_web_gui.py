from flask import Flask, request, redirect, make_response, render_template
import jwt
import datetime
from config import *

app = Flask(__name__)


# The root directory for the website. The user will only be redirected here if no cookie is active.
@app.route('/')
def home():
    return render_template('login.html')


# The POST request for getting the username and password.
@app.route('/login', methods=['POST'])
def login():

    # Get the information from the user.
    username = request.form.get('username')
    password = request.form.get('password')
    if username in users and users[username] == password:

        # If the username and password is correct, generate a encrypted with the secret key.
        token = jwt.encode({
            'user': username,
            'group': groups[username],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
        }, secret_key, algorithm='HS256')
        resp = make_response(redirect('/update'))
        resp.set_cookie('token', token)
        return resp
    return redirect('/')


# The main landing page for a user that successfully logged into to the website.
@app.route('/update')
def main():
    token = request.cookies.get('token')

    # Send user back to root if no cookie is active.
    if not token:
        return redirect('/')
    try:
        data = jwt.decode(token, secret_key, algorithms=['HS256'])
        is_admin = data["group"] == "admin"
        return render_template('update.html', user=data["user"], group=data["group"], is_admin=is_admin)
    except jwt.ExpiredSignatureError:
        return 'Session expired!', 403
    except jwt.InvalidTokenError:
        return 'Invalid token!', 403


# Only users in the "admin" group can access this resource.
@app.route('/admin')
def admin():
    token = request.cookies.get('token')
    if not token:
        return redirect('/')
    try:
        data = jwt.decode(token, secret_key, algorithms=['HS256'])
        if data['group'] == 'admin':
            is_admin = data["group"] == "admin"
            return render_template('admin.html', user=data["user"], group=data["group"], is_admin=is_admin)
        else:
            return make_response(redirect('/'))
    except jwt.ExpiredSignatureError:
        return 'Session expired!', 403
    except jwt.InvalidTokenError:
        return 'Invalid token!', 403


# The landing page for the main Simulacra username function
@app.route('/username')
def secret():
    token = request.cookies.get('token')
    if not token:
        return redirect('/')
    try:
        data = jwt.decode(token, secret_key, algorithms=['HS256'])
        if data['group'] == 'admin' or data['group'] == 'user':
            is_admin = data["group"] == "admin"
            return render_template('username.html', user=data["user"], group=data["group"], is_admin=is_admin)
        else:
            return make_response(redirect('/'))
    except jwt.ExpiredSignatureError:
        return 'Session expired!', 403
    except jwt.InvalidTokenError:
        return 'Invalid token!', 403


# Open place where everyone can visit.
@app.route('/readme')
def open_route():
    token = request.cookies.get('token')
    if not token:
        return render_template('readme.html', user="", group="", is_admin=False)
    try:
        data = jwt.decode(token, secret_key, algorithms=['HS256'])
        if data['group'] == 'admin' or data['group'] == 'user':
            is_admin = data["group"] == "admin"
            return render_template('readme.html', user=data["user"], group=data["group"], is_admin=is_admin)
        else:
            return make_response(redirect('/'))
    except jwt.ExpiredSignatureError:
        return 'Session expired!', 403
    except jwt.InvalidTokenError:
        return 'Invalid token!', 403


# A logout button that clears the cookie.
@app.route('/logout')
def logout():
    resp = make_response(redirect('/'))
    resp.set_cookie('token', '', expires=0)
    return resp


# The main run function. Should switch to debug mode while developing.
if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
