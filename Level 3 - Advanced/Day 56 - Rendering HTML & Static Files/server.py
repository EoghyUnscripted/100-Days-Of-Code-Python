"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 56
PROJECT: Name Card
LEVEL: Advanced

"""

from flask import Flask, render_template


app = Flask(__name__)

    
# Main route
@app.route("/")
def hello():
    
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)