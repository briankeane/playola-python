from typing import Dict

from sqlalchemy.sql.sqltypes import JSON
from sqlmodel import Field, Relationship, SQLModel, Column


# Shared properties
# TODO replace email str with EmailStr when sqlmodel supports it
class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    is_active: bool = True
    is_superuser: bool = False


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str


# TODO replace email str with EmailStr when sqlmodel supports it
class UserCreateOpen(SQLModel):
    email: str
    password: str


# Properties to receive via API on update, all are optional
# TODO replace email str with EmailStr when sqlmodel supports it
class UserUpdate(UserBase):
    email: str | None = None
    password: str | None = None


# TODO replace email str with EmailStr when sqlmodel supports it
class UserUpdateMe(SQLModel):
    full_name: str | None = None
    email: str | None = None


class UpdatePassword(SQLModel):
    current_password: str
    new_password: str


# Database model, database table inferred from class name
class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str
    items: list["Item"] = Relationship(back_populates="owner")


# Properties to return via API, id is always required
class UserOut(UserBase):
    id: int


class UsersOut(SQLModel):
    data: list[UserOut]
    count: int


# Shared properties
class ItemBase(SQLModel):
    title: str
    description: str | None = None


# Properties to receive on item creation
class ItemCreate(ItemBase):
    title: str


# Properties to receive on item update
class ItemUpdate(ItemBase):
    title: str | None = None


# Database model, database table inferred from class name
class Item(ItemBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    owner_id: int | None = Field(default=None, foreign_key="user.id", nullable=False)
    owner: User | None = Relationship(back_populates="items")


# Properties to return via API, id is always required
class ItemOut(ItemBase):
    id: int
    owner_id: int


class ItemsOut(SQLModel):
    data: list[ItemOut]
    count: int


# Generic message
class Message(SQLModel):
    message: str


# JSON payload containing access token
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(SQLModel):
    sub: int | None = None


class NewPassword(SQLModel):
    token: str
    new_password: str


class SpotifyUserBase(SQLModel):
    spotify_user_id: str
    spotify_display_name: str
    spotify_token_info: dict


class SpotifyUser(SpotifyUserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    spotify_display_name: str | None = Field(default=None)
    spotify_user_id: str | None = Field(default=None, nullable=False)
    user_id: int = Field(default=None, foreign_key="user.id", nullable=False)
    spotify_token_info: dict | None = Field(default=None, sa_column=Column(JSON))

    class Config:
        arbitrary_types_allowed = True


class SpotifyUserCreate(SpotifyUserBase):
    user_id: int


class SpotifyUserUpdate(SpotifyUserBase):
    spotify_display_name: str | None = None
    spotify_user_id: str | None = None
    user_id: int | None = None
    spotify_token_info: Dict | None = None
