import sys

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/table/<sex>/<age>')
def login(sex, age):
    return render_template('login.html', title='Оформление каюты', s=sex, a=int(age))



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
