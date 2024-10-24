from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# This should be the name of the environment variable, not the connection string itself
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")  # Use the environment variable name

# Check if the URL is correctly loaded (optional, for debugging)
if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables.")

# Create the engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for model classes
Base = declarative_base()

# Dependency to get a session in FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
