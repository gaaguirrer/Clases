# backend/src/routes/app.py

from fastapi import FastAPI, HTTPException
from src.models import Estudiante
from src.db.mongo import db
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Habilitar CORS si tienes frontend separado
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Colección
coleccion = db.estudiantes

# Leer todos
@app.get("/estudiantes")
def obtener_estudiantes():
    estudiantes = []
    for est in coleccion.find():
        est["_id"] = str(est["_id"])
        estudiantes.append(est)
    return estudiantes

# Crear
@app.post("/estudiantes")
def crear_estudiante(estudiante: Estudiante):
    resultado = coleccion.insert_one(estudiante.dict())
    return {"_id": str(resultado.inserted_id)}

# Leer uno
@app.get("/estudiantes/{carnet}")
def obtener_estudiante(carnet: str):
    est = coleccion.find_one({"carnet": carnet})
    if est:
        est["_id"] = str(est["_id"])
        return est
    raise HTTPException(status_code=404, detail="Estudiante no encontrado")

# Actualizar
@app.put("/estudiantes/{carnet}")
def actualizar_estudiante(carnet: str, estudiante: Estudiante):
    result = coleccion.update_one({"carnet": carnet}, {"$set": estudiante.dict()})
    if result.modified_count:
        return {"mensaje": "Estudiante actualizado"}
    raise HTTPException(status_code=404, detail="Estudiante no encontrado")

# Eliminar
@app.delete("/estudiantes/{carnet}")
def eliminar_estudiante(carnet: str):
    result = coleccion.delete_one({"carnet": carnet})
    if result.deleted_count:
        return {"mensaje": "Estudiante eliminado"}
    raise HTTPException(status_code=404, detail="Estudiante no encontrado")
