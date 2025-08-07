from sqlalchemy import String,Integer,Column,Boolean,ForeignKey,TIMESTAMP,text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class Post(base):
    __tablename__ ="posts"
    id = Column(Integer,nullable=False,primary_key=True,index=True)
    title =Column(String,nullable=False)
    content =Column(String,nullable=False)
    published = Column(Boolean,default=True)
    create_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('Now()'))
    # owner_id =Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    # onwer = relationship("user")

class user (base):
    __tablename__="users"
    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,unique=True,nullable=False)
    password = Column(String,nullable=False)
    create_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('Now()'))

