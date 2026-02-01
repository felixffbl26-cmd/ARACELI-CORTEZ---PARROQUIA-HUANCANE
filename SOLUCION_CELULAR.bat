@echo off
chcp 65001 >nul
cls
color 0E

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║                                                            ║
echo ║        🔧 SOLUCIÓN: NO PUEDO ACCEDER DESDE CELULAR 🔧     ║
echo ║                                                            ║
echo ╚════════════════════════════════════════════════════════════╝
echo.
echo.
color 0C
echo ⚠️  PROBLEMA: El firewall está bloqueando la conexión
echo.
color 0F
echo ════════════════════════════════════════════════════════════
echo.
echo 🎯 SOLUCIÓN RÁPIDA (Recomendada):
echo.
echo    1️⃣  Haz clic DERECHO en: CONFIGURAR_FIREWALL.bat
echo.
echo    2️⃣  Selecciona: "Ejecutar como administrador"
echo.
echo    3️⃣  Haz clic en "Sí" cuando Windows pregunte
echo.
echo    4️⃣  Espera a que diga "REGLA CREADA EXITOSAMENTE"
echo.
echo    5️⃣  Intenta de nuevo desde tu celular:
echo        http://192.168.1.71:8503
echo.
echo ════════════════════════════════════════════════════════════
echo.
echo 🔧 SOLUCIÓN ALTERNATIVA (Manual):
echo.
echo    Si la solución rápida no funciona:
echo.
echo    1. Presiona la tecla Windows
echo    2. Escribe: "Firewall"
echo    3. Abre: "Firewall de Windows Defender"
echo    4. Clic en: "Configuración avanzada"
echo    5. Clic en: "Reglas de entrada" (lado izquierdo)
echo    6. Clic en: "Nueva regla..." (lado derecho)
echo    7. Selecciona: "Puerto" → Siguiente
echo    8. Selecciona: "TCP"
echo    9. Escribe en "Puertos locales específicos": 8503
echo    10. Siguiente → Siguiente → Siguiente
echo    11. Nombre: "Dashboard Parroquia"
echo    12. Finalizar
echo.
echo ════════════════════════════════════════════════════════════
echo.
echo 💡 VERIFICACIÓN:
echo.
echo    Después de configurar el firewall:
echo.
echo    ✅ Verifica que el dashboard esté corriendo
echo       (DASHBOARD_V3.bat debe estar abierto)
echo.
echo    ✅ Verifica que ambos estén en la misma WiFi
echo.
echo    ✅ En tu celular, abre el navegador y escribe:
echo       http://192.168.1.71:8503
echo.
echo ════════════════════════════════════════════════════════════
echo.
echo 📞 ¿SIGUE SIN FUNCIONAR?
echo.
echo    Otras posibles causas:
echo.
echo    🔸 Antivirus bloqueando (desactiva temporalmente)
echo    🔸 VPN activa (desactiva en celular y computadora)
echo    🔸 IP cambió (ejecuta OBTENER_IP.bat)
echo    🔸 Router con aislamiento AP (consulta a tu proveedor)
echo.
echo ════════════════════════════════════════════════════════════
echo.
pause
