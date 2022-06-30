"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 55
PROJECT: Higher or Lower
LEVEL: Advanced

"""

from flask import Flask
import random


ran_int = random.randint(1, 10)
print(ran_int)

app = Flask(__name__)
    
# Main route
@app.route("/")
def hello():
    
    return (f"<h1 style='text-align: center;'>Hello! Guess a number between 1 and 10!</h1>"
            + f"<img style='display: block; margin-left: auto; margin-right: auto;' src='https://media.giphy.com/media/UDU4oUJIHDJgQ/giphy.gif'/>")


# Guessed number route
@app.route("/<int:num>")
def choice(num):
    
        # Guessed number is greater than random number
        if num > ran_int:
        
            return (f"<em><h1 style='text-align: center; color: red;'>That guess is too high!</h1></em>"
                        + f"<img style='display: block; margin-left: auto; margin-right: auto;' src='https://media.giphy.com/media/xTiN0CNHgoRf1Ha7CM/giphy.gif'/>")

        # Guessed number is less than random number
        elif num < ran_int:
            
            return (f"<em><h1 style='text-align: center; color: red;'>That guess is too low!</h1></em>"
                         + f"<img style='display: block; margin-left: auto; margin-right: auto;' src='https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif'/>")
        
        # Guessed number matches random number
        elif num == ran_int:
            
            return (f"<em><h1 style='text-align: center; color: green;'>That guess is correct!</h1></em>"
                         + f"<img style='display: block; margin-left: auto; margin-right: auto;' src='https://media.giphy.com/media/26u4cqiYI30juCOGY/giphy.gif'/>")


if __name__ == "__main__":
    app.run(debug=True)