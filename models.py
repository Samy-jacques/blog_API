from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from .database import Base


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key= True, index=True)
    title = Column(String(200), nullable=False, index=True)
    content = Column(Text, nullable=False)
    author = Column(String(100), nullable=False, index=True)
    category = Column(String(100), nullable=True, index= True)
    tags = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())