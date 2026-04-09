from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Reemplaza estos datos con los tuyos
usuario = "maxlorddrakkon"
clave = "EqN3Rh8YjHqNhuU"

uri = f"mongodb+srv://{usuario}:{clave}@clusterunp.b7jhaev.mongodb.net/?retryWrites=true&w=majority&appName=ClusterUNP"

# Crear el cliente
client = MongoClient(uri, server_api=ServerApi('1'))

# Verificar conexión
try:
    client.admin.command('ping')
    print("✅ ¡Conectado correctamente a MongoDB Atlas!")
except Exception as e:
    print("❌ Error al conectar:", e)
