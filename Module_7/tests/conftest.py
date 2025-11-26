import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:", echo=True)
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
