"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 57
PROJECT: Blog Project
LEVEL: Advanced

"""

from datetime import datetime
import requests
from flask import Flask, render_template
from post import Post

# Get filler blog posts
r = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
posts_list = []

# Loop through json data to create new post objects and add to list
for post in r:
    next_post = Post(post["id"], post["title"], post["subtitle"], post["body"])
    posts_list.append(next_post)
    

app = Flask(__name__)
    

# Main route
@app.route("/")
def home():
    
    this_year = datetime.now().year
    
    return render_template("index.html", year=this_year, posts=posts_list)


# Blog route
@app.route("/post/<int:this_post>")
def get_post(this_post):
    
    this_year = datetime.now().year
    
    get_post = None
    
    # Match the requested post id to post object in list, return
    for post in posts_list:
        if post.id == this_post:
            get_post = post
    
    return render_template("blog.html", year=this_year, post=get_post)


if __name__ == "__main__":
    app.run(debug=True)