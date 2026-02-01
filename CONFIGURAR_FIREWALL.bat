@echo off
chcp 65001 >nul

echo.
echo ════════════════════════════════════════════════════════════
echo  🔥 CONFIGURAR FIREWALL PARA ACCESO MÓVIL 🔥
echo ════════════════════════════════════════════════════════════
echo.
echo Este script creará una regla en el firewall de Windows
echo para permitir el acceso al dashboard desde tu celular.
echo.
echo ⚠️  IMPORTANTE: Necesitas ejecutar como ADMINISTRADOR
echo.
pause

echo.
echo 🔧 Creando regla en el firewall...
echo.

netsh advfirewall firewall add rule name="Dashboard Parroquia - Puerto 8503" dir=in action=allow protocol=TCP localport=8503

if %errorlevel% == 0 (
    color 0A
    echo.
    echo ════════════════════════════════════════════════════════════
    echo  ✅ ¡REGLA CREADA EXITOSAMENTE!
    echo ════════════════════════════════════════════════════════════
    echo.
    echo Ahora intenta acceder desde tu celular:
    echo.
    echo    http://192.168.1.71:8503
    echo.
    echo ════════════════════════════════════════════════════════════
) else (
    color 0C
    echo.
    echo ════════════════════════════════════════════════════════════
    echo  ❌ ERROR: No se pudo crear la regla
    echo ════════════════════════════════════════════════════════════
    echo.
    echo SOLUCIÓN:
    echo.
    echo 1. Cierra esta ventana
    echo 2. Haz clic DERECHO en CONFIGURAR_FIREWALL.bat
    echo 3. Selecciona "Ejecutar como administrador"
    echo 4. Haz clic en "Sí" cuando Windows pregunte
    echo.
    echo ════════════════════════════════════════════════════════════
)

echo.
pause
