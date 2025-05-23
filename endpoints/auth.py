from fastapi import APIRouter, Request, Depends, HTTPException, Response
from starlette import status
from services.google_oauth import oauth, get_user_from_google
from sqlalchemy.orm import Session
from db.database import get_db
from models.user import User
from services.jwt import create_access_token, create_refresh_token
import config


router = APIRouter(prefix='/auth')


@router.get('/google', status_code=status.HTTP_200_OK)
async def login_by_google(request:Request):
    redirect_uri = request.url_for('auth_callback')
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get('/google/callback', name='auth_callback')
async def google_auth_callback(request: Request, response: Response, db: Session = Depends(get_db)):
    user_data = await get_user_from_google(request)

    if not user_data:
        raise HTTPException(status_code=400, detail="Google authentication failed")

    sub = user_data['sub']
    email = user_data['email']
    username = user_data['name'] 
    avatar_url = user_data.get('picture')

    db_user = db.query(User).filter(User.google_id == sub).first()

    if not db_user:
        db_user = User(
            google_id=sub,
            email=email,
            username=username,
            avatar_url=avatar_url
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

    access_token = create_access_token({
        'sub': str(db_user.id),
        'username': db_user.username,
        'email': db_user.email
    })
    
    refresh_token = create_refresh_token({
        'sub': str(db_user.id),
        'username': db_user.username,
        'email': db_user.email
    })

    response.set_cookie(
        config.REFRESH_COOKIE_NAME,
        refresh_token,
        httponly=True,
        max_age=60 * 60 * 24 * config.REFRESH_TOKEN_EXPIRE_DAYS,
        secure=False,
        samesite="strict"
    )
    response.set_cookie(
        config.ACCESS_COOKIE_NAME,
        access_token,
        httponly=True,
        max_age=60 * config.ACCESS_TOKEN_EXPIRE_MINUTES,
        secure=False,
        samesite="strict"
    )