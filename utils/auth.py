from fastapi import Request, Response, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from models.user import User
from services.jwt import decode_access_token
import config
from db.database import get_db
from uuid import UUID

def get_current_user(request:Request, response:Response, db:Session = Depends(get_db)) -> User: 
    
    token = request.cookies.get(config.ACCESS_COOKIE_NAME)
    
    if not token:
        raise HTTPException(status_code=401, detail='Token not found')
        
    try:
        
        user_id = decode_access_token(token)
      
        stmt = select(User).where(User.id == UUID(user_id))
        user = db.scalars(stmt).first()
        
        if user.is_banned:
            raise HTTPException(status_code=403, detail='Banned user')
        
        return user
    
    except Exception as e:
            response.delete_cookie(config.ACCESS_COOKIE_NAME)
            response.delete_cookie(config.REFRESH_COOKIE_NAME)
            raise HTTPException(status_code=401, detail='Invalid or expired token')
            