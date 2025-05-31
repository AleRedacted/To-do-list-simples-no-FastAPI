from fastapi import FastAPI
from api.routes.todo import todo_router

app = FastAPI()
app.include_router()

@app.get('/')
async def root():
    return {"Status": "To do list atualizada"}

