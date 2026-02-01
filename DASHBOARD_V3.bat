@echo off
chcp 65001 >nul
cls
color 0B

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║                                                            ║
echo ║        ⛪ DASHBOARD PROFESIONAL V3.0 ⛪                    ║
echo ║                                                            ║
echo ║         Parroquia Santiago Apóstol de Huancané            ║
echo ║                                                            ║
echo ╚════════════════════════════════════════════════════════════╝
echo.
echo 🚀 Iniciando Dashboard Profesional...
echo.
echo ════════════════════════════════════════════════════════════
echo.
echo 💻 ACCESO EN COMPUTADORA:
echo    🌐 http://localhost:8503
echo    ✅ Se abrirá automáticamente en tu navegador
echo.
echo ════════════════════════════════════════════════════════════
echo.
echo 📱 PARA ABRIR EN TU CELULAR:
echo.
color 0E
echo    ⭐⭐⭐ BUSCA LA "Network URL" ABAJO ⭐⭐⭐
echo.
color 0B
echo    1. Asegúrate que tu celular esté en la MISMA WiFi
echo    2. Busca abajo una línea que diga "Network URL:"
echo    3. Copia la dirección completa (ej: http://192.168.1.5:8503)
echo    4. Pégala en el navegador de tu celular
echo.
echo ════════════════════════════════════════════════════════════
echo.
echo 📄 PARA ABRIR EL INFORME WORD:
echo    ▶ Ejecuta: ABRIR_WORD.bat
echo.
echo ════════════════════════════════════════════════════════════
echo.
echo ⏳ Iniciando en 3 segundos...
echo.

cd /d "%~dp0dashboard"

REM Abrir el navegador automáticamente
timeout /t 3 /nobreak >nul
start http://localhost:8503

REM Ejecutar Streamlit con configuración de red
python -m streamlit run app.py --server.port=8503 --server.address=0.0.0.0 --server.headless=false

pause
