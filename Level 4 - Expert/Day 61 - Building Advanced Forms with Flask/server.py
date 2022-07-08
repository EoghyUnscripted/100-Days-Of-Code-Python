"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 61
PROJECT: Flask WTForms
LEVEL: Expert

"""


from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from decouple import config


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.secret_key = config('FLASK_SECRET_KEY')
    
    return app


app = create_app()


class LoginForm(FlaskForm):
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Log In')
    

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    
    form = LoginForm()
    
    if form.validate_on_submit():
        
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
        
            return render_template('success.html')
        
        else:
        
            return render_template('denied.html')
    
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)