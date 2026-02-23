from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "postgresql://admin:123456@localhost:5432/collab_db"

engine = create_engine(DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session