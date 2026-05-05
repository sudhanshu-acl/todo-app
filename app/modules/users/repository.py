from sqlalchemy.orm import Session
from .model import User

def get_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create(db: Session, obj_in: dict):
    db_obj = User(**obj_in)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update(db: Session, user_id: int, obj_in: dict):
    db_obj = get_by_id(db, user_id)
    if not db_obj:
        return None
    for key, value in obj_in.items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete(db: Session, user_id: int):
    db_obj = get_by_id(db, user_id)
    if not db_obj:
        return None
    db.delete(db_obj)
    db.commit()
    return db_obj
