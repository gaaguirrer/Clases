from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# --- Parámetros de conexión ---
usuario = "maxlorddrakkon"
clave = "EqN3Rh8YjHqNhuU"
uri = f"mongodb+srv://{usuario}:{clave}@clusterunp.b7jhaev.mongodb.net/?retryWrites=true&w=majority&appName=ClusterUNP"

# --- Crear cliente Mongo ---
client = MongoClient(uri, server_api=ServerApi('1'))

# --- Verificar conexión ---
try:
    client.admin.command('ping')
    print("Conectado a MongoDB Atlas")

    # --- Seleccionar base de datos ---
    db = client["universidad_unp"] 

    # --- Leer e imprimir todos los estudiantes ---
    print("\n Lista de estudiantes:")
    for estudiante in db.estudiantes.find():
        print(f"- Carnet: {estudiante.get('carnet')}, Nombre: {estudiante.get('nombre')}, Correo: {estudiante.get('correo')}, Teléfono: {estudiante.get('telefono')}")

except Exception as e:
    print("Error al conectar o consultar:", e)