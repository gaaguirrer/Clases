@echo off
REM Script para iniciar json-server con la base de datos de Pokémon
echo ========================================
echo Iniciando JSON Server - Pokedex Backend
echo ========================================
echo.
echo Puerto: 3000
echo Base de datos: data/db.json
echo.

cd /d "%~dp0"

if not exist "data\db.json" (
    echo ERROR: No se encontro data\db.json
    echo Por favor ejecuta primero: python scripts/populate_db.py --generation 1
    pause
    exit /b 1
)

echo Iniciando servidor con npx...
call npx json-server --watch data/db.json --port 3000 --host localhost

pause
