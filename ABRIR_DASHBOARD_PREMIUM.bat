@echo off
chcp 65001 > nul
color 0B
title Dashboard Premium - Parroquia Huancané

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║                                                                ║
echo ║        ⛪ DASHBOARD PREMIUM - PARROQUIA HUANCANÉ ⛪            ║
echo ║                                                                ║
echo ║              Enfoque en Sacramentos y Actividad Pastoral       ║
echo ║                                                                ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
echo 🚀 Iniciando Dashboard Premium...
echo.
echo 📊 Características:
echo    • Enfoque principal en SACRAMENTOS
echo    • Visualizaciones de clase mundial
echo    • Diseño responsive premium
echo    • Análisis automáticos
echo.
echo ⏳ Cargando aplicación...
echo.

cd /d "%~dp0"

streamlit run dashboard\app_premium.py --server.port=8501 --server.headless=true

if errorlevel 1 (
    echo.
    echo ❌ ERROR: No se pudo iniciar el dashboard
    echo.
    echo 💡 Soluciones:
    echo    1. Instala las dependencias: pip install -r requirements.txt
    echo    2. Verifica que Python y Streamlit estén instalados
    echo    3. Revisa que el archivo app_premium.py exista
    echo.
    pause
    exit /b 1
)

pause
