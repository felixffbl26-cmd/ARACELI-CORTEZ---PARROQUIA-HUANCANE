@echo off
chcp 65001 > nul
color 0A
title Instalación Dashboard Premium - Parroquia Huancané

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║                                                                ║
echo ║     🚀 INSTALACIÓN DASHBOARD PREMIUM - PARROQUIA HUANCANÉ     ║
echo ║                                                                ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
echo Este script instalará todas las dependencias necesarias.
echo.
echo ⏳ Verificando Python...
echo.

python --version > nul 2>&1
if errorlevel 1 (
    echo ❌ ERROR: Python no está instalado
    echo.
    echo 💡 Por favor instala Python desde: https://www.python.org/downloads/
    echo    Asegúrate de marcar "Add Python to PATH" durante la instalación
    echo.
    pause
    exit /b 1
)

echo ✅ Python encontrado
echo.
echo ⏳ Instalando dependencias...
echo.

pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ❌ ERROR: No se pudieron instalar las dependencias
    echo.
    echo 💡 Intenta ejecutar manualmente:
    echo    pip install streamlit pandas numpy plotly openpyxl xlrd
    echo.
    pause
    exit /b 1
)

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║                                                                ║
echo ║                  ✅ INSTALACIÓN COMPLETADA                     ║
echo ║                                                                ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
echo 🎉 ¡Todo listo! Ahora puedes ejecutar el dashboard.
echo.
echo 📝 Próximos pasos:
echo    1. Doble click en: ABRIR_DASHBOARD_PREMIUM.bat
echo    2. El dashboard se abrirá en tu navegador
echo    3. ¡Disfruta!
echo.
echo 📚 Documentación:
echo    • README_PREMIUM.md - Guía completa
echo    • GUIA_DEPLOY.md - Para subir a internet
echo.
pause
