from re import L
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