# -*- coding: utf-8 -*-

from pydantic import BaseModel, Field

class Message(BaseModel):
    class Config:
        populate_by_name = True

    session_id: str = Field(alias="sessionId")
    text: str = Field(alias="text")