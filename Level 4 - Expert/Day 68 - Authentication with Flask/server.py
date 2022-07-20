"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 68
PROJECT: User Authentication
LEVEL: Expert

"""

from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from decouple import config


app = Flask(__name__)


app.config['SECRET_KEY'] = config('FLASK_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['STATIC_DIRECTORY'] = "Level 4 - Expert/Day 68 - Authentication with Flask"
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        
        if User.query.filter_by(email=request.form.get('email')).first():
            
            flash("You've already signed up with that email, log in instead!")
            
            return redirect(url_for('login'))
        
        data = request.form
        
        hash_and_salted_password = generate_password_hash(
            data.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email = data.get("email"),
            password = hash_and_salted_password,
            name = data.get("name")
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        login_user(new_user)
        
        return redirect(url_for("secrets"))
    
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == "POST":
        
        data = request.form
        
        email = data.get('email')
        password = data.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if not user:
            
            flash("That email does not exist, please try again.")
            
            return redirect(url_for('login'))
        
        elif not check_password_hash(user.password, password):
            
            flash('Password incorrect, please try again.')
            
            return redirect(url_for('login'))
        
        else:
            
            login_user(user)
            
            return redirect(url_for('secrets'))
    
    return render_template("login.html")


@login_manager.user_loader
def load_user(user_id):
    
    return User.query.get(int(user_id))


@app.route('/secrets')
@login_required
def secrets():
    
    return render_template("secrets.html", name=current_user.name, logged_in=current_user.is_authenticated)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template("login.html")


@app.route('/download')
@login_required
def download():
    return send_from_directory("static", "files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
