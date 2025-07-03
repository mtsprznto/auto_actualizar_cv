@echo off
setlocal ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION

:: Obtener fecha en formato YYYY-MM-DD
for /f %%i in ('powershell -Command "Get-Date -Format yyyy-MM-dd"') do set FECHA=%%i

:: Guardar hora de inicio (en segundos desde epoch)
for /f %%i in ('powershell -Command "[int](Get-Date -UFormat %%s)"') do set START=%%i

echo ===================================================
echo 🔄 Activando entorno virtual...
call .\.venv\Scripts\activate

echo ---------------------------------------------------
echo ✅ Entorno virtual activado.
echo 🚀 Ejecutando main.py...

python main.py

echo ---------------------------------------------------
:: Verificar que se haya generado el CV
if exist .\data\CV_Matias_Perez_Nauto.pdf (
    echo 📄 CV generado correctamente.
) else (
    echo ❌ No se encontró el archivo de CV generado.
    goto end
)

echo ---------------------------------------------------
echo 📦 Realizando commit y push a GitHub...

git add .
git commit -m "%FECHA% Actualizando CV"
git push

:: Calcular duración del proceso
for /f %%i in ('powershell -Command "[int](Get-Date -UFormat %%s)"') do set END=%%i
set /a DURATION=!END! - !START!

echo ===================================================
echo ✅ Repositorio actualizado en GitHub.
echo 🕒 Duración total del proceso: !DURATION! segundos
echo ===================================================

:end
echo.
echo ✨ Proceso completado. Presiona una tecla para salir...
pause >nul