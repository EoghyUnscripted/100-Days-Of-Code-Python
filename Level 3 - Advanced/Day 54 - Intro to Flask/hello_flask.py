"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 54
PROJECT: Hello Flask
LEVEL: Advanced

"""

from flask import Flask
import time


app = Flask(__name__)


def speed_calc_decorator(function):

    def timer():
        start = time.time()     # Get time at start
        function()              # Call function
        end = time.time()       # Get time at end
        speed = end - start     # Output time to complete
        
        return f"<p>{function.__name__} Speed = {speed}</p>"
    
    return timer


@speed_calc_decorator           # Call decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator           # Call decorator 
def slow_function():
    for i in range(100000000):
        i * i
            
            
@app.route("/")
def hello():

    return (f"<h1>Hello, World!</h1>"
            + f"<p>{fast_function()}</p>"
            + f"<p>{slow_function()}</p>")


if __name__ == "__main__":
    app.run(debug=True)