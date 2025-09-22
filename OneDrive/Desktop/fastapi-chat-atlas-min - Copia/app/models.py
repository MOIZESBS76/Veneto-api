from __future__ import annotations
from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime

class MessageIn(BaseModel):
	username: str = Field(..., min_length=1, max_length=50)
	content: str = Field(..., min_length=1, max_length=1000)

	@validator("username", pre=True, always=True)
	def strip_username(cls, v):
		return (str(v) if v is not None else "").strip()[:50]

	@validator("content", pre=True, always=True)
	def strip_content(cls, v):
		return (str(v) if v is not None else "").strip()[:1000]

class MessageOut(BaseModel):
  _id: str
  room: str
  username: str
  content: str
  created_at: str

class MessagesPage(BaseModel):
  items: list[MessageOut]
  next_cursor: Optional[str]