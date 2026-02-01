# 📱 Guía de Uso - Sistema de Gestión Parroquial

**Parroquia Santiago Apóstol de Huancané**  
*Versión 2.0 - Optimizada para Dispositivos Móviles*

---

## 🚀 Inicio Rápido

### Opción 1: Usar el Menú de Inicio (Recomendado)

1. **Doble clic** en el archivo `INICIAR.bat`
2. Seleccione la opción que necesite:
   - **[1]** Dashboard Interactivo (para ver datos en tiempo real)
   - **[2]** Generar Informe en Word (para imprimir o compartir)
   - **[3]** Procesar Datos de Excel (cuando agregue nuevos registros)

---

## 📊 Dashboard Interactivo

### ¿Qué es?
Es una página web interactiva que muestra todos los datos de la parroquia con gráficos y estadísticas en tiempo real.

### ¿Cómo usarlo?

#### En Computadora:
1. Ejecute `INICIAR.bat` y seleccione opción **[1]**
2. Se abrirá automáticamente en su navegador
3. Explore las diferentes pestañas

#### En Celular o Tablet:
1. Ejecute el dashboard en su computadora (paso 1 arriba)
2. En la ventana negra que aparece, busque una línea que dice:
   ```
   Network URL: http://192.168.X.X:8501
   ```
3. **Copie esa dirección completa**
4. En su celular/tablet:
   - Asegúrese de estar conectado a la **misma red WiFi** que la computadora
   - Abra el navegador (Chrome, Safari, etc.)
   - Pegue la dirección copiada
   - ¡Listo! Ya puede ver el dashboard en su dispositivo móvil

### Pestañas del Dashboard

#### 📊 COMPARATIVA
- **Qué muestra:** Comparación entre años (2024 vs 2025)
- **Útil para:** Ver si los ingresos están creciendo o disminuyendo
- **Gráficos:**
  - Barras comparativas por año
  - Líneas de tendencia mensual

#### 📅 DETALLE
- **Qué muestra:** Información específica del año seleccionado
- **Filtros disponibles:**
  - 📅 Año (2024 o 2025)
  - 📆 Mes (Todos o uno específico)
  - 🏷️ Categoría (Misas, Sacramentos, etc.)
- **Incluye:** Tabla con todos los movimientos

#### 🙏 PASTORAL
- **Qué muestra:** Actividad sacramental y litúrgica
- **Gráficos:**
  - Distribución de sacramentos (Bautismos, Matrimonios, etc.)
  - Tipos de misas más frecuentes

#### 💰 FINANZAS
- **Qué muestra:** Salud financiera de la parroquia
- **Gráficos:**
  - Ingresos vs Egresos por mes
  - Balance neto (superávit o déficit)
- **Incluye:** Diagnóstico financiero automático

---

## 📄 Generar Informe en Word

### ¿Cuándo usarlo?
- Para presentaciones formales
- Para imprimir y archivar
- Para compartir con el consejo parroquial

### Pasos:
1. Ejecute `INICIAR.bat`
2. Seleccione opción **[2]**
3. Espere a que termine el proceso
4. El archivo se guardará en: `informes\Informe_Profesional_2025.docx`

### Contenido del Informe:
- Portada con resumen ejecutivo
- Gráficos de alta calidad
- Análisis automático de cada gráfico
- Conclusiones generales

---

## 🔄 Procesar Nuevos Datos

### ¿Cuándo hacerlo?
Cuando tenga nuevos archivos Excel con registros de caja.

### Pasos:

1. **Preparar los archivos Excel:**
   - Coloque los archivos `.xls` o `.xlsx` en la carpeta `datos`
   - **Importante:** El nombre del archivo debe incluir el año (ej: "ABRIL 2024.xlsx")

2. **Ejecutar el procesador:**
   - Abra `INICIAR.bat`
   - Seleccione opción **[3]**
   - Espere a que termine

3. **Verificar:**
   - Se creará/actualizará el archivo `datos_consolidados.csv`
   - Verá un resumen en pantalla con:
     - Total de registros procesados
     - Años detectados
     - Balance general

---

## 📱 Optimización para Móviles

### Características Especiales:

✅ **Texto más grande** - Fácil de leer en pantallas pequeñas  
✅ **Botones táctiles** - Diseñados para tocar con el dedo  
✅ **Gráficos responsivos** - Se adaptan al tamaño de la pantalla  
✅ **Navegación simplificada** - Menú lateral colapsable  
✅ **Filtros en acordeón** - No ocupan espacio innecesario  

### Consejos para Móvil:

1. **Orientación:** Use el celular en **horizontal** para ver mejor los gráficos
2. **Zoom:** Puede hacer zoom en los gráficos tocando con dos dedos
3. **Filtros:** Toque el botón "🔍 Filtros de Búsqueda" para mostrar/ocultar opciones
4. **Tablas:** Deslice hacia los lados para ver todas las columnas

---

## ❓ Preguntas Frecuentes

### ¿Por qué solo veo datos de un año?

**R:** Verifique que:
1. Los archivos Excel tengan el año en el nombre (ej: "ENERO 2024.xlsx")
2. Haya ejecutado el procesador de datos (opción [3])
3. En el dashboard, cambie el año en los filtros

### ¿Cómo ver datos de 2024 Y 2025 juntos?

**R:** Vaya a la pestaña **"📊 COMPARATIVA"** - ahí verá ambos años lado a lado.

### El dashboard no se abre en mi celular

**R:** Verifique que:
1. El celular esté en la **misma red WiFi** que la computadora
2. Haya copiado la dirección **completa** (incluyendo el puerto :8501)
3. El dashboard siga corriendo en la computadora (ventana negra abierta)

### ¿Cómo detengo el dashboard?

**R:** En la ventana negra que se abrió, presione **CTRL + C**

### Los gráficos se ven muy pequeños

**R:** 
- En móvil: Toque el gráfico con dos dedos y sepárelos para hacer zoom
- En computadora: Los gráficos se ajustan automáticamente al ancho de la ventana

---

## 🆘 Soporte

Si tiene problemas o preguntas:

1. **Revise esta guía** - La mayoría de dudas están respondidas aquí
2. **Verifique los datos** - Asegúrese de que los archivos Excel estén correctos
3. **Reinicie el sistema** - Cierre todo y vuelva a ejecutar `INICIAR.bat`

---

## 📊 Interpretación de Datos

### Colores en los Gráficos:

- 🟢 **Verde:** Ingresos, valores positivos
- 🔴 **Rojo:** Egresos, valores negativos
- 🔵 **Azul:** Datos generales, comparativas

### Símbolos:

- ✅ **Positivo:** Balance favorable
- ⚠️ **Advertencia:** Requiere atención
- ❌ **Negativo:** Situación desfavorable
- 💡 **Interpretación:** Análisis automático

---

## 🔐 Seguridad de Datos

- Los datos **nunca salen de su computadora**
- No se requiere conexión a internet
- Los archivos están en su disco local
- Haga copias de seguridad periódicas de la carpeta completa

---

**Última actualización:** Enero 2026  
**Versión del sistema:** 2.0 - Mobile Optimized

---

*Que Dios bendiga el trabajo pastoral de la Parroquia Santiago Apóstol* 🙏
