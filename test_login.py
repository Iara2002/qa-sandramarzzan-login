from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Iniciar navegador
driver = webdriver.Chrome()
driver.get("https://distribuidores.sandramarzzan.com.ar/login.php")
time.sleep(2)

# Completar usuario y contraseña
driver.find_element(By.NAME, "email").send_keys("usuario_prueba")
driver.find_element(By.NAME, "doc").send_keys("clave_prueba")

# Click en botón
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(3)

# Captura de pantalla
driver.save_screenshot("resultado_login.png")

# Cerrar navegador
driver.quit()
