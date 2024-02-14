from sqlalchemy.orm import Session

from . import models, schemas


# def get_user (db : Session, 
#               user_id : int) :
    
#     db_query = db.query (models.User).filter (models.User.id == user_id).first ()
    
#     return db_query

# def get_user_by_email (db : Session, 
#                       email : str) :
    
#     db_query = db.query (models.User).filter (models.User.email == email).first ()
    
#     return db_query

def get_users (db : Session, 
               skip : int = 0, 
               limit : int = 100
               ) :
    
    db_query = db.query (models.User).offset (skip).limit (limit).all ()
    
    return db_query

def create_user (db : Session, 
                 user : schemas.UserCreate
                 ) :
    
    db_user = models.User (email = user.email, 
                           password = user.password)
    
    db.add (db_user)
    db.commit ()
    db.refresh (db_user)
    
    return db_user

def read_user (db : Session, 
               user_id : int
               ) :
    
        db_query = db.query (models.User).filter (models.User.id == user_id).first ()
    
        return db_query

def update_user (db : Session, 
                 user: schemas.UserUpdate,
                 user_id : int
                 ) :
        
    db_user = db.query (models.User).filter (models.User.id == user_id).first ()
    
    if db_user:
        
        for key, value in user.dict().items():
                
            setattr (db_user, 
                     key, 
                     value)
            
        db.commit ()
        db.refresh (db_user)
            
        return db_user

def delete_user (db: Session, 
                 user_id: int
                ) :
    
    db_user = db.query (models.User).filter (models.User.id == user_id).first ()
    
    if db_user :
        
        db.delete (db_user)
        db.commit()
    
    return db_user

def get_articles (db : Session, 
                  skip : int = 0, 
                  limit: int = 100
                  ) : 
    
    db_query = db.query (models.Article).offset (skip).limit (limit).all ()

    return db_query

def create_user_article (db : Session, 
                         article_id : schemas.ArticleCreate, 
                         user_id : int
                        ) :
    
    db_article = models.Article (**article_id.dict (), 
                                 owner_id = user_id)
    
    db.add (db_article)
    db.commit ()
    db.refresh (db_article)
    
    return db_article

def read_user_article (db : Session, 
                       article_id : int, 
                       user_id : int
                       ) :
    
    db_query = db.query (models.Article).filter (models.Article.id == article_id, 
                                                 models.Article.owner_id == user_id).first ()
    
    return db_query

def update_user_article (db : Session,
                         article_id : schemas.ArticleUpdate,  
                         user_id : int 
                        ) :
    
    db_article = db.query (models.Article).filter (models.Article.id == article_id, 
                                                   models.Article.owner_id == user_id).first ()

    if db_article :
            
        for key, value in article_id.dict ().items ():
                
            setattr (db_article, 
                     key, 
                     value)

        db.commit ()
        db.refresh (db_article)

    return db_article

def delete_user_article (db : Session, 
                         user_id: int
                        ) :
    
    db_user = db.query (models.Article).filter (models.Article.owner_id == user_id).first ()

    if db_user :
        
        db.delete (db_user)
        db.commit ()

    return db_user