@echo off
chcp 65001 >nul
cls
color 0E

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║                                                            ║
echo ║           📄 ABRIR INFORME WORD 📄                        ║
echo ║                                                            ║
echo ║         Parroquia Santiago Apóstol de Huancané            ║
echo ║                                                            ║
echo ╚════════════════════════════════════════════════════════════╝
echo.
echo 🔍 Buscando informe más reciente...
echo.

cd /d "%~dp0"

REM Buscar el archivo Word más reciente
for /f "delims=" %%i in ('dir /b /od informes\*.docx 2^>nul') do set "ultimo=%%i"

if defined ultimo (
    echo ✅ Informe encontrado: %ultimo%
    echo.
    echo 📂 Ubicación: %~dp0informes\%ultimo%
    echo.
    echo 🚀 Abriendo en Microsoft Word...
    echo.
    start "" "informes\%ultimo%"
    timeout /t 2 /nobreak >nul
    echo.
    echo ✅ ¡Informe abierto exitosamente!
) else (
    echo ❌ No se encontró ningún informe Word.
    echo.
    echo 💡 Genera uno primero usando INICIAR.bat ^> Opción 2
)

echo.
pause
