from pydantic import BaseModel

class ArticleBase (BaseModel) :
    
    title : str
    description : str | None = None

class Article (ArticleBase) : 
    
    id : int
    owner_id : int

    class Config :
        
        from_attributes = True
        
class ArticleCreate (ArticleBase) :
    
    pass
    
class ArticleUpdate (ArticleBase) :
        
        id : int
        owner_id : int

class UserBase (BaseModel) :
    
    email: str

class User (UserBase) :
    
    id : int
    is_active : bool
    articles : list [Article] = []

    class Config :
        
        from_attributes = True

class UserCreate (UserBase) :
    
    password : str

class UserUpdate (UserBase) :
        
    password : str | None = None