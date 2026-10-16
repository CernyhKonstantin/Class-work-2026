from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    """
    This endpoint return greeting
    """
    return {"message":"Hello from FastAPI"}

@app.get('/info/{id}')
def info(id:str):
    """
    This echo endpoint. Send id
    
    Args:
        id: uuid format
    """
    return {"info_id": id}

# uvicorn - сервер
"""
main - назва файлу для запуска
app - об'єкт додатку
--reload флаг, перезавантажувати сервер після змін у коді

uvicorn main:app --reload
"""