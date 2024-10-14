import os
from typing import Annotated

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from ..models import Users
from ..database import SessionLocal
from .auth import get_current_user
from passlib.context import CryptContext

router = APIRouter(
    prefix='/user',
    tags=['user']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


load_dotenv()
bcrypt_schemes = os.getenv('BCRYPT_SCHEMES')

SECRET_KEY = os.getenv('SECRET')
bcrypt_context = CryptContext(schemes=[bcrypt_schemes], deprecated='auto')
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("/info", status_code=status.HTTP_200_OK)
async def read_user_info(user: user_dependency,
                         db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')

    return db.query(Users).filter(Users.id == user.get('id')).first()


class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)


@router.put("/password", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependency, db: db_dependency,
                          user_verification: UserVerification):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    user_model = db.query(Users).filter(Users.id == user.get('id')).first()

    if not bcrypt_context.verify(user_verification.password, user_model.hashed_password):
        raise HTTPException(status_code=401, detail='Error on password change')
    user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)
    db.add(user_model)
    db.commit()


@router.put("/phonenumber/{phone_number}", status_code=status.HTTP_204_NO_CONTENT)
async def change_phonenumber(user: user_dependency, db: db_dependency,
                             phone_number: str):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    user_model = db.query(Users).filter(Users.id == user.get('id')).first()
    user_model.phone_number = phone_number
    db.add(user_model)
    db.commit()
