# Fullstack Application

Este proyecto es una aplicación fullstack que utiliza Python con Flask para el backend y React para el frontend, con MongoDB como base de datos.

## Estructura del Proyecto

```
fullstack-app
├── backend
│   ├── src
│   │   ├── app.py
│   │   ├── models
│   │   │   └── __init__.py
│   │   ├── routes
│   │   │   └── __init__.py
│   │   └── db
│   │       └── mongo.py
│   ├── requirements.txt
│   └── README.md
├── frontend
│   ├── src
│   │   ├── App.jsx
│   │   ├── components
│   │   │   └── index.jsx
│   │   └── pages
│   │       └── Home.jsx
│   ├── package.json
│   └── README.md
└── README.md
```

## Requisitos

- Python 3.x
- Node.js
- MongoDB

## Instalación

### Backend

1. Navega al directorio del backend:
   ```
   cd backend
   ```

2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación:
   ```
   python src/app.py
   ```

### Frontend

1. Navega al directorio del frontend:
   ```
   cd frontend
   ```

2. Instala las dependencias:
   ```
   npm install
   ```

3. Ejecuta la aplicación:
   ```
   npm start
   ```

## Uso

Accede a la aplicación en tu navegador en `http://localhost:3000` para el frontend y `http://localhost:5000` para el backend.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cambios.

## Licencia

Este proyecto está bajo la Licencia MIT.