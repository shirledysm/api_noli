from typing import Union
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr

app = FastAPI()

class Cliente(BaseModel):
    cedula: int
    nombres: str
    apellidos: str
    telefono: int
    correo: EmailStr
    tipo_cliente: int


class ClienteResponse(Cliente):
    id: int

    class Config:
        orm_mode = True


class Usuario(BaseModel):
    usuario: str
    password: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/login-cliente")
def loguear_cliente(usuario: Usuario):

    # aqui debe ir la logica que valida el usuario si este registrado,
    # y que el usuario y la contraseña son correctas

    if usuario.usuario=="" or usuario.password =="" :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={
            "mensaje": "Usuario o contraseña incorrecto"
        })


    # buscar el usuario en la base de datos y comparar la contraseña    
    return {
        "mensaje": "Usuario correcto"
    }



@app.post("/registrar-cliente", response_model=ClienteResponse, status_code=status.HTTP_201_CREATED)
def registrar_cliente(cliente: Cliente):
    return cliente.model_dump()