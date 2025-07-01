from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Leer usuario y contraseña desde variables de entorno
usuario = os.getenv("TEST_USER")
contraseña = os.getenv("TEST_PASS")

# Verificar que las variables estén definidas
if not usuario or not contraseña:
    raise Exception("ERROR: Las variables de entorno TEST_USER y TEST_PASS no están definidas.")

# Iniciar navegador
driver = webdriver.Chrome()
driver.get("https://distribuidores.sandramarzzan.com.ar/login.php")
time.sleep(2)

# Completar usuario y contraseña
driver.find_element(By.NAME, "email").send_keys(usuario)
driver.find_element(By.NAME, "doc").send_keys(contraseña)

# Click en botón
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(3)

# Captura de pantalla
driver.save_screenshot("resultado_login.png")

# Cerrar navegador
driver.quit()
