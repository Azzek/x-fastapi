from models.user import User
import config
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import HTTPException

def create_access_token(data:dict):
    
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=int(config.ACCESS_TOKEN_EXPIRE_MINUTES))
    
    to_encode['exp'] = expire
    encoded_jwt = jwt.encode(to_encode, str(config.ACCESS_SECRET), algorithm=config.JWT_ALGORITHM)
    
    return encoded_jwt


def create_refresh_token(data:dict):
    
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=int(config.REFRESH_TOKEN_EXPIRE_DAYS))
    
    to_encode['exp'] = expire
    encoded_jwt = jwt.encode(to_encode, str(config.REFRESH_SECRET), algorithm=config.JWT_ALGORITHM)
    
    return encoded_jwt
        
        
def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, str(config.ACCESS_SECRET), algorithms=[config.JWT_ALGORITHM])
        user_id = payload.get('sub')
       
        if not user_id:
            raise HTTPException(status_code=401, detail='Invalid token: user ID not found')
        return user_id

    except JWTError:
        raise HTTPException(status_code=401, detail='Invalid or expired token')