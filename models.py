from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey,Text,String
from typing import List

class Base(DeclarativeBase):
    pass
 
class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(30),nullable=False)
    email: Mapped[str]
    
    comments:Mapped[List["Comment"]] =relationship(back_populates="user",cascade="all, delete-orphan")
    
    def __repr__(self)->str:
        return f"User(id={self.id!r}, name={self.user_name!r}, email={self.email!r})"
        
    
class Comment(Base):
    __tablename__ = 'comments'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"),nullable=False)
    text: Mapped[str] = mapped_column(Text,nullable=False)
    
    user:Mapped["User"]=relationship(back_populates="comments")

    def __repr__(self)->str:
        return f"Comment(text={self.text!r} by {self.user.user_name})"