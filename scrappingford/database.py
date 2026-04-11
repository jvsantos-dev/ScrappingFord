from dotenv import load_dotenv
import os 
from sqlalchemy import Column, create_engine, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from .schemas import CarSchema
load_dotenv()
senha = os.getenv('SENHA')
# DATABASE_URL = f"postgresql://postgres:{senha}@db.cpjpjsrqblymmnbpiiho.supabase.co:5432/postgres"
DATABASE_URL = F"sqlite:///database.db"
engine = create_engine(DATABASE_URL)

class DataBase:
    def __init__(self, database_url:str = 'sqlite:///database.db'):
        self.engine = create_engine(database_url)
        self.SessionLocal = sessionmaker(bind=self.engine)

    def create_car(self, car):
        session = self.SessionLocal()
        try:
            session.add(car)
        except Exception as e:
            session.rollback()
            print(e)
        else:
            session.commit()
        session.close()


    def execute(self, sql: str):
        session = self.SessionLocal()
        try:
            self.engine.connection.execute(text(sql))
            session.commit()
        except Exception as e:
            print(e)
        else:
            session.commit()
        session.close()
    

    def update(self, car_id, car: CarSchema, table):
        session = self.SessionLocal()
        car_atual = session.get(car, car_id)
        car_atual.marca = car.marca
        car_atual.ano = car.ano
        session.commit()
    

    def delete(self, car_id):
        session = self.SessionLocal()
        session.delete(car_id)
        session.commit()
        session.close()
