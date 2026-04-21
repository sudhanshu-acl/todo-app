from . import repository

def create_todo(db, data):
    return repository.create(db, data)


def get_all_todos(db):
    return repository.get_all(db)


def get_todo_by_id(db, todo_id: int):
    return repository.get_by_id(db, todo_id)


def update_todo(db, todo_id: int, data):
    return repository.update(db, todo_id, data)


def delete_todo(db, todo_id: int):
    return repository.delete(db, todo_id)


def toggle_todo(db, todo_id: int):
    return repository.toggle_complete(db, todo_id)

