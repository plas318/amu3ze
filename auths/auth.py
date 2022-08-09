from os import stat
from flask import Blueprint
from flask import url_for, redirect, render_template, request
from flask.helpers import get_flashed_messages
from flask_login import login_user, logout_user, login_required, current_user
from flask import flash
from .func import user_authenticate, user_create


auth_view = Blueprint('auth_view', __name__, template_folder='templates', static_folder='static', static_url_path='auth_static')

@auth_view.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = user_authenticate(email, password)
        if user:
            login_user(user)
            return redirect(url_for('views.index'))
        flash('Login Failed Please try again', category='danger')
        return redirect(url_for('auth_view.login'))
    return render_template('login.html')

@auth_view.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.index'))

@auth_view.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('views.index'))
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if len(email) < 3:
            print('Name/Email is too short!')
            flash('Name is too short!', category='danger')
        if user_create(email, password):
            return redirect(url_for('auth_view.login', create='success'))
        flash('Register Failed Please try again', category='danger')
        return redirect(url_for('auth_view.sign_up', create='fail'))
    return render_template('sign_up.html')
    


