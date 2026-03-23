from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List


class ArticleBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="Titre de l'article (obligatoire)")
    author: str = Field(..., max_length=100, description="Nom ou pseudo de l'auteur")
    content: str = Field(..., min_length=10, description="Contenu principal de l'article")
    category: Optional[str] = Field(None, max_length=100, description="Categorie (ex: Tech, Sport, Voyage)")
    tags: Optional[str] = Field(None, description="Tags separes par des virgules (ex: python, fastapi, damso)")


class ArticleCreate(ArticleBase):
    pass


class ArticleUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    content: Optional[str] = Field(None, min_length=10)
    category: Optional[str] = Field(None, max_length=100)
    tags: Optional[str] = Field(None)

    class Config:
        extra = "forbid"


class ArticleResponse(ArticleBase):
    id: int
    created_at: Optional[datetime]

    class Config:
        from_attributes = True