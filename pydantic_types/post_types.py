from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class PostRequest(BaseModel):
    content: str = Field(min_length=1, max_length=280)
    reply_to: Optional[UUID] = None
    reply_of: Optional[UUID] = None
       
class PostResponse(BaseModel):
    msg: str
    post_id: Optional[UUID] = None