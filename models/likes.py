from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from db.database import Base

likes = Table(
    'likes',
    Base.metadata,
    Column('user_id', UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), primary_key=True),
    Column('post_id', UUID(as_uuid=True), ForeignKey('posts.id', ondelete='CASCADE'), primary_key=True)
)