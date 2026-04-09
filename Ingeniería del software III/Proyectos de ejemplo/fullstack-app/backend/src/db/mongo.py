from pymongo import MongoClient
from pymongo.server_api import ServerApi

usuario = "maxlorddrakkon"
clave = "EqN3Rh8YjHqNhuU"
uri = f"mongodb+srv://{usuario}:{clave}@clusterunp.b7jhaev.mongodb.net/?retryWrites=true&w=majority&appName=ClusterUNP"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client["universidad_unp"]
