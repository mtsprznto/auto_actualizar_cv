@echo off
setlocal ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION


:: Obtener fecha en formato YYYY-MM-DD
for /f %%i in ('powershell -Command "Get-Date -Format yyyy-MM-dd"') do set FECHA=%%i

:: Guardar hora de inicio (en segundos desde epoch)
for /f %%i in ('powershell -Command "[int]((Get-Date).ToUniversalTime() - [datetime]'1970-01-01').TotalSeconds"') do set START=%%i

echo ===================================================
echo Activando entorno virtual...
call .\.venv\Scripts\activate

echo ---------------------------------------------------
echo Entorno virtual activado.
echo Ejecutando get_auto_actualizar_cv.py...

python get_auto_actualizar_cv.py
set "errorlevel_script=%ERRORLEVEL%"

echo ---------------------------------------------------
:: Verificar que se haya generado el CV
if exist .\data\CV_Matias_Perez_Nauto.pdf (
    echo CV generado correctamente.
    copy /Y ".\data\CV_Matias_Perez_Nauto.pdf" "D:\LLLIT\Code-W11\portafolio-minimalist\public\CV_Matias_Perez_Nauto.pdf"

) else (
    echo No se encontró el archivo de CV generado.
    goto end
)


echo ---------------------------------------------------
echo Copiando CV al portafolio público...



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


:: Calcular duración del proceso
for /f %%i in ('powershell -Command "[int]((Get-Date).ToUniversalTime() - [datetime]'1970-01-01').TotalSeconds"') do set END=%%i
set /a DURATION=!END! - !START!

echo ===================================================
echo Repositorio actualizado en GitHub.
echo Duración total del proceso: !DURATION! segundos
echo ===================================================




exit /b

