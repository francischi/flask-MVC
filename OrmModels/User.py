from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(36), nullable=False)
    description = db.Column(
        db.String(100), nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description