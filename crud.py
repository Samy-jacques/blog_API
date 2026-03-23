from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

def create_article(db: Session, article: schemas.ArticleCreate):
    db_article = models.Article(
        title=article.title,
        content=article.content,
        author=article.author,
        category=article.category,
        tags=article.tags,
    )
    db.add(db_article)
    db.commit()
    db.refresh(db_article)


    return schemas.ArticleResponse(
        id=db_article.id,
        title=db_article.title,
        author=db_article.author,
        date=db_article.created_at.strftime("%Y-%m-%d") if db_article.created_at else "",
        category=db_article.category,
        content=db_article.content,
        tags=db_article.tags
    )


def get_articles(
        db: Session,
        skip: int = 0,
        limit: int = 100,
        category: str | None = None,
        author: str | None = None,
        date: str | None = None,
):
    query = db.query(models.Article)

    if category:
        query = query.filter(models.Article.category == category)
    if author:
        query = query.filter(models.Article.author == author)
    if date:
        try:
            parsed_date = datetime.strptime(date, "%Y-%m-%d")
            next_day = parsed_date.replace(hour=23, minute=59, second=59)

            query = query.filter(
                models.Article.created_at >= parsed_date,
                models.Article.created_at <= next_day
            )
        except ValueError:
            pass
    return query.offset(skip).limit(limit).all()

def get_article_by_id(db: Session, article_id: int):
    return db.query(models.Article).filter(models.Article.id == article_id).first()

def update_article(db: Session, article_id: int, article: schemas.ArticleUpdate):
    db_article = db.query(models.Article).filter(models.Article.id == article_id).first()

    if not db_article:
        return None

    update_data = article.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_article, key, value)

    db.commit()
    db.refresh(db_article)

    return db_article

def delete_article(db: Session, article_id: int):
    db_article = db.query(models.Article).filter(models.Article.id == article_id).first()

    if not db_article:
        return None

    db.delete(db_article)
    db.commit()

    return db_article


def search_articles(db: Session, query: str):
    return db.query(models.Article).filter(
        (models.Article.title.ilike(f"%{query}%")) |
        (models.Article.content.ilike(f"%{query}%"))
    ).all()