from dotenv import load_dotenv
import os 
from sqlalchemy import Column, create_engine, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from ..vehicles.models.vehicle import Vehicle
load_dotenv()
senha = os.getenv('SENHA')
database_url =  f'postgresql://postgres:{senha}@db.cpjpjsrqblymmnbpiiho.supabase.co:5432/postgres'
engine = create_engine(database_url)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

    