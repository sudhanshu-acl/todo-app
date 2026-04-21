from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.modules.todos.schema import TodoCreate, TodoUpdate, TodoResponse
from app.modules.todos.service import (
    create_todo,
    get_all_todos,
    get_todo_by_id,
    update_todo,
    delete_todo,
    toggle_todo
)
# import
from app.modules.todos.deps import get_db


router = APIRouter(prefix="/todos", tags=["Todo Module"])

@router.post("/", response_model=TodoResponse, status_code=201)
def create_todo_endpoint(todo: TodoCreate, db: Session = Depends(get_db)):
    todo_item = create_todo(db, todo)
    return todo_item

@router.get("/", response_model=list[TodoResponse])
def list_todos(db: Session = Depends(get_db)):
    todos = get_all_todos(db)
    return todos

@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = get_todo_by_id(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo_endpoint(todo_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    updated_todo = update_todo(db, todo_id, todo)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo

@router.delete("/{todo_id}")
def delete_todo_endpoint(todo_id: int, db: Session = Depends(get_db)):
    deleted = delete_todo(db, todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted"}

@router.patch("/{todo_id}/toggle")
def toggle_todo_endpoint(todo_id: int, db: Session = Depends(get_db)):
    toggled = toggle_todo(db, todo_id)
    if not toggled:
        raise HTTPException(status_code=404, detail="Todo not found")
    return toggled

