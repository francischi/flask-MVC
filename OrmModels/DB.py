from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
ormSetting =  config['DB']['ORM']

engine = create_engine(ormSetting)

DBSession = sessionmaker(bind=engine)

session = DBSession()