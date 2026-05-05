from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.modules.users import schema, service, deps

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register", response_model=schema.UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(user_in: schema.UserCreate, db: Session = Depends(deps.get_db)):
    print("User register api route HIT..", user_in)
    user = service.create_user(db, user_in)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists."
        )
    return user

@router.get("/", response_model=list[schema.UserResponse])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    return service.get_users(db, skip=skip, limit=limit)

@router.get("/{user_id}", response_model=schema.UserResponse)
def get_user(user_id: int, db: Session = Depends(deps.get_db)):
    user = service.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
