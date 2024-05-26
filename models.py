from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///blog.db', echo=True)

Base = declarative_base()


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    author = relationship("Author", back_populates="posts")
    category = relationship("Category", back_populates="posts")


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    posts = relationship("Post", back_populates="category")


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    posts = relationship("Post", back_populates="author")


if __name__ == '__main__':
    Base.metadata.create_all(engine)
