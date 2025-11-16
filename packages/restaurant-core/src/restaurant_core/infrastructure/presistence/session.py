from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


DB_URL = "postgresql+psycopg2://admin:password@localhost/Restaurant-db"

engine = create_engine(DB_URL)

connection = engine.connect()

Session = sessionmaker(bind=engine)