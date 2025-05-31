from fastapi import APIRouter,HTTPException
from api.models.todo import Todo
from api.schemas.todo import GetTodo, PostTodo,PutTodo

todo_router = APIRouter(prefix="/api", tags=["Todo"])

@todo_router.get("/")
async def todas_tarefas():
    data = Todo.all()
    return await GetTodo.from_queryset(Todo.all(data))

@todo_router.post("/")
async def criar_todo(body: PostTodo):
    row = await Todo.create(**body.dict(exclude_unset=True))
    return await GetTodo.from_tortoise_orm(row)

@todo_router.put("/{id}")
async def todo_atualizar (id:int, body: PutTodo):
    data = body.dict(exclude_unset=True)
    exists = await Todo.filter(id=key).exists()
    if not exists:
        raise HTTPException(status_code = ()
    return "Ainda não há tarefas"    

#ainda trabalhando aqui
@todo_router.delete("/{id}")
async def deletar_tarefa(id:int):
    return "Ainda não há tarefas"
