# 🧪 Test Automatizado: Login de Distribuidores Sandra Marzzan

Este proyecto automatiza el flujo de **login** del sitio de distribuidores de **Sandra Marzzan** utilizando **Python** y **Selenium WebDriver**.

---

## 🔍 **Objetivo**

Verificar que el formulario de acceso de la web funcione correctamente ante diferentes escenarios:

- Campos vacíos
- Credenciales inválidas
- Credenciales válidas

---

## 🛠️ **Herramientas utilizadas**

- **Lenguaje:** Python
- **Librería:** Selenium WebDriver
- **Navegador:** Google Chrome
- **Driver:** ChromeDriver

---

## 📝 **Casos de prueba**

### 🔴 **Caso 1: Usuario vacío**

| 🆔 | TC-001 |
|----|--------|
| **Descripción** | Validar que el sistema muestre un error cuando el campo de usuario está vacío. |
| **Datos de prueba** | `Usuario: ""`<br>`Contraseña: "clave_prueba"` |
| **Resultado esperado** | El formulario muestra un mensaje de error indicando que falta completar el usuario. |
| **Resultado obtenido** | ✅ El navegador abrió, se completó el campo de contraseña, se hizo clic y se tomó la captura correctamente. |

---

### 🔴 **Caso 2: Contraseña vacía**

| 🆔 | TC-002 |
|----|--------|
| **Descripción** | Validar que el sistema muestre un error cuando el campo de contraseña está vacío. |
| **Datos de prueba** | `Usuario: "usuario_prueba"`<br>`Contraseña: ""` |
| **Resultado esperado** | El formulario muestra un mensaje de error indicando que falta completar la contraseña. |
| **Resultado obtenido** | ✅ El navegador abrió, se completó el campo de usuario, se hizo clic y se tomó la captura correctamente. |

---

### 🔴 **Caso 3: Login inválido**

| 🆔 | TC-003 |
|----|--------|
| **Descripción** | Validar que el sistema rechace el acceso cuando se ingresan credenciales incorrectas. |
| **Datos de prueba** | `Usuario: "usuario_invalido"`<br>`Contraseña: "clave_invalida"` |
| **Resultado esperado** | El formulario muestra un mensaje de error de credenciales incorrectas o acceso denegado. |
| **Resultado obtenido** | ✅ El navegador abrió, se completaron los campos, se hizo clic y se tomó la captura correctamente. |

---

### ✅ **Caso 4: Login válido**

| 🆔 | TC-004 |
|----|--------|
| **Descripción** | Validar que el sistema permita el acceso con credenciales válidas. |
| **Datos de prueba** | `Usuario` y `Contraseña` definidos en variables de entorno: `TEST_USER` y `TEST_PASS`. |
| **Resultado esperado** | El usuario accede correctamente al sistema. |
| **Resultado obtenido** | ✅ El navegador abrió, se completaron los campos, se hizo clic y se tomó la captura correctamente. |

---

## 📸 **Evidencias**

### 🖼️ Caso 1: Usuario vacío

![Error usuario vacío](screenshots/resultado_error_usuario.png)

---

### 🖼️ Caso 2: Contraseña vacía

![Error contraseña vacía](screenshots/resultado_error_contraseña.png)

---

### 🖼️ Caso 3: Login inválido

![Login inválido](screenshots/resultado_login_invalido.png)

---

### 🖼️ Caso 4: Login válido

![Login exitoso](screenshots/resultado_login.png)

---

## 🚀 **Cómo ejecutar los tests**

### 🔴 Para los casos de **errores (login inválido)**:

```bash
python login_invalid.py

