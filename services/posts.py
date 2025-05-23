from fastapi import HTTPException
from models.post import Post
from models.user import User
from sqlalchemy.orm import Session
from sqlalchemy import select
from pydantic_types.post_types import PostResponse, PostRequest
from uuid import UUID
from fastapi import status

class PostsService:
    
    @staticmethod
    def create(db: Session, user: User, post: dict) -> PostResponse:
        reply_of = None
        reply_to = None
        
        # Validation reply_of
        if post.get('reply_of'):
            smtp = select(Post).where(Post.id == post['reply_of'])
            reply_of_post_model = db.scalars(smtp).first()
            if not reply_of_post_model:
                raise HTTPException(status_code=404, detail='Post not found')
            if reply_of_post_model.reply_to:
                raise HTTPException(status_code=401, detail='First post cannot be a reply')

        # Determining the response via respond_to
        if post.get('reply_to'):
            smtp = select(Post).where(Post.id == post['reply_to'])
            reply_post = db.scalars(smtp).first()
            if not reply_post:
                raise HTTPException(status_code=404, detail='Reply-to post not found')
            reply_of = reply_post.reply_of or reply_post
            reply_to = reply_post
            
        new_post = Post(
            author_id=user.id,
            content=post['content'],
            reply_to=reply_to,
            reply_of=reply_of
        )

        db.add(new_post)
        db.commit()
        db.refresh(new_post)

        return PostResponse(msg='ok', post_id=new_post.id)


    @staticmethod
    def delete_post(db: Session, user: User, post_id: UUID) -> PostResponse:
        stmt = select(Post).where(Post.id == post_id)
        post = db.scalars(stmt).first()

        if not post:
            raise HTTPException(status_code=404, detail='Post not found')

        if post.author_id != user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Post does not belong to this user')

        db.delete(post)
        db.commit()

        return PostResponse(msg='ok')
    
    
    @staticmethod
    def update(db: Session, user: User, post_request: PostRequest, post_id):
        post_data = post_request.model_dump()
        
        smtp = select(Post).where(Post.id == post_id)
        post = db.scalars(smtp).first()
        
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post not found')
        
        if post.author_id != user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Post does not belong to this user')
        
        post.content = post_request.content
        
        db.add(post)
        db.commit()
        
        return PostResponse(msg='ok', post_id=post.id)
        