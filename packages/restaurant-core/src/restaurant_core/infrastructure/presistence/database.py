from sqlalchemy import create_engine


DB_URL = "postgresql+psycopg2://admin:password@localhost/Restaurant-db"

engine = create_engine(DB_URL)

connection = engine.connect()