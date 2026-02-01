@echo off
chcp 65001 >nul
title Sistema Parroquial - Huancané
color 0A

:inicio
cls
echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║                                                            ║
echo ║     ⛪ SISTEMA DE GESTIÓN PARROQUIAL - HUANCANÉ ⛪         ║
echo ║                                                            ║
echo ║         Parroquia Santiago Apóstol de Huancané            ║
echo ║                                                            ║
echo ╚════════════════════════════════════════════════════════════╝
echo.
echo.
echo 📋 Seleccione una opción:
echo.
echo    [1] 📊 Abrir Dashboard Interactivo (Recomendado para móvil)
echo    [2] 📄 Generar Informe en Word
echo    [3] 🔄 Procesar Datos de Excel
echo    [4] ❌ Salir
echo.
echo ════════════════════════════════════════════════════════════
echo.

set /p opcion="👉 Ingrese el número de su opción: "

if "%opcion%"=="1" goto dashboard
if "%opcion%"=="2" goto informe
if "%opcion%"=="3" goto procesar
if "%opcion%"=="4" goto salir

echo.
echo ❌ Opción inválida. Intente nuevamente.
timeout /t 2 >nul
goto inicio

:dashboard
cls
echo.
echo ════════════════════════════════════════════════════════════
echo 🚀 Iniciando Dashboard Interactivo...
echo ════════════════════════════════════════════════════════════
echo.
echo 📱 OPTIMIZADO PARA MÓVILES
echo.
echo 💡 Instrucciones:
echo    - El dashboard se abrirá en tu navegador
echo    - Para ver en móvil: copia la URL "Network URL"
echo    - Usa CTRL+C para detener el servidor
echo.
echo ════════════════════════════════════════════════════════════
echo.
cd /d "%~dp0dashboard"
python -m streamlit run app.py --server.port=8502
goto fin

:informe
cls
echo.
echo ════════════════════════════════════════════════════════════
echo 📄 Generando Informe en Word...
echo ════════════════════════════════════════════════════════════
echo.
cd /d "%~dp0"
python generar_informe.py
if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✅ Proceso completado!
    echo 📁 El informe se guardó en: informes\Informe_Profesional_2025.docx
) else (
    echo.
    echo ❌ Hubo un error al generar el informe
    echo 💡 Verifica que tengas instaladas todas las librerías necesarias
)
echo.
pause
goto inicio

:procesar
cls
echo.
echo ════════════════════════════════════════════════════════════
echo 🔄 Procesando Datos de Excel...
echo ════════════════════════════════════════════════════════════
echo.
echo ⚠️  IMPORTANTE: Asegúrate de que los archivos Excel estén en la carpeta 'datos'
echo.
pause
cd /d "%~dp0"
python procesador_datos.py
if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✅ Proceso completado!
    echo 📊 Los datos consolidados se guardaron en: datos_consolidados.csv
) else (
    echo.
    echo ❌ Hubo un error al procesar los datos
    echo 💡 Verifica que haya archivos Excel en la carpeta 'datos'
)
echo.
pause
goto inicio

:salir
cls
echo.
echo ════════════════════════════════════════════════════════════
echo 👋 Gracias por usar el Sistema de Gestión Parroquial
echo ════════════════════════════════════════════════════════════
echo.
timeout /t 2 >nul
exit

:fin
echo.
pause
goto inicio
