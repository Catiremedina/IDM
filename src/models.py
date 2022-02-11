import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    username = Column(String(250))
    email = Column(String(250), nullable=False)
    password = Column(String(50), nullable=False)
    online = Column(Boolean, unique=False, default=False)
    
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    user = relationship(User)
    likes = Column(Integer, nullable=False)
    user_id = Column(Integer,ForeignKey('user.id'))

class Photo(Base):
    __tablename__ = 'photo'
    id = Column(Integer, primary_key=True)
    url = Column(String(250))
    post = relationship(Post)
    post_id = Column(Integer,ForeignKey('post.id'))
   
class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment = Column(String(250)) 
    user = relationship(User)
    user_id = Column(Integer,ForeignKey('user.id'))
    post = relationship(Post)
    post_id = Column(Integer,ForeignKey('post.id'))
   
    
class Follower (Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, nullable=False)
    user_id= Column(Integer, ForeignKey("user.id"))
    user= relationship("User", back_populates="children")

class Following (Base):
    __tablename__ = 'following'
    id = Column(Integer, primary_key=True)
    following_id = Column(Integer, nullable=False)
    user_id= Column(Integer, ForeignKey("user.id"))
    user= relationship("User", back_populates="children")




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')