from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas

from .database import SessionLocal, engine

models.Base.metadata.create_all (bind = engine)

app = FastAPI ()

# Dependency
def get_db () :
    
    db = SessionLocal ()
    
    try :
        
        yield db
        
    finally :
        
        db.close ()

@app.get ("/users/", response_model = list [schemas.User])
def read_users (skip : int = 0, 
                limit : int = 100, 
                db : Session = Depends (get_db)
                ) :
    
    crud_read_users = crud.get_users (db, 
                                     skip = skip, 
                                     limit = limit
                                     )
    if crud_read_users is None :
        
        http_exception = HTTPException (status_code = 404, 
                                        detail = "User not found"
                                        )
            
        raise http_exception
    
    return crud_read_users

@app.post("/users/{user_id}", response_model = schemas.User)
def create_user (user : schemas.UserCreate, 
                 db : Session = Depends (get_db)
                 ) :
    
        crud_create_user = crud.create_user (db = db, 
                                             user = user
                                            )
        
        if crud_create_user is None :
        
            http_exception = HTTPException (status_code = 404, 
                                            detail = "User not create"
                                            )
        
            raise http_exception
        
        return crud_create_user

@app.get ("/users/{user_id}", response_model = schemas.User)
def read_user (user_id : int, 
               db : Session = Depends (get_db)
               ) : 
    
    crud_read_user = crud.read_user (db, 
                                     user_id = user_id)
    if crud_read_user is None :
        
        http_exception = HTTPException (status_code = 404, 
                                        detail = "User not read"
                                        )
        
        raise http_exception
    
    return crud_read_user
        
@app.put("/users/{user_id}", response_model = schemas.User)
def update_user (user_id: int, 
                 user : schemas.UserUpdate, 
                 db : Session = Depends (get_db)
                ) :
    
    crud_update_user = crud.update_user (db = db, 
                                         user_id = user_id, 
                                         user = user
                                        )
            
    if crud_update_user is None :
                
        http_exception = HTTPException (status_code = 404, 
                                        detail = "User not update"
                                        )
        
        raise http_exception
            
    return crud_update_user

@app.delete ("/users/{user_id}", response_model = schemas.User)
def delete_user (user_id : int, 
                 db : Session = Depends (get_db)
                ) :
    
    crud_delete_user = crud.delete_user (db = db, 
                                         user_id = user_id
                                         )
        
    if crud_delete_user is None :
        
        http_exception = HTTPException(status_code = 404, 
                                       detail = "User not delete"
                                       )
            
        raise http_exception
        
    return crud_delete_user

@app.get ("/articles/", response_model = list [schemas.Article])
def read_articles (skip : int = 0, 
                   limit : int = 100, 
                   db : Session = Depends (get_db)
                   ) :
    
    crud_read_articles = crud.get_articles (db, 
                                           skip = skip, 
                                           limit = limit
                                           )
    
    if crud_read_articles is None :
        
        http_exception = HTTPException (status_code = 404, 
                                        detail = "Article not found"
                                        )
            
        raise http_exception
    
    return crud_read_articles

@app.post ("/users/{user_id}/articles/", response_model = schemas.Article)
def create_article_for_user (user_id : int, 
                             article_id : schemas.ArticleCreate, 
                             db : Session = Depends (get_db)
                            ) :

    crud_create_user_article = crud.create_user_article (db = db, 
                                                         article_id = article_id, 
                                                         user_id = user_id
                                                         )
    if crud_create_user_article is None :
            
        http_exception = HTTPException (status_code = 404, 
                                        detail = "Article not create"
                                        )
        raise http_exception
    
    return crud_create_user_article
    
@app.get("/users/{user_id}/articles/", response_model = schemas.Article)
def read_article_for_user (user_id : int, 
                           article_id : schemas.ArticleUpdate, 
                           db : Session = Depends (get_db)
                           ) :
    
    crud_read_user_article = crud.read_user_article (db, 
                                                     article_id = article_id,
                                                     user_id = user_id
                                                    )
        
    if crud_read_user_article is None :
        
        http_exception = HTTPException (status_code = 404, 
                                        detail = "Article not read"
                                        )
            
        raise http_exception
        
    return crud_read_user_article

@app.put("/users/{user_id}/articles/", response_model = schemas.Article)
def update_article_for_user (user_id : int,
                             article_id : schemas.ArticleUpdate, 
                             db : Session = Depends (get_db)
                             ) :
    
    crud_update_user_article = crud.update_user_article (db = db,
                                                         article_id = article_id,
                                                         user_id = user_id
                                                         )
    if crud_update_user_article is None :
            
        http_exception = HTTPException (status_code = 404, 
                                        detail = "Article not update"
                                        )
        raise http_exception
        
    return crud_update_user_article

@app.delete("/users/{user_id}/articles/")
def delete_article_for_user (user_id : int, 
                             db: Session = Depends (get_db)
                            ) :
    
    crud_delete_user_article = crud.delete_user_article (db = db, 
                                                         user_id = user_id
                                                        )
    
    if crud_delete_user_article is None :
        
        http_exception = HTTPException (status_code = 404, 
                                        detail = "Article not delete"
                                        )
        raise http_exception
    
    return crud_delete_user_article