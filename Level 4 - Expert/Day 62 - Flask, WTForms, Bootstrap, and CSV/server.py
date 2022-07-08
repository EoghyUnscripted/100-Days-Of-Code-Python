"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 62
PROJECT: Flask, Bootstrap, Forms, & Data
LEVEL: Expert

"""


from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, URLField, SelectField
from wtforms.validators import DataRequired, URL
from datetime import datetime
import csv
from decouple import config

app = Flask(__name__)
app.config['SECRET_KEY'] = config('FLASK_SECRET_KEY')
Bootstrap(app)


coffee_rating_choices = ['Select', '✘', '☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️']
wifi_rating_choices = ['Select', '✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪']
power_rating_choices = ['Select', '✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌']


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location = URLField('Location', validators=[DataRequired(), URL()])
    open_time = TimeField('Open Time', validators=[DataRequired()])
    closing_time = TimeField('Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=coffee_rating_choices)
    wifi_rating = SelectField('WiFi Rating', choices=wifi_rating_choices)
    power_rating = SelectField('Power Rating', choices=power_rating_choices)
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    
    form = CafeForm()
    
    if form.validate_on_submit():
        
        print("True")
        
        with open('Level 4 - Expert/Day 62 - Flask, WTForms, Bootstrap, and CSV/Data/cafe-data.csv', 'a') as file:
            
            d_open = (form.open_time.data).strftime("%I:%M%p")
            d_close = (form.closing_time.data).strftime("%I:%M%p")
            
            new_line = (f"\n{ form.cafe.data },{ form.location.data },{ d_open },{ d_close },"
                      + f"{ form.coffee_rating.data },{ form.wifi_rating.data },{ form.power_rating.data }")
            
            file.write(new_line)
            
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('Level 4 - Expert/Day 62 - Flask, WTForms, Bootstrap, and CSV/Data/cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
