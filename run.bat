@echo off

setlocal ENABLEDELAYEDEXPANSION

:: Fecha en formato YYYY-MM-DD
for /f %%i in ('powershell -Command "Get-Date -Format yyyy-MM-dd"') do set FECHA=%%i


echo Activando entorno virtual...
REM Ajustá esta ruta si tu venv está en otra carpeta
call .\.venv\Scripts\activate

echo Entorno virtual activado.
echo Ejecutando main.py...

python main.py

:: Verificá que el CV fue generado
if exist .\data\CV_Matias_Perez_Nauto.pdf (
    echo ✅ CV generado correctamente.
) else (
    echo ❌ No se encontró el archivo de CV generado.
    goto end
)

echo.
echo 📦 Realizando commit y push a GitHub...

git add .
git commit -m "%FECHA% Actualizando CV"
git push

:end
echo.
echo ✅ Repositorio actualizado en GitHub.


echo ✨ Proceso completado. Presiona una tecla para salir...
pause >nul
