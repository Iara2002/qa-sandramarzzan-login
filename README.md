# 🧪 Test Automatizado: Login de Distribuidores Sandra Marzzan

Este proyecto automatiza el flujo de login del sitio de distribuidores de **Sandra Marzzan** utilizando **Python** y **Selenium WebDriver**.

---

## 🔍 **Objetivo**

Verificar que el formulario de acceso de la web funcione correctamente al ingresar distintos tipos de datos: campos vacíos e inicio de sesión inválido.

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

## 📸 **Evidencias**

### 🖼️ Caso 1: Usuario vacío

![Error usuario vacío](resultado_error_usuario.png)

---

### 🖼️ Caso 2: Contraseña vacía

![Error contraseña vacía](resultado_error_contraseña.png)

---

### 🖼️ Caso 3: Login inválido

![Login inválido](resultado_login_invalido.png)

---

## 🚀 **Cómo ejecutar los tests**

```bash
# 1. Clonar el repositorio
git clone https://github.com/tuusuario/tu-repositorio.git

# 2. Instalar Selenium
pip install selenium

# 3. Ejecutar el script
python nombre_del_script.py


