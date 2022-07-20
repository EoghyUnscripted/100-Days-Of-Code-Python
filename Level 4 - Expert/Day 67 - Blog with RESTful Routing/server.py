"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 67
PROJECT: RESTful Blog
LEVEL: Expert

"""

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from decouple import config
from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = config('FLASK_SECRET_KEY')
ckeditor = CKEditor(app)
Bootstrap(app)


##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

@app.route('/')
def home():
    
    posts = BlogPost.query.all()
    
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:post>", methods=['GET'])
def show_post(post):
    
    requested_post = BlogPost.query.get(post)
            
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=['GET', 'POST'])
def new_post():
    
    form = CreatePostForm()
    
    if form.validate_on_submit():
        
        new_post = BlogPost(
            title = form.title.data,
            subtitle = form.subtitle.data,
            author = form.author.data,
            img_url = form.img_url.data,
            body = form.body.data,
            date=date.today().strftime("%B %d, %Y")
        )
        
        db.session.add(new_post)
        db.session.commit()
        
        return redirect(url_for("home"))
            
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post>", methods=['GET', 'POST'])
def edit_post(post):
    
    posting = BlogPost.query.get(post)
    edit_form = CreatePostForm(
            title = posting.title,
            subtitle = posting.subtitle,
            author = posting.author,
            img_url = posting.img_url,
            body = posting.body,
        )
    if edit_form.validate_on_submit():
        
        posting.title = edit_form.title.data
        posting.subtitle = edit_form.subtitle.data
        posting.img_url = edit_form.img_url.data
        posting.author = edit_form.author.data
        posting.body = edit_form.body.data    
        
        db.session.commit()
        
        return redirect(url_for("show_post", post=posting.id))
    
    edit_form.submit.label.text = 'Save Edits'
            
    return render_template("make-post.html", form=edit_form, is_edit=True)


@app.route("/delete-post/<int:post>", methods=['GET'])
def delete_post(post):
    
    delete_post = BlogPost.query.get(post)
    db.session.delete(delete_post)
    db.session.commit()
    
    return redirect(url_for("home"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)