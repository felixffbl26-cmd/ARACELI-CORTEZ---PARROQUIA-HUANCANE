@echo off
chcp 65001 >nul
cls
color 0B

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║                                                            ║
echo ║              🌐 OBTENER IP DE LA COMPUTADORA 🌐           ║
echo ║                                                            ║
echo ╚════════════════════════════════════════════════════════════╝
echo.
echo 🔍 Buscando dirección IP...
echo.
echo ════════════════════════════════════════════════════════════

ipconfig | findstr /i "IPv4"

echo ════════════════════════════════════════════════════════════
echo.
echo 💡 INSTRUCCIONES:
echo.
echo    1. Busca la línea que dice "Dirección IPv4"
echo    2. Anota el número (ejemplo: 192.168.1.71)
echo    3. En tu celular, abre el navegador
echo    4. Escribe: http://[TU-IP]:8503
echo.
echo    Ejemplo: http://192.168.1.71:8503
echo.
echo ════════════════════════════════════════════════════════════
echo.
pause
