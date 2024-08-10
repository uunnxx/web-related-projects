from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

from todo.models.models import Todo, TodoPydantic, TodoInPydantic


class Status(BaseModel):
    message: str


app = FastAPI()


@app.get('/')
async def read_root():
    return {'Hello': 'World'}


@app.get('/todos', response_model=list[TodoPydantic])
async def get_todos():
    return await TodoPydantic.from_queryset(Todo.all())


@app.get('/todos/{todo_id}', response_model=TodoPydantic, responses={404: {'model': HTTPNotFoundError}})
async def get_todo(todo_id: int):
    return await TodoPydantic.from_queryset_single(Todo.get(id=todo_id))


@app.post('/todos', response_model=TodoPydantic)
async def create_todo(todo: TodoInPydantic):
    todo_object = await Todo.create(**todo.dict(exclude_unset=True))
    return await TodoPydantic.from_tortoise_orm(todo_object)


@app.put('/todos/{todo_id}', response_model=TodoPydantic, responses={404: {'model': HTTPNotFoundError}})
async def update_todo(todo_id: int, todo: TodoInPydantic):
    await Todo.filter(id=todo_id).update(**todo.dict(exclude={'id'}, exclude_unset=True))
    return await TodoPydantic.from_queryset_single(Todo.get(id=todo_id))


register_tortoise(
    app,
    db_url="postgres://postgres:postgres@0.0.0.0:5432/fastapi_todo",
    modules={'models': ['todo.models.models']},
    generate_schemas=True,
    add_exception_handlers=True,
)
