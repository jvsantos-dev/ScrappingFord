from dotenv import load_dotenv
import os 
from sqlalchemy import Column, create_engine, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from .schemas import CarSchema
load_dotenv()
senha = os.getenv('SENHA')
# Mudar depois para o novo depois de testar tudo
class DataBase:
    def __init__(self, database_url:str = f'postgresql://postgres:{senha}@db.cpjpjsrqblymmnbpiiho.supabase.co:5432/postgres'):
        self.engine = create_engine(database_url)
        self.session = sessionmaker(bind=self.engine)

    def create_car(self, car):
        session = self.session()        
        try:
            session.add(car)
        except Exception as e:
            session.rollback()
            print(e)
        else:
            session.commit()
        session.close()


    def execute(self, sql: str):
        session = self.session()
        try:
            result = session.execute(text(sql))
            session.commit()
            return result.fetchall()
        
        except Exception as e:
            session.rollback()
            print(e)
            
        finally:
            session.close()


    def update(self, car_id, car: CarSchema, table):
        session = self.session()
        car_atual = session.get(car, car_id)
        car_atual.marca = car.marca
        car_atual.ano = car.ano
        session.commit()
    

    def delete(self, car_id):
        session = self.session()
        session.delete(car_id)
        session.commit()
        session.close()

    