"""
Database class and functions
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config import DELETE_PIN


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Cafe(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(nullable=False)
    img_url: Mapped[str] = mapped_column(nullable=False)
    location: Mapped[str] = mapped_column(nullable=False)
    has_sockets: Mapped[bool] = mapped_column(nullable=False)
    has_toilet: Mapped[bool] = mapped_column(nullable=False)
    has_wifi: Mapped[bool] = mapped_column(nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(nullable=False)
    seats: Mapped[str] = mapped_column()
    coffee_price: Mapped[str] = mapped_column()


def insert_cafe(c):
    """
    Insert new cafe into db
    :param c:dict CafeForm data
    :return: None
    """
    new_cafe = Cafe(
        name=c["name"],
        map_url=c["map"],
        img_url=c["photo"],
        location=c["location"],
        has_sockets=c["sockets"],
        has_toilet=c["toilet"],
        has_wifi=c["wifi"],
        can_take_calls=c["calls"],
        seats=c["seats"],
        coffee_price=c["price"]
    )
    db.session.add(new_cafe)
    db.session.commit()


def delete_cafe(c):
    """
    Delete cafe from db
    :param c:dict DelCafeForm data
    :return: True id cafe nae was found and deleted from db
    """
    if c["pin"] == DELETE_PIN:
        cafe = db.session.execute(db.select(Cafe).where(Cafe.name == c["name"])).scalar()
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return True
        else:
            return False
    else:
        return False
