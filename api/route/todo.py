from fastapi import APIRouter

todo_router = APIRouter(prefix="/api", tags=["Todo"])

@todo_router.get("/")
def todas_tarefas():
    return "Ainda não tem tarefas"

@todo_router.post("/")
def criar_todo():
    return "Ainda não há tarefas"

@todo_router.put("/{id}")
def todo_atualizar (id:int):
    return "Ainda não há tarefas"
    

@todo_router.delete("/{id}")
def deletar_tarefa(id:int):
    return "Ainda não há tarefas"