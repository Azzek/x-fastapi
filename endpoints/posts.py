from fastapi import Depends,APIRouter
from starlette import status
from pydantic_types.post_types import PostResponse, PostRequest
from models.user import User
from sqlalchemy.orm import Session
from db.database import get_db
from utils.auth import get_current_user
from services.posts import PostsService
from uuid import UUID

roter = APIRouter(
    prefix='/posts', tags=['posts']
)

@roter.post(
    '/',
    tags=['posts'], 
    description='Endpoint that creates a new note',
    status_code=status.HTTP_201_CREATED,
    response_model=PostResponse,
)
def create_post(
    post: PostRequest,
    db: Session=Depends(get_db),
    user: User=Depends(get_current_user)
    
):
    return PostsService.create(db, user, post.model_dump())

@roter.delete(
    '/{post_id}',
    tags=['posts'],
    description='Endpoint that delete a note by id',
    status_code=status.HTTP_200_OK,
    response_model=PostResponse
)

def delete_post(
    post_id: UUID,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return PostsService.delete_post(db, user, post_id)

@roter.put(
    '/{post_id}',
    tags=['posts'],
    description='Endpoint that uptade post by id',
    status_code=status.HTTP_200_OK,
    response_model=PostResponse
)
def delete_post(
    post_id: UUID,
    post_request: PostRequest,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return PostsService.update(db, user, post_request, post_id)

