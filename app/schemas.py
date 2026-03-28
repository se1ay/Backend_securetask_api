from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal

class LoginIn(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)

class TokenOut(BaseModel):
    token: str
    expires_in: int

TaskStatus = Literal["todo", "doing", "done"]

class TaskIn(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=5000)

class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: TaskStatus

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=5000)
    status: Optional[TaskStatus] = None

class Page(BaseModel):
    items: list[TaskOut]
    total: int
    limit: int
    offset: int
