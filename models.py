from sqlalchemy import create_engine, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm import relationship


engine = create_engine("sqlite:///db.db")   
conn = engine.connect()

def get_session():
    return Session(bind=engine)


BaseModel = declarative_base()


class GameSession(BaseModel):
    __tablename__ = "sessions"
    id = Column(String(36), primary_key=True)
    users = relationship("User")
    abab = 12
    def json(self):
        return {
            "id": self.id
        }

class User(BaseModel):
    __tablename__ = "users"
    id = Column(String(36), primary_key=True)
    active_session_id = Column(String(36), ForeignKey('sessions.id'))
    active_session = relationship("GameSession", overlaps="users")