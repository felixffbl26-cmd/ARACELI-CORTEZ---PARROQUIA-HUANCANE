# 📱 URL para Acceder desde tu Celular

## 🎯 Dirección Exacta

Abre esta URL en el navegador de tu celular:

```
http://192.168.1.71:8503
```

---

## 📋 Pasos Detallados

### 1️⃣ Verifica la WiFi
- Tu **celular** y tu **computadora** deben estar en la **misma red WiFi**
- Ejemplo: Ambos conectados a "WiFi-Casa" o "Movistar-XXXX"

### 2️⃣ Abre el Navegador
- En tu celular, abre cualquier navegador:
  - Chrome
  - Safari (iPhone)
  - Firefox
  - Edge
  - Cualquier otro navegador

### 3️⃣ Escribe la URL
- En la barra de direcciones, escribe exactamente:
  ```
  http://192.168.1.71:8503
  ```
- **IMPORTANTE:** Incluye el `http://` y el `:8503`

### 4️⃣ Presiona Enter/Ir
- El dashboard debería cargarse en tu celular

---

## ⚠️ Solución de Problemas

### ❌ "No se puede acceder al sitio" o "Página no disponible"

**Causa 1: No están en la misma WiFi**
- ✅ Solución: Conecta ambos dispositivos a la misma red

**Causa 2: El dashboard no está corriendo**
- ✅ Solución: Asegúrate que `DASHBOARD_V3.bat` esté abierto y corriendo en la computadora

**Causa 3: Firewall bloqueando**
- ✅ Solución temporal: Desactiva el firewall de Windows
  1. Busca "Firewall" en Windows
  2. Haz clic en "Activar o desactivar Firewall de Windows Defender"
  3. Desactiva para "Red privada"
  4. Prueba de nuevo
  5. **Recuerda reactivarlo después**

**Causa 4: La IP cambió**
- ✅ Solución: Ejecuta `OBTENER_IP.bat` para ver tu IP actual

---

## 🔄 Si la IP Cambió

Si reiniciaste tu computadora o router, la IP puede haber cambiado.

**Para obtener la nueva IP:**
1. Ejecuta `OBTENER_IP.bat`
2. Busca la línea que dice "Dirección IPv4"
3. Usa esa nueva IP en lugar de 192.168.1.71

---

## ✅ Verificación Rápida

Antes de intentar desde el celular, verifica en la computadora:

1. Abre el navegador en la computadora
2. Ve a: http://localhost:8503
3. Si funciona en la computadora, debería funcionar en el celular

---

## 📞 Ayuda Adicional

Si sigues teniendo problemas:

1. Verifica que el dashboard esté corriendo (ventana negra abierta)
2. Confirma que ambos dispositivos estén en la misma WiFi
3. Intenta desde otro dispositivo para descartar problemas del celular
4. Revisa `INSTRUCCIONES_RAPIDAS.md` para más detalles

---

**URL para copiar:**
```
http://192.168.1.71:8503
```

*Última actualización: 30/01/2026*
