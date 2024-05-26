from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Post, Category, Tag, Author

engine = create_engine('sqlite:///blog.db')
Session = sessionmaker(bind=engine)


class PostCRUD:
    @classmethod
    def create(cls, title, content, author_id, category_id):
        try:
            session = Session()
            print(int(category_id), [int(category.id) for category in session.query(Category).all()], int(author_id), [int(author.id) for author in session.query(Author).all()])
            if (int(category_id) not in [int(category.id) for category in session.query(Category).all()]) or (int(author_id) not in [int(author.id) for author in session.query(Author).all()]):
                return -2  # connection error

            posts = session.query(Post).all()
            posts = [post.title for post in posts]
            if title in posts:
                return 1  # category exists

            post = Post(title=title, content=content, author_id=author_id, category_id=category_id)
            session.add(post)
            session.commit()
            session.close()
            return 0  # all right
        except Exception as e:
            print(e)
            return -1  # something went wrong

    @classmethod
    def read(cls):
        try:
            session = Session()
            posts = session.query(Post).all()
            session.close()
            return posts  # all right
        except Exception as e:
            print(e)
            return -1  # something went wrong

    @classmethod
    def update(cls, post_id, title=None, content=None, author_id=None, category_id=None):
        try:
            session = Session()
            post = session.query(Post).filter(Post.id == post_id).first()
            if title:
                post.title = title
            if content:
                post.content = content
            if author_id:
                post.author_id = author_id
            if category_id:
                post.category_id = category_id
            session.commit()
            session.close()
            return 0  # all right
        except Exception as e:
            print(e)
            return -1  # something went wrong

    @classmethod
    def delete(cls, post_id):
        try:
            session = Session()
            post = session.query(Post).filter(Post.id == post_id).first()
            session.delete(post)
            session.commit()
            session.close()
            return 0  # all right
        except Exception as e:
            print(e)
            return -1  # something went wrong


class CategoryCRUD:
    @classmethod
    def create(cls, name):
        try:
            session = Session()
            categories = session.query(Category).all()
            categories = [category.name for category in categories]
            if name in categories:
                return 1  # category exists

            category = Category(name=name)
            session.add(category)
            session.commit()
            session.close()
            return 0  # all right
        except Exception as e:
            print(e)
            return -1  # something went wrong

    @classmethod
    def read(cls):
        try:
            session = Session()
            categories = session.query(Category).all()
            session.close()
            return categories
        except Exception as e:
            print(e)
            return -1  # something went wrong

    @classmethod
    def update(cls, category_id, name):
        try:
            session = Session()
            category = session.query(Category).filter(Category.id == category_id).first()
            category.name = name
            session.commit()
            session.close()
            return 0  # all right
        except Exception as e:
            print(e)
            return -1  # something went wrong

    @classmethod
    def delete(cls, category_id):
        try:
            session = Session()
            category = session.query(Category).filter(Category.id == category_id).first()
            session.delete(category)
            session.commit()
            session.close()
            return 0
        except Exception as e:
            print(e)
            return -1  # something went wrong


class TagCRUD:
    @classmethod
    def create(cls, name):
        try:
            session = Session()

            tags = [category.name for category in session.query(Tag).all()]
            if name in tags:
                return 1  # category exists

            tag = Tag(name=name)
            session.add(tag)
            session.commit()
            session.close()
            return 0  # all right
        except Exception as e:
            print(e)
            return -1  # something went wrong

    @classmethod
    def read(cls):
        try:
            session = Session()
            tags = session.query(Tag).all()
            session.close()
            return tags
        except Exception as e:
            print(e)
            return -1  # something went wrong

    @classmethod
    def update(cls, tag_id, name):
        try:
            session = Session()
            tag = session.query(Tag).filter(Tag.id == tag_id).first()
            tag.name = name
            session.commit()
            session.close()
            return 0  # all right
        except Exception as e:
            print(e)
            return -1  # something went wrong

    @classmethod
    def delete(cls, tag_id):
        try:
            session = Session()
            tag = session.query(Tag).filter(Tag.id == tag_id).first()
            session.delete(tag)
            session.commit()
            session.close()
            return 0
        except Exception as e:
            print(e)
        return -1  # something went wrong



class AuthorCRUD:
    @classmethod
    def create(cls, name):
        try:
            session = Session()

            authors = [category.name for category in session.query(Author).all()]
            if name in authors:
                return 1  # category exists

            author = Author(name=name)
            session.add(author)
            session.commit()
            session.close()
            return 0  # all right
        except Exception as e:
            print(e)
            return -1  # something went wrong

    @classmethod
    def read(cls):
        try:
            session = Session()
            authors = session.query(Author).all()
            session.close()
            return authors
        except Exception as e:
            print(e)
            return -1  # something went wrong

    @classmethod
    def update(cls, author_id, name):
        try:
            session = Session()
            author = session.query(Author).filter(Author.id == author_id).first()
            author.name = name
            session.commit()
            session.close()
            return 0  # all right
        except Exception as e:
            print(e)
            return -1  # something went wrong

    @classmethod
    def delete(cls, author_id):
        try:
            session = Session()
            author = session.query(Author).filter(Author.id == author_id).first()
            session.delete(author)
            session.commit()
            session.close()
            return 0
        except Exception as e:
            print(e)
            return -1  # something went wrong


if __name__ == '__main__':
    pass
