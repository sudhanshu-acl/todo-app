from sqlalchemy.orm import Session
from .model import Todo


def create(db: Session, data):
    print("Creating todo with data:", data)
    todo = Todo(**data.dict())
    print("Created todo object:", todo)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def get_all(db: Session):
    return db.query(Todo).all()


def get_by_id(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()


def update(db: Session, todo_id: int, data):
    todo = get_by_id(db, todo_id)
    if not todo:
        return None

    for key, value in data.dict(exclude_unset=True).items():
        setattr(todo, key, value)

    db.commit()
    db.refresh(todo)
    return todo


def delete(db: Session, todo_id: int):
    todo = get_by_id(db, todo_id)
    if not todo:
        return None

    db.delete(todo)
    db.commit()
    return todo


def toggle_complete(db: Session, todo_id: int):
    todo = get_by_id(db, todo_id)
    if not todo:
        return None

    todo.completed = not todo.completed
    db.commit()
    db.refresh(todo)
    return todo

