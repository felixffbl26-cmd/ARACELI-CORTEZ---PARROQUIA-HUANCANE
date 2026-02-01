# 🆘 Guía Rápida de Solución de Problemas

## ❌ "No puedo abrir el dashboard en mi laptop"

### Solución 1: Usar el script de inicio
1. Haz **doble clic** en `ABRIR_DASHBOARD.bat` (archivo nuevo)
2. Espera a que se abra el navegador automáticamente
3. Si no se abre, copia la URL que aparece y pégala en tu navegador

### Solución 2: Desde el menú principal
1. Haz doble clic en `INICIAR.bat`
2. Selecciona opción **[1]**
3. El dashboard se abrirá automáticamente

### Solución 3: Comando manual
Abre PowerShell o CMD en la carpeta del proyecto y ejecuta:
```bash
cd dashboard
python -m streamlit run app.py --server.port=8502
```

---

## ❌ "Error: streamlit no se reconoce"

**Causa:** Streamlit no está instalado o no está en el PATH

**Solución:**
```bash
pip install streamlit
```

O usa el comando completo:
```bash
python -m streamlit run app.py
```

---

## ❌ "Error al cargar datos"

**Causa:** No existe el archivo `datos_consolidados.csv`

**Solución:**
1. Coloca tus archivos Excel en la carpeta `datos/`
2. Ejecuta `INICIAR.bat` → Opción [3] (Procesar Datos)
3. Espera a que termine
4. Vuelve a abrir el dashboard

---

## ❌ "El puerto 8501 está en uso"

**Causa:** Ya hay otro proceso usando ese puerto

**Solución 1:** Usa el nuevo script que usa puerto 8502
```bash
ABRIR_DASHBOARD.bat
```

**Solución 2:** Cierra otros procesos de Streamlit
- Presiona `CTRL+C` en cualquier ventana negra abierta
- O reinicia tu computadora

---

## ❌ "No veo datos de 2024"

**Verificación:**
1. Abre el dashboard
2. Ve a la pestaña **"📊 COMPARATIVA"**
3. Deberías ver ambos años

**Si no aparecen:**
1. Verifica que los archivos Excel tengan el año en el nombre (ej: "ENERO 2024.xlsx")
2. Vuelve a procesar los datos (Opción [3] del menú)

---

## ❌ "No se abre en mi celular"

**Checklist:**
- [ ] ¿El dashboard está corriendo en la PC? (ventana negra abierta)
- [ ] ¿El celular está en la **misma WiFi** que la PC?
- [ ] ¿Copiaste la URL **completa** incluyendo `:8502`?
- [ ] ¿Probaste desactivar el firewall temporalmente?

**URL correcta:**
```
http://192.168.X.X:8502
```
(Copia exactamente lo que dice "Network URL" en la ventana negra)

---

## ❌ "Librerías faltantes"

**Error típico:**
```
ModuleNotFoundError: No module named 'streamlit'
```

**Solución - Instalar todo:**
```bash
pip install streamlit pandas plotly python-docx matplotlib seaborn openpyxl xlrd
```

---

## ❌ "El informe no se genera"

**Verificación:**
1. ¿Existe `datos_consolidados.csv`?
2. ¿Tienes instalado `python-docx`?

**Solución:**
```bash
pip install python-docx matplotlib seaborn
python generar_informe.py
```

---

## 🔧 Comandos Útiles

### Ver si los datos están cargados:
```bash
python -c "import pandas as pd; df = pd.read_csv('datos_consolidados.csv'); print(f'Registros: {len(df)}'); print(f'Años: {sorted(df[\"año\"].unique())}')"
```

### Verificar librerías instaladas:
```bash
python -c "import streamlit; import pandas; import plotly; print('✅ Todo OK')"
```

### Matar procesos de Streamlit:
```bash
taskkill /F /IM streamlit.exe
```

---

## 📞 Pasos de Diagnóstico

Si nada funciona, sigue estos pasos en orden:

1. **Verifica Python:**
   ```bash
   python --version
   ```
   Debe ser 3.8 o superior

2. **Verifica las librerías:**
   ```bash
   pip list | findstr streamlit
   ```

3. **Verifica los datos:**
   ```bash
   dir datos_consolidados.csv
   ```

4. **Intenta el comando más simple:**
   ```bash
   cd dashboard
   python -m streamlit run app.py --server.port=8503
   ```

5. **Si todo falla, reinstala:**
   ```bash
   pip uninstall streamlit
   pip install streamlit
   ```

---

## 💡 Consejos

- **Siempre usa `python -m streamlit`** en lugar de solo `streamlit`
- **Cambia el puerto** si hay conflictos (8502, 8503, 8504...)
- **Reinicia la PC** si los problemas persisten
- **Verifica el firewall** si no funciona en móvil

---

## ✅ Verificación Rápida

Ejecuta esto para verificar que todo esté bien:

```bash
cd c:\Users\FELIX\.gemini\antigravity\scratch\parroquia_huancane
python -c "import streamlit, pandas, plotly; df = pandas.read_csv('datos_consolidados.csv'); print(f'✅ Todo OK! {len(df)} registros cargados')"
```

Si ves "✅ Todo OK!", entonces el problema es solo de ejecución, no de datos.

---

**Última actualización:** Enero 30, 2026  
**Versión:** 2.0
