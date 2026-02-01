@echo off
chcp 65001 >nul
title Dashboard Parroquial
color 0B

echo.
echo ════════════════════════════════════════════════════════════
echo   ⛪ Iniciando Dashboard de la Parroquia de Huancané ⛪
echo ════════════════════════════════════════════════════════════
echo.
echo 📱 El dashboard se abrirá en tu navegador...
echo.
echo 💡 Para ver en tu celular:
echo    1. Copia la URL que dice "Network URL: http://..."
echo    2. Ábrela en el navegador de tu celular (misma WiFi)
echo.
echo ⚠️  Para detener: Presiona CTRL+C
echo.
echo ════════════════════════════════════════════════════════════
echo.

cd /d "%~dp0dashboard"
python -m streamlit run app.py --server.port=8502

pause
