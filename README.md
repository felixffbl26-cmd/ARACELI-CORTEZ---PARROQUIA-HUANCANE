# ⛪ Sistema de Gestión Parroquial - Huancané

**Parroquia Santiago Apóstol de Huancané**  
*Sistema de análisis y visualización de datos parroquiales*

## 🆕 Novedades Versión 2.0

### ✨ Optimización para Dispositivos Móviles
- 📱 **Diseño Responsivo:** Interfaz completamente adaptada para celulares y tablets
- 👆 **Botones Táctiles:** Elementos más grandes y fáciles de tocar
- 📊 **Gráficos Adaptables:** Visualizaciones que se ajustan automáticamente al tamaño de pantalla
- 🎨 **Mejor Contraste:** Colores optimizados para lectura en pantallas pequeñas

### 📊 Comparativas Mejoradas
- 📈 **Vista Comparativa 2024-2025:** Nueva pestaña dedicada a comparar años
- 📉 **Gráficos de Tendencia:** Visualización de patrones mensuales entre años
- 💰 **Análisis Automático:** Interpretaciones inteligentes de las variaciones

### 🚀 Mejoras de Usabilidad
- 🎯 **Navegación Simplificada:** Menú lateral colapsable para móviles
- 🔍 **Filtros en Acordeón:** Opciones de filtrado que no ocupan espacio innecesario
- 📋 **Métricas Destacadas:** KPIs más visibles y fáciles de entender
- 🎨 **Diseño Moderno:** Interfaz actualizada con mejor estética

---

## 📋 Características Principales

### 1. Dashboard Interactivo
- Visualización en tiempo real de datos parroquiales
- 4 pestañas especializadas:
  - **📊 Comparativa:** Análisis entre años
  - **📅 Detalle:** Información mensual detallada
  - **🙏 Pastoral:** Actividad sacramental y litúrgica
  - **💰 Finanzas:** Salud financiera de la parroquia

### 2. Generador de Informes
- Informes profesionales en formato Word
- Gráficos de alta calidad (300 DPI)
- Análisis automático de tendencias
- Listo para imprimir o compartir

### 3. Procesador de Datos
- Importación automática desde Excel
- Detección inteligente de fechas y categorías
- Consolidación de múltiples archivos
- Validación y limpieza de datos

---

## 🚀 Inicio Rápido

### Método 1: Menú Interactivo (Recomendado)

1. Doble clic en `INICIAR.bat`
2. Seleccione la opción deseada:
   ```
   [1] Dashboard Interactivo
   [2] Generar Informe Word
   [3] Procesar Datos Excel
   ```

### Método 2: Línea de Comandos

```bash
# Dashboard
cd dashboard
streamlit run app.py

# Informe
python generar_informe.py

# Procesar datos
python procesador_datos.py
```

---

## 📱 Uso en Dispositivos Móviles

### Configuración Inicial:

1. **En la computadora:**
   - Ejecute `INICIAR.bat` → Opción [1]
   - Busque la línea: `Network URL: http://192.168.X.X:8501`
   - Copie esa dirección completa

2. **En el móvil:**
   - Conéctese a la **misma red WiFi**
   - Abra el navegador
   - Pegue la dirección copiada
   - ¡Listo!

### Consejos para Móvil:

- 📱 Use orientación **horizontal** para gráficos
- 👆 Toque con dos dedos para hacer zoom
- 🔍 Use el botón de filtros para opciones avanzadas
- 📊 Deslice las tablas horizontalmente

---

## 📂 Estructura del Proyecto

```
parroquia_huancane/
│
├── 📁 datos/                    # Archivos Excel originales
│   └── *.xlsx                   # (Coloque aquí sus archivos)
│
├── 📁 dashboard/                # Dashboard interactivo
│   └── app.py                   # Aplicación Streamlit
│
├── 📁 informes/                 # Informes generados
│   ├── 📁 graficos/            # Gráficos PNG
│   └── Informe_Profesional_2025.docx
│
├── 📄 procesador_datos.py       # Procesador de Excel
├── 📄 generar_informe.py        # Generador de informes
├── 📄 datos_consolidados.csv    # Datos procesados
│
├── 🚀 INICIAR.bat              # Menú de inicio
├── 📖 GUIA_PARA_EL_PADRE.md    # Guía de usuario
└── 📖 README.md                # Este archivo
```

---

## 🔧 Requisitos del Sistema

### Software Necesario:
- Python 3.8 o superior
- Navegador web moderno (Chrome, Firefox, Edge, Safari)

### Librerías Python:
```bash
pip install streamlit pandas plotly python-docx matplotlib seaborn openpyxl xlrd
```

