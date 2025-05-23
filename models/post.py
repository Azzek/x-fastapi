from db.database import Base

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, Text, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid



class Post(Base):
    
    __tablename__ = 'posts'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    author_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    
    content = Column(Text(280), nullable=False)
    media_url = Column(String(150), nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    reply_of_id = Column(UUID(as_uuid=True), ForeignKey('posts.id'), nullable=True)
    reply_to_id = Column(UUID(as_uuid=True), ForeignKey('posts.id'), nullable=True)
    
    liked_by = relationship('User', secondary='likes', back_populates='liked_posts')
    
    reply_of = relationship('Post', remote_side=[id], foreign_keys=[reply_of_id], back_populates='replies')
    replies = relationship('Post',
                           back_populates='reply_of',
                           cascade='all, delete-orphan',
                           foreign_keys=[reply_of_id])
    
    reply_to = relationship('Post', remote_side=[id], foreign_keys=[reply_to_id], back_populates='reply_targets')
 
    reply_targets = relationship('Post',
                                 back_populates='reply_to',
                                 cascade='all, delete-orphan',
                                 foreign_keys=[reply_to_id])
    
    author = relationship('User', back_populates='posts')

    