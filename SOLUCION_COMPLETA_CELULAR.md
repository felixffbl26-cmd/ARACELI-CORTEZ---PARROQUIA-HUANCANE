# 🔥 Solución: No Puedo Acceder desde el Celular

## 🎯 Problema Identificado

**Causa más común:** El **Firewall de Windows** está bloqueando el puerto 8503.

---

## ✅ SOLUCIÓN RÁPIDA (Recomendada)

### Paso 1: Configurar Firewall Automáticamente

1. **Haz clic DERECHO** en: `CONFIGURAR_FIREWALL.bat`
2. Selecciona: **"Ejecutar como administrador"**
3. Haz clic en **"Sí"** cuando Windows pregunte
4. Espera a que diga: **"✅ REGLA CREADA EXITOSAMENTE"**
5. Intenta de nuevo desde tu celular: `http://192.168.1.71:8503`

> **Nota:** Si no tienes permisos de administrador, usa la solución manual abajo.

---

## 🔧 SOLUCIÓN MANUAL (Si la automática no funciona)

### Opción 1: Crear Regla en el Firewall

1. Presiona la tecla **Windows** en tu teclado
2. Escribe: **"Firewall"**
3. Abre: **"Firewall de Windows Defender con seguridad avanzada"**
4. En el panel izquierdo, haz clic en: **"Reglas de entrada"**
5. En el panel derecho, haz clic en: **"Nueva regla..."**
6. Selecciona: **"Puerto"** → Clic en **"Siguiente"**
7. Selecciona: **"TCP"**
8. En "Puertos locales específicos" escribe: **8503**
9. Clic en **"Siguiente"**
10. Selecciona: **"Permitir la conexión"** → **"Siguiente"**
11. Deja todas las opciones marcadas → **"Siguiente"**
12. Nombre: **"Dashboard Parroquia"**
13. Clic en **"Finalizar"**

### Opción 2: Desactivar Firewall Temporalmente (Solo para probar)

> ⚠️ **ADVERTENCIA:** Solo hazlo temporalmente para probar. Recuerda reactivarlo después.

1. Presiona la tecla **Windows**
2. Escribe: **"Firewall"**
3. Abre: **"Firewall de Windows Defender"**
4. Clic en: **"Activar o desactivar Firewall de Windows Defender"**
5. En **"Configuración de red privada"**, selecciona: **"Desactivar"**
6. Clic en **"Aceptar"**
7. Intenta acceder desde el celular
8. **Si funciona:** El problema era el firewall. Reactívalo y usa la Opción 1
9. **Si no funciona:** Reactiva el firewall y prueba otras soluciones abajo

---

## 🔍 Otras Verificaciones

### 1. Verificar que el Dashboard esté Corriendo

- La ventana de `DASHBOARD_V3.bat` debe estar **abierta**
- Debe mostrar: `"You can now view your Streamlit app..."`
- Si está cerrada, ábrela de nuevo

### 2. Verificar la WiFi

**En la computadora:**
```
1. Haz clic en el ícono de WiFi (esquina inferior derecha)
2. Anota el nombre de la red (ej: "Movistar-1234")
```

**En el celular:**
```
1. Ve a Configuración → WiFi
2. Verifica que esté conectado a la MISMA red
```

### 3. Verificar la IP

La IP puede cambiar si reiniciaste la computadora o el router.

**Ejecuta:** `OBTENER_IP.bat`

Busca la línea que dice "Dirección IPv4" y usa esa IP.

### 4. Probar en el Navegador de la Computadora

Antes de probar en el celular, verifica que funcione en la computadora:

1. Abre el navegador en tu computadora
2. Ve a: `http://localhost:8503`
3. **Si funciona:** El problema es de red/firewall
4. **Si NO funciona:** El problema es el dashboard

---

## 🚨 Problemas Avanzados

### Antivirus Bloqueando

Algunos antivirus (Avast, Norton, McAfee) bloquean conexiones de red.

**Solución:**
1. Abre tu antivirus
2. Busca "Configuración de firewall" o "Protección de red"
3. Agrega una excepción para el puerto 8503
4. O desactiva temporalmente el antivirus para probar

### VPN Activa

Si tienes una VPN activa, puede interferir.

**Solución:**
- Desactiva la VPN en la computadora
- Desactiva la VPN en el celular
- Intenta de nuevo

### Aislamiento de Puntos de Acceso (AP Isolation)

Algunos routers tienen esta función que impide que dispositivos se comuniquen entre sí.

**Solución:**
1. Accede a la configuración de tu router (generalmente `192.168.1.1`)
2. Busca "AP Isolation" o "Aislamiento de clientes"
3. Desactívalo
4. Reinicia el router

### Router con Doble WiFi (2.4GHz y 5GHz)

Si tu router tiene dos redes WiFi separadas:

**Solución:**
- Asegúrate que ambos dispositivos estén en la **misma banda**
- Ejemplo: Ambos en "WiFi-Casa-2.4GHz" o ambos en "WiFi-Casa-5GHz"

---

## ✅ Lista de Verificación Completa

Marca cada punto que hayas verificado:

- [ ] Dashboard corriendo (DASHBOARD_V3.bat abierto)
- [ ] Ambos dispositivos en la misma WiFi
- [ ] IP correcta (192.168.1.71)
- [ ] Firewall configurado (regla creada)
- [ ] Funciona en navegador de computadora (localhost:8503)
- [ ] Antivirus no está bloqueando
- [ ] No hay VPN activa
- [ ] Misma banda WiFi (2.4GHz o 5GHz)

---

## 🎯 Prueba Final

Después de configurar el firewall:

1. **En la computadora:** Abre `http://localhost:8503` → Debe funcionar
2. **En el celular:** Abre `http://192.168.1.71:8503` → Debe funcionar

---

## 📞 Ayuda Adicional

Si después de todo esto sigue sin funcionar:

1. Ejecuta: `SOLUCION_CELULAR.bat` para ver todas las opciones
2. Revisa el walkthrough para más detalles
3. Considera usar la computadora directamente si es urgente

---

**Archivos de Ayuda:**
- `CONFIGURAR_FIREWALL.bat` - Configura firewall automáticamente
- `SOLUCION_CELULAR.bat` - Guía interactiva
- `OBTENER_IP.bat` - Muestra tu IP actual
- `URL_PARA_CELULAR.bat` - Muestra la URL exacta

---

*Última actualización: 30/01/2026*
