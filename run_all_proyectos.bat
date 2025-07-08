@echo off
setlocal ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION

:: Marcar inicio
for /f %%i in ('powershell -Command "[int]((Get-Date).ToUniversalTime() - [datetime]'1970-01-01').TotalSeconds"') do set START=%%i

echo ===================================================
echo [INFO] Activando entorno virtual...
call .\.venv\Scripts\activate

if errorlevel 1 (
    echo ❌ No se pudo activar el entorno virtual.
    goto end
)

echo ---------------------------------------------------
echo [INFO] Entorno virtual activado correctamente.
echo [RUN] Ejecutando get_all_repositorios.py...

python get_all_repositorios.py

if errorlevel 1 (
    echo ❌ El script Python falló durante la ejecución.
    goto end
)

echo ---------------------------------------------------
echo Realizando commit y push a GitHub...

git diff --quiet
if errorlevel 1 (
    git add .
    git commit -m "%FECHA% Actualizando CV"
    git push
) else (
    echo No hay cambios para subir a GitHub.
)

:: Marcar fin
for /f %%i in ('powershell -Command "[int]((Get-Date).ToUniversalTime() - [datetime]'1970-01-01').TotalSeconds"') do set END=%%i
set /a DURATION=!END! - !START!

echo ---------------------------------------------------
echo ✅ Proceso completado exitosamente.
echo 🕒 Duración total: !DURATION! segundos
echo ===================================================

:end
echo.
echo Presiona una tecla para salir...
pause >nul