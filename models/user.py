from db.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Text, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid

class User(Base):
    
    __tablename__ = 'users'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    google_id = Column(String, unique=True, index=True)
    
    username = Column(String(20), unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    bio = Column(Text(220), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    avatar_url = Column(String, nullable=True)
    
    is_banned = Column(Boolean)
    
    posts = relationship('Post', back_populates='author')
    liked_posts = relationship('Post', secondary='likes', back_populates='liked_by')