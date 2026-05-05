from sqlalchemy.orm import Session
import bcrypt
from . import repository
from .schema import UserCreate

def get_password_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def create_user(db: Session, user_in: UserCreate):
    existing_user = repository.get_by_email(db, user_in.email)
    if existing_user:
        return None
    
    hashed_password = get_password_hash(user_in.password)
    user_data = user_in.model_dump()
    del user_data["password"]
    user_data["hashed_password"] = hashed_password

    return repository.create(db, user_data)

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return repository.get_all(db, skip=skip, limit=limit)

def get_user_by_id(db: Session, user_id: int):
    return repository.get_by_id(db, user_id)
