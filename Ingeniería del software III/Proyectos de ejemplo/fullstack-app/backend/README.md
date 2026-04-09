# Backend Application

Este directorio contiene el código fuente del backend de la aplicación, que está construido utilizando Flask y se conecta a una base de datos MongoDB.

## Estructura del Proyecto

- **src/app.py**: Punto de entrada de la aplicación. Configura Flask y las rutas.
- **src/models/**: Contiene los modelos de datos que representan las colecciones de MongoDB.
- **src/routes/**: Define las rutas de la aplicación y maneja las solicitudes HTTP.
- **src/db/mongo.py**: Maneja la conexión a la base de datos MongoDB.

## Requisitos

Asegúrate de tener instaladas las siguientes dependencias:

- Flask
- PyMongo

Puedes instalar las dependencias ejecutando:

```
pip install -r requirements.txt
```

## Ejecución

Para ejecutar la aplicación, utiliza el siguiente comando:

```
python src/app.py
```

La aplicación estará disponible en `http://localhost:5000`.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.