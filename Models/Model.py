from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Model(db.Model):
    __tablename__ = 'models'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(36), nullable=False)
    status = db.Column(
        db.String(15), nullable=False)
    createTime = db.Column(
        db.String(15), nullable=False)
    modifyTime = db.Column(
        db.String(15), nullable=True)
    deleteTime = db.Column(
        db.String(15), nullable=True)    

    def __init__(self, name, status, createTime,modifyTime,deleteTime):
        self.name = name
        self.status = status
        self.createTime = createTime
        self.modifyTime = modifyTime
        self.deleteTime = deleteTime