@echo off
echo Activando entorno virtual...

REM Ajustá esta ruta si tu venv está en otra carpeta
call .\.venv\Scripts\activate

echo Entorno virtual activado.
echo Ejecutando main.py...

python main.py

echo.
echo ✨ Proceso completado. Presiona una tecla para salir...
pause >nul