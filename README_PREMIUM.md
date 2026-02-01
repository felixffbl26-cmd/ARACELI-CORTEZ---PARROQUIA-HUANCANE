# ⛪ Dashboard Premium - Parroquia Santiago Apóstol de Huancané

## 🎯 Descripción

Dashboard profesional con **enfoque principal en SACRAMENTOS** y actividad pastoral, diseñado específicamente para la Parroquia Santiago Apóstol de Huancané.

**Desarrollado por:** Araceli Victoria Cortez

---

## ✨ Características Principales

### 🏆 Enfoque en Sacramentos (Página Principal)
- **Métricas destacadas**: Bautismos, Matrimonios, Confirmaciones
- **Evolución mensual** de cada sacramento
- **Comparativa año actual vs anterior**
- **Distribución de tipos de misas** (alma, salud, exequias, chacra, etc.)
- **Heatmap de actividad sacramental**
- **Análisis automáticos** con insights inteligentes

### 💰 Dashboard Financiero
- Ingresos y egresos mensuales
- Balance neto con alertas
- Distribución por categorías
- Gráficos interactivos

### 📋 Gestión de Documentos
- Partidas, constancias y certificados
- Estadísticas de emisión
- Tendencias mensuales

### 📊 Reportes Completos
- Resumen general del año
- Tablas de datos detallados
- Exportación a CSV

### 🎨 Diseño Premium
- **Gradientes modernos** y colores vibrantes
- **Animaciones sutiles** para mejor UX
- **Responsive design** (móvil y desktop)
- **Visualizaciones de clase mundial** con Plotly
- **Firma sutil** de la desarrolladora

---

## 🚀 Inicio Rápido

### Opción 1: Usar el Script Automático (Recomendado)

1. **Doble click** en `ABRIR_DASHBOARD_PREMIUM.bat`
2. El dashboard se abrirá automáticamente en tu navegador

### Opción 2: Línea de Comandos

```bash
# 1. Instalar dependencias (solo la primera vez)
pip install -r requirements.txt

# 2. Ejecutar dashboard
streamlit run dashboard/app_premium.py
```

El dashboard estará disponible en: **http://localhost:8501**

---

## 📦 Requisitos

- Python 3.8 o superior
- Dependencias (se instalan automáticamente):
  - streamlit >= 1.28.0
  - pandas >= 2.0.0
  - numpy >= 1.24.0
  - plotly >= 5.17.0
  - openpyxl >= 3.1.0
  - xlrd >= 2.0.1

---

## 📁 Estructura del Proyecto

```
parroquia_huancane/
├── dashboard/
│   ├── app_premium.py          ← ⭐ DASHBOARD PRINCIPAL (NUEVO)
│   ├── app.py                  ← Dashboard anterior (backup)
│   └── app_v3.py               ← Versión 3 (backup)
├── datos/                      ← Archivos Excel originales
├── datos_consolidados.csv      ← Datos procesados
├── procesador_datos.py         ← Procesador de datos
├── requirements.txt            ← Dependencias
├── .streamlit/
│   └── config.toml            ← Configuración de tema
├── ABRIR_DASHBOARD_PREMIUM.bat ← Script de inicio
└── GUIA_DEPLOY.md             ← Guía para Streamlit Cloud
```

---

## 🌐 Deploy en Streamlit Cloud (GitHub)

Para subir el dashboard a internet y accederlo desde cualquier lugar:

1. **Lee la guía completa**: `GUIA_DEPLOY.md`
2. **Sube a GitHub** los archivos necesarios
3. **Conecta con Streamlit Cloud**
4. **¡Listo!** Tu dashboard estará en línea 24/7

**URL ejemplo:** `https://parroquia-huancane.streamlit.app`

---

## 🎯 Diferencias con la Versión Anterior

### ✅ NUEVO Dashboard Premium (`app_premium.py`)

| Característica | Anterior | Premium |
|---------------|----------|---------|
| **Enfoque principal** | Finanzas | ⛪ **SACRAMENTOS** |
| **Diseño** | Básico | 🎨 **Premium con gradientes** |
| **Visualizaciones** | Estándar | 📊 **Clase mundial (heatmaps, sunburst)** |
| **Análisis** | Manual | 💡 **Automático con insights** |
| **Comparativas** | Limitadas | 📈 **Año vs año completo** |
| **Firma** | No | ✍️ **Araceli Victoria Cortez** |
| **Responsive** | Básico | 📱 **Optimizado móvil/desktop** |

---

## 📊 Capturas de Pantalla

### Página Principal - Sacramentos
- Métricas destacadas de bautismos, matrimonios y confirmaciones
- Gráfico de evolución mensual
- Distribución por tipo (donut chart)
- Heatmap de actividad
- Comparativa con año anterior

### Dashboard Financiero
- Flujo de caja mensual
- Balance neto
- Distribución de ingresos

### Documentos y Reportes
- Estadísticas de documentos emitidos
- Tablas detalladas con exportación

---

## 🔧 Solución de Problemas

### Error: "streamlit no reconocido"
```bash
pip install streamlit
```

### Error: "No se encuentra datos_consolidados.csv"
```bash
# Procesar datos primero
python procesador_datos.py
```

### El dashboard no carga
1. Verifica que Python esté instalado: `python --version`
2. Instala dependencias: `pip install -r requirements.txt`
3. Verifica que el archivo CSV exista

---

## 📝 Actualizar Datos

Para actualizar con nuevos datos:

```bash
# 1. Agregar archivos Excel nuevos a la carpeta 'datos/'

# 2. Procesar datos
python procesador_datos.py

# 3. El dashboard se actualizará automáticamente
```

---

## 🎨 Personalización

### Cambiar Colores
Edita `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#3b82f6"      # Color principal
backgroundColor = "#f8fafc"    # Fondo
secondaryBackgroundColor = "#e0e7ff"  # Fondo secundario
```

### Modificar Visualizaciones
Edita `dashboard/app_premium.py` - Todas las visualizaciones usan Plotly

---

## 📞 Soporte

Para preguntas o problemas:
- Revisa `GUIA_DEPLOY.md` para deploy
- Revisa `SOLUCION_PROBLEMAS.md` para errores comunes

---

## 📜 Licencia

Dashboard desarrollado para uso exclusivo de la Parroquia Santiago Apóstol de Huancané.

**Desarrollado con dedicación por:** Araceli Victoria Cortez  
**Fecha:** Febrero 2026  
**Versión:** Premium 1.0

---

## 🌟 Características Técnicas

- **Framework**: Streamlit
- **Visualizaciones**: Plotly
- **Procesamiento**: Pandas + NumPy
- **Precisión financiera**: Decimal
- **Caché inteligente**: @st.cache_data
- **Responsive**: CSS Grid + Flexbox
- **Animaciones**: CSS Animations
- **Deploy**: Streamlit Cloud compatible

---

## 🎉 ¡Disfruta tu Dashboard Premium!

El dashboard está listo para usar. Simplemente ejecuta `ABRIR_DASHBOARD_PREMIUM.bat` y explora todas las funcionalidades.

**¡Que Dios bendiga a la Parroquia Santiago Apóstol de Huancané!** ⛪
