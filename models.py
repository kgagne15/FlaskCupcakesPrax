"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """Model for cupcake
    id: PK
    Flavor: Text, Not Null
    Size: Text, Not Null
    Rating: Float, Not Null
    Image: Text, Not Null, Default: https://tinyurl.com/demo-cupcake
    """
    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default="https://tinyurl.com/demo-cupcake")

    def __repr__(self):
        c = self
        return f"<Cupcake id={c.id}, Flavor={c.flavor}, Size={c.size}, Rating={c.rating}>"

