from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
from pymongo.server_api import ServerApi

app = FastAPI()

# Configurar CORS para permitir solicitudes desde todas las fuentes (esto es para desarrollo, en producción, deberías restringirlo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Puedes reemplazar "*" con la URL de tu aplicación React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configura tu conexión a MongoDB Atlas
client = MongoClient("mongodb+srv://ocontreras:onesmile159@cluster0.ug30h2w.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))

# Selecciona la base de datos y la colección
db = client.Joyeria 
users_collection = db.CuentaUsuario

class User(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(user: User):
    # Aquí puedes realizar la autenticación y otras lógicas según tus necesidades
    # Por ejemplo, puedes verificar las credenciales en la colección de usuarios
    user_data = users_collection.find_one({"Username": user.username, "Password": user.password})
    if not user_data:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    return {"message": "Login exitoso"}
