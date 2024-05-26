from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db import CategoryCRUD, TagCRUD, AuthorCRUD, PostCRUD

app = FastAPI()


@app.post("/create_post/", tags=["Posts"])
def create_category(title: str, content: str, author_id: int, category_id: int):
    result = PostCRUD.create(title=title, content=content, author_id=author_id, category_id=category_id)
    if result == 0:
        return {"message": "Запись данных выполнена успешно"}
    elif result == 1:
        return {"message": "Категория уже существует"}
    elif result == -2:
        return {"message": "Вы указали несуществующего автора или категорию"}
    else:
        return {"message": "Что-то пошло не так"}


@app.get("/read_post/", tags=["Posts"])
def read_category():
    result = PostCRUD.read()
    if result == -1:
        return {"message": "Что-то пошло не так"}
    else:
        out = {}
        for el in result:
            out[el.id] = el.title

        return out


@app.post("/update_post/", tags=["Posts"])
def update_category(post_id: int, new_title: str):
    result = PostCRUD.update(post_id, new_title)
    if result == 0:
        return {"message": "Запись успешно обновлена"}
    else:
        return {"message": "Что-то пошло не так"}


@app.post("/delete_post/", tags=["Posts"])
def delete_category(post_id: int):
    result = PostCRUD.delete(post_id)
    if result == 0:
        return {"message": f"Запись успешно удалена"}
    else:
        return {"message": "Что-то пошло не так"}


@app.post("/create_category/", tags=["Categories"])
def create_category(name: str):
    result = CategoryCRUD.create(name=name)
    if result == 0:
        return {"message": "Запись данных выполнена успешно"}
    elif result == 1:
        return {"message": "Категория уже существует"}
    else:
        return {"message": "Что-то пошло не так"}


@app.get("/read_category/", tags=["Categories"])
def read_category():
    result = CategoryCRUD.read()
    if result == -1:
        return {"message": "Что-то пошло не так"}
    else:
        out = {}
        for el in result:
            out[el.id] = el.name

        return out


@app.post("/update_category/", tags=["Categories"])
def update_category(category_id: int, new_name: str):
    result = CategoryCRUD.update(category_id, new_name)
    if result == 0:
        return {"message": "Запись успешно обновлена"}
    else:
        return {"message": "Что-то пошло не так"}


@app.post("/delete_category/", tags=["Categories"])
def delete_category(category_id: int):
    result = CategoryCRUD.delete(category_id)
    if result == 0:
        return {"message": f"Запись успешно удалена"}
    else:
        return {"message": "Что-то пошло не так"}


@app.post("/create_tag/", tags=["Tags"])
def create_tag(name: str):
    result = TagCRUD.create(name=name)
    if result == 0:
        return {"message": "Запись данных выполнена успешно"}
    elif result == 1:
        return {"message": "Тег уже существует"}
    else:
        return {"message": "Что-то пошло не так"}


@app.get("/read_tag/", tags=["Tags"])
def read_tag():
    result = TagCRUD.read()
    if result == -1:
        return {"message": "Что-то пошло не так"}
    else:
        out = {}
        for el in result:
            out[el.id] = el.name

        return out


@app.post("/update_tag/", tags=["Tags"])
def update_tag(tag_id: int, new_name: str):
    result = TagCRUD.update(tag_id, new_name)
    if result == 0:
        return {"message": "Запись успешно обновлена"}
    else:
        return {"message": "Что-то пошло не так"}


@app.post("/delete_tag/", tags=["Tags"])
def delete_tag(delete_id: int):
    result = TagCRUD.delete(delete_id)
    if result == 0:
        return {"message": f"Запись успешно удалена"}
    else:
        return {"message": "Что-то пошло не так"}


@app.post("/create_author/", tags=["Authors"])
def create_tag(name: str):
    result = AuthorCRUD.create(name=name)
    if result == 0:
        return {"message": "Запись данных выполнена успешно"}
    elif result == 1:
        return {"message": "Автор уже существует"}
    else:
        return {"message": "Что-то пошло не так"}


@app.get("/read_author/", tags=["Authors"])
def read_author():
    result = AuthorCRUD.read()
    if result == -1:
        return {"message": "Что-то пошло не так"}
    else:
        out = {}
        for el in result:
            out[el.id] = el.name

        return out


@app.post("/update_author/", tags=["Authors"])
def update_author(author_id: int, new_name: str):
    result = AuthorCRUD.update(author_id, new_name)
    if result == 0:
        return {"message": "Запись успешно обновлена"}
    else:
        return {"message": "Что-то пошло не так"}


@app.post("/delete_author/", tags=["Authors"])
def delete_author(author_id: int):
    result = AuthorCRUD.delete(author_id)
    if result == 0:
        return {"message": f"Запись успешно удалена"}
    else:
        return {"message": "Что-то пошло не так"}


if __name__ == "__main__":
    pass
