"""
FlaskForm forms definitions
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, BooleanField, PasswordField
from wtforms.validators import DataRequired, URL, Length


class CafeForm(FlaskForm):
    name = StringField("Cafe name", validators=[DataRequired()])
    map = URLField("Google Maps link", validators=[DataRequired(), URL()])
    photo = URLField("Photo link", validators=[DataRequired(), URL()])
    location = StringField("Neighbourhood", validators=[DataRequired()])
    sockets = BooleanField("Has sockets")
    toilet = BooleanField("Has toilet")
    wifi = BooleanField("Has Wi-Fi")
    calls = BooleanField("Calls friendly")
    seats = StringField("Number of seats")
    price = StringField("Coffee price")
    submit = SubmitField("Submit")


class DelCafeForm(FlaskForm):
    name = StringField("Cafe name", validators=[DataRequired()])
    pin = PasswordField("PIN", validators=[DataRequired(), Length(4,4)])
    submit = SubmitField("Submit")
