from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(36), nullable=False)
    description = db.Column(
        db.String(256), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description