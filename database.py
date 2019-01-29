from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///databases.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create(name,title):
    pic=Gallery(name=name,title=title)
    session.add(pic)
    session.commit()

def delete(id):
    session.query(Gallery).filter_by(id=id).delete()
    session.commit()
def get_all_pics():
    pics = session.query(Gallery).all()
    return pics
