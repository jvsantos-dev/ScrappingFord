import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
import os 
from scrappingford.models import table_registry

@pytest.fixture(scope="module")
def client():

    previous_database_url = os.environ.get("TEST_DATABASE_URL")
    engine = create_engine(previous_database_url)
    table_registry.metadata.drop_all(engine)
    table_registry.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    yield session