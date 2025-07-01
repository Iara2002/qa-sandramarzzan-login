from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Función para ejecutar un caso de login
def probar_login(usuario, contraseña, nombre_archivo):
    driver = webdriver.Chrome()
    driver.get("https://distribuidores.sandramarzzan.com.ar/login.php")
    time.sleep(2)

    # Completar campos
    driver.find_element(By.NAME, "email").send_keys(usuario)
    driver.find_element(By.NAME, "doc").send_keys(contraseña)

    # Hacer clic en el botón
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    time.sleep(3)

    # Captura de pantalla
    driver.save_screenshot(nombre_archivo)

    # Cerrar navegador
    driver.quit()

# 🔴 Caso 1: Usuario vacío
probar_login("", "clave_prueba", "resultado_error_usuario.png")

# 🔴 Caso 2: Contraseña vacía
probar_login("usuario_prueba@mail.com", "", "resultado_error_contraseña.png")

# 🔴 Caso 3: Usuario y contraseña inválidos (usuario mal formado o credenciales incorrectas)
probar_login("usuario_invalido@mail.com", "clave_invalida", "resultado_login_invalido.png")
