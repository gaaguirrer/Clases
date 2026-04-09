from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Conexión
usuario = "maxlorddrakkon"
clave = "EqN3Rh8YjHqNhuU"
uri = f"mongodb+srv://{usuario}:{clave}@clusterunp.b7jhaev.mongodb.net/?retryWrites=true&w=majority&appName=ClusterUNP"
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("✅ Conectado a MongoDB Atlas")

    db = client["universidad_unp"]  # Base de datos

    # 1. Estudiantes
    db.estudiantes.insert_many([
        {"carnet": "2023-001", "nombre": "Ana Pérez", "correo": "ana@unp.edu.ni", "telefono": "87221100"},
        {"carnet": "2023-002", "nombre": "Carlos López", "correo": "carlos@unp.edu.ni", "telefono": "87551122"}
    ])

    # 2. Recinto
    db.recinto.insert_many([
        {"nombre": "Rivas", "telefono": "25601234"},
        {"nombre": "Estelí", "telefono": "27114567"}
    ])

    # 3. Docente
    db.docentes.insert_many([
        {
            "nombre": "Ing. María Torres",
            "materias": ["Matemática I", "Programación"],
            "correo": "maria.torres@unp.edu.ni",
            "telefono": "88112233"
        }
    ])

    # 4. Administrativo
    db.administrativos.insert_many([
        {
            "nombre": "Luis González",
            "correo": "luis.gonzalez@unp.edu.ni",
            "telefono": "88990011"
        }
    ])

    # 5. Grupo
    db.grupos.insert_many([
        {
            "nombre": "ISI-I-SAB",
            "estudiantes": ["2023-001", "2023-002"]  # carnets como referencia
        }
    ])

    # 6. Carrera
    db.carreras.insert_one({
        "nombre": "Ingeniería en Sistemas de Información",
        "grupos": ["ISI-I-SAB"]
    })

    # 7. Asignatura
    db.asignaturas.insert_one({
        "nombre": "Introducción a la Electrónica",
        "grupo": "ISI-I-SAB",
        "docente": "Ing. María Torres",
        "aula": "Aula 4",
        "horario": "Sábado 8:00-12:00"
    })

    # Ver colecciones creadas
    print("\n📁 Colecciones en la base 'universidad_unp':")
    for nombre in db.list_collection_names():
        print(" -", nombre)

except Exception as e:
    print("❌ Error:", e)
