from flask import Flask, render_template, request, url_for, session, redirect, flash
from werkzeug.utils import secure_filename
from functools import wraps
from markupsafe import escape
import os
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_hex()
app.config['client_password'] = ''


# ---------------------------------------------------------------
# Decorators
def setup_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        client_password = app.config['client_password']
        if not client_password:
            return redirect(url_for('setup_page'))
        return f(*args, **kwargs)

    return decorated_function


def is_setup(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_password' and 'client_password' in session:
            return redirect(url_for('admin_page'))
        return f(*args, **kwargs)

    return decorated_function


def client_login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'login' in session:
            return f(*args, **kwargs)
        elif 'admin' in session:
            return redirect(url_for('admin_page'))
        return redirect(url_for('login_page'))
    return decorated_function


def is_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin' in session:
            return f(*args, **kwargs)
        return render_template('index_page')

    return decorated_function


# ---------------------------------------------------------------
#                   ADMIN SECTION
# ---------------------------------------------------------------
# SETUP PAGE
@app.route('/setup', methods=['GET', 'POST'])
@is_setup
def setup_page():
    if request.method == 'POST':

        client_password = escape(request.form['client_password'])

        app.config['client_password'] = client_password
        session['admin'] = True
        return redirect(url_for('admin_page'))

    return render_template('setup.html')


# -------------------------------------------------------------
# ADMIN PAGE
@app.route('/admin')
@setup_required
@is_admin
def admin_page():
    client_password = app.config['client_password']
    file_list = os.listdir(f'{os.path.abspath(os.getcwd())}\\static\\uploads')
    return render_template('admin.html',
                           file_list=file_list,
                           client_password=client_password)


# --------------------------------------------------------------
@app.route('/admin/delete/file/<name>', methods=['GET'])
@is_admin
def delete_file(name):
    os.remove(f'{os.path.abspath(os.getcwd())}\\static\\uploads\\{name}')
    return redirect(url_for('admin_page'))


# --------------------------------------------------------------
@app.route('/admin/add/file', methods=['POST'])
def add_file():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(f'{os.path.abspath(os.getcwd())}\\static\\uploads', filename))
    return redirect(url_for('admin_page'))


# -------------------------------------------------------------
# ERROR HANDLING
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# ---------------------------------------------------------------
# ---------------------------------------------------------------
#                   CLIENT SECTION
# ---------------------------------------------------------------
# ---------------------------------------------------------------
#  CLIENT LOGIN
@app.route('/client/login', methods=['POST', 'GET'])
def login_page():
    if request.method == 'POST':
        password = escape(request.form['client_password'])

        if not password:
            flash('الرجاء إدخال كلمة المرور')
            return redirect(url_for('login_page'))

        if password == app.config['client_password']:
            session['login'] = True
            return redirect(url_for('index_page'))

    return render_template('client_login.html')


# ---------------------------------------------------------------
# CLIENT INDEX PAGE
@app.route('/')
@setup_required
@client_login_required
def index_page():
    file_list = os.listdir(f'{os.path.abspath(os.getcwd())}\\static\\uploads')

    return render_template('index.html', file_list=file_list)


# --------------------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0')
