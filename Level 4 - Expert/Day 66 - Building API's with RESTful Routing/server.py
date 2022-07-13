"""

INSTITUTION: UDEMY.COM
COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2022
INSTRUCTOR: Dr. Angela Yu

DESCRIPTION:
Master Python by building 100 projects in 100 days.
Learn to build websites, games, apps, plus scraping and data science

DAY: 66
PROJECT: Cafe & Wifi API
LEVEL: Expert

"""


from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice
from decouple import config


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():

    return render_template('index.html')


@app.route("/random", methods=['GET'])
def random():

    all_cafes = db.session.query(Cafe).all()
    random_cafe = choice(all_cafes)

    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all", methods=['GET'])
def all():

    all_cafes = db.session.query(Cafe).all()

    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search", methods=['GET'])
def search():

    search_cafes = Cafe.query.filter_by(
        location=str(request.args.get('loc')).capitalize())

    search_results = [cafe.to_dict() for cafe in search_cafes]

    if len(search_results) < 1:
        return jsonify(error={
            "Not Found": f"Sorry, we do not have a cafe in { str(request.args.get('loc')).capitalize() }."
        })

    else:

        return jsonify(cafes=[cafe.to_dict() for cafe in search_cafes])


@app.route("/new", methods=['POST'])
def new():

    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        has_sockets=bool(request.form.get("sockets")),
        can_take_calls=bool(request.form.get("calls")),
        coffee_price=request.form.get("price")
    )

    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_price(cafe_id):

    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)

    if not cafe:

        return jsonify(error={
            "Not Found": f"Sorry, we do not have a cafe with id { cafe_id }."
        })

    else:

        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the coffee price."})


@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def delete(cafe_id):

    api_key = request.args.get("api_key")
    cafe = db.session.query(Cafe).get(cafe_id)

    if not cafe:

        return jsonify(error={
            "Not Found": f"Sorry, we do not have a cafe with id { cafe_id }."
        })

    else:

        if api_key == config("REST_API_KEY"):

            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from our list."})

        else:

            return jsonify(response={"Forbidden": "Sorry, that is not allowed. Please check your api_key."})


if __name__ == '__main__':
    app.run(debug=True)