---

## 📊 Datos Soportados

### Formato de Archivos Excel:

El sistema detecta automáticamente las siguientes columnas:
- **Fecha:** Fecha de la transacción
- **Detalle:** Descripción del movimiento
- **Ingreso:** Monto de entrada
- **Egreso:** Monto de salida

### Categorización Automática:

El sistema clasifica automáticamente:
- 🙏 **MISA:** Misas de alma, salud, chacra, exequias, etc.
- ✝️ **SACRAMENTO:** Bautismos, matrimonios, confirmaciones
- 📄 **DOCUMENTO:** Partidas, constancias, certificados
- 💼 **OTROS:** Donaciones, gastos administrativos, etc.

---

## 📈 Métricas Disponibles

### Dashboard:
- 💰 Ingresos totales por periodo
- 💸 Egresos totales por periodo
- 📊 Balance neto (superávit/déficit)
- 📋 Número de transacciones
- 🏷️ Distribución por categoría
- 📅 Tendencias mensuales
- 🆚 Comparativas anuales

### Informes:
- Gráficos de barras comparativas
- Gráficos de líneas de tendencia
- Gráficos circulares de distribución
- Análisis de sacramentos
- Diagnóstico financiero

---

## 🎨 Personalización

### Colores del Dashboard:
Los colores están definidos en `dashboard/app.py`:
```python
# Edite estos valores para cambiar la paleta
color_primary = '#3498db'    # Azul principal
color_success = '#2ecc71'    # Verde (positivo)
color_danger = '#e74c3c'     # Rojo (negativo)
```

### Categorías:
Las categorías se definen en `procesador_datos.py`:
```python
self.categorias = {
    'MISA': ['MISA', 'EXEQUIA'],
    'SACRAMENTO': ['BAUTISMO', 'MATRIMONIO', 'CONFIRMACION'],
    # Agregue más según necesite
}
```

---

## ❓ Solución de Problemas

### El dashboard no muestra datos de 2024

**Solución:**
1. Verifique que los archivos Excel tengan el año en el nombre
2. Ejecute el procesador de datos (Opción [3])
3. En el dashboard, cambie el filtro de año

### Error al procesar archivos Excel

**Solución:**
1. Verifique que los archivos estén en la carpeta `datos/`
2. Asegúrese de que tengan las columnas correctas
3. Revise que las fechas estén en formato válido

### El dashboard no se abre en el móvil

**Solución:**
1. Verifique que ambos dispositivos estén en la misma red WiFi
2. Copie la dirección completa incluyendo el puerto `:8501`
3. Desactive temporalmente el firewall si es necesario

### Los gráficos se ven cortados

**Solución:**
1. En móvil: Rote el dispositivo a horizontal
2. Haga zoom con dos dedos
3. Ajuste el tamaño de la ventana del navegador

---

## 🔐 Seguridad y Privacidad

- ✅ **100% Local:** Todos los datos permanecen en su computadora
- ✅ **Sin Internet:** No requiere conexión a internet para funcionar
- ✅ **Sin Nube:** No se envía información a servidores externos
- ✅ **Privado:** Solo accesible en su red local

### Recomendaciones:
- 🔒 Haga copias de seguridad periódicas
- 🔒 Proteja el acceso a la computadora
- 🔒 No comparta la dirección de red fuera de su WiFi

---

## 📝 Notas de Versión

### v2.0 (Enero 2026)
- ✨ Optimización completa para móviles
- 📊 Nueva pestaña de comparativas anuales
- 🎨 Rediseño de interfaz con mejor UX
- 📱 Diseño responsivo adaptable
- 🔍 Filtros mejorados en acordeón
- 📈 Gráficos comparativos entre años
- 📖 Guía actualizada para usuarios

### v1.0 (Diciembre 2025)
- 🎉 Lanzamiento inicial
- 📊 Dashboard básico
- 📄 Generador de informes
- 🔄 Procesador de datos

---

## 🤝 Soporte

Para ayuda adicional:
1. Consulte `GUIA_PARA_EL_PADRE.md`
2. Revise la sección de solución de problemas
3. Verifique que todos los requisitos estén instalados

---

## 📜 Licencia

Este sistema fue desarrollado específicamente para la **Parroquia Santiago Apóstol de Huancané**.

---

## 🙏 Agradecimientos

*Que Dios bendiga el trabajo pastoral y administrativo de la Parroquia Santiago Apóstol de Huancané.*

---

**Desarrollado con ❤️ para la gestión eficiente de la obra parroquial**

*Última actualización: Enero 2026*
