from Models.Model import Model
from flask_sqlalchemy import SQLAlchemy
import time
import threading

class ModelService:
    def __init__(self):
        self.db = SQLAlchemy()
    def createNew(self,name , status,second):
        model = Model(name , status , time.time() , None , None)
        self.db.session.add(model)
        self.db.session.commit()
        threadJob = self.createThreadJob(second)
        threadJob.start()

    def createThreadJob(self,second):
        def trainingModel():
            time.sleep(int(second))
            print('=====job done=====')
        job = threading.Thread(target = trainingModel)
        return job