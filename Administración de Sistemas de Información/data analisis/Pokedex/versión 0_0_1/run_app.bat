@echo off
REM Script para iniciar la aplicación Streamlit
echo ========================================
echo Iniciando Pokedex App
echo ========================================
echo.

cd /d "%~dp0"

REM Verificar que json-server esté corriendo
echo Verificando json-server...
curl -s http://localhost:3000/pokemon/1 >nul 2>&1
if errorlevel 1 (
    echo WARNING: json-server no parece estar corriendo en puerto 3000
    echo La aplicacion funcionara con PokeAPI como fallback (mas lento^)
    echo.
    echo Para mejor rendimiento, ejecuta start_server.bat en otra ventana
    echo.
    timeout /t 3
)

echo (Opcional) Activando entorno virtual Python...
if exist "%~dp0\.venv\Scripts\activate.bat" (
    call "%~dp0\.venv\Scripts\activate.bat"
) else (
    echo No se encontro un entorno virtual local. Continuando con Python del sistema.
)

echo Iniciando Streamlit...
streamlit run app.py

pause
