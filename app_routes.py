"""
Flask routes definitions
"""

from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap

from cafes_db import db, Cafe, insert_cafe, delete_cafe
from forms import CafeForm, DelCafeForm

# create the app
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
# initialize the app with the extension
db.init_app(app)


# home
@app.route("/")
def home():
    return render_template("index.html")


# all cafes
@app.route("/cafes")
def all_cafes():
    cafes = db.session.execute(db.select(Cafe).order_by(Cafe.location)).scalars()
    header = {"name": "Name",
              "map_url": "Google Maps",
              "location": "Neighbourhood",
              "has_sockets": "Sockets",
              "has_toilet": "Toilet",
              "has_wifi": "Wi-Fi",
              "can_take_calls": "Calls friendly",
              "seats": "Seats",
              "coffee_price": "Coffee price",
              "img_url": "Photo"
              }
    return render_template('cafes.html', header=header, cafes=cafes)


# add cafe
@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm(request.form)
    if request.method == "POST" and form.validate():
        form_data = form.data
        form_data.pop("submit", None)
        form_data.pop("csrf_token", None)
        print(form_data)
        insert_cafe(form_data)
        return redirect("cafes")
    return render_template("add.html", form=form)


# delete cafe
@app.route("/delete", methods=["GET", "POST"])
def del_cafe():
    form = DelCafeForm(request.form)
    if request.method == "POST" and form.validate():
        form_data = form.data
        form_data.pop("submit", None)
        form_data.pop("csrf_token", None)
        if delete_cafe(form_data):
            return redirect("cafes")
    return render_template("delete.html", form=form)
