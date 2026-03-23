from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session


from . import models, schemas, crud
from .database import engine, get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Blog API",
    description="Premiere partie d'une API pour gerer des articles",
    version="1.0.0"
)


@app.post("/api/articles", response_model=schemas.ArticleResponse, status_code=status.HTTP_201_CREATED, tags=["articles"])
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    return crud.create_article(db=db, article=article)

@app.get("/api/articles", response_model=list[schemas.ArticleResponse], tags=["articles"])
def read_articles(
    skip: int = 0,
    limit: int = 100,
    category: str | None = None,
    author: str | None = None,
    date: str | None = None,
    db: Session = Depends(get_db)
):
    articles = crud.get_articles(
        db,
        skip=skip,
        limit=limit,
        category=category,
        author=author,
        date=date
    )
    return articles


@app.get("/api/articles/search", response_model=list[schemas.ArticleResponse], tags=["articles"])
def search_articles(query: str, db: Session = Depends(get_db)):
    articles = crud.search_articles(db, query)
    return articles


@app.get("/api/articles/{articles_id}", response_model=schemas.ArticleResponse, tags=["articles"])
def read_articles(article_id: int, db: Session = Depends(get_db)):
    db_article = crud.get_article_by_id(db, article_id)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article non Trouve")
    return db_article


@app.get("/")
def root():
    return {"message": "Blog API est lancee! Aller sur /docs pour voir Swagger"}


@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    return {"message": "Connexion avec la base de donnee reussie!"}


@app.put("/api/articles/{article_id}", response_model=schemas.ArticleResponse, tags=["articles"])
def update_article(article_id: int, article: schemas.ArticleUpdate, db: Session = Depends(get_db)):
    db_article = crud.update_article(db, article_id, article)

    if db_article is None:
        raise HTTPException(status_code=404, detail="Article non trouve")

    return db_article


@app.delete("/api/articles/{article_id}", tags=["articles"])
def delete_article(article_id: int, db: Session = Depends(get_db)):
    db_article = crud.delete_article(db, article_id)

    if db_article is None:
        raise HTTPException(status_code=404, detail="Article non trouve")

    return {"message": f"Article avec ID {article_id} supprime avec succes"}
