from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

#Registro de Usuario

# Crear carpetas necesarias
os.makedirs("Screenshots Proyecto", exist_ok=True)
os.makedirs("Descargas Proyecto", exist_ok=True)

# Inicializar navegador
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://demoqa.com/automation-practice-form")

    #RELLENAR CAMPOS NOMBRE Y APELLIDO
    driver.find_element(By.ID, "firstName").send_keys("Ana")
    driver.find_element(By.ID, "lastName").send_keys("Gómez")

    #RELLENAR CAMPOS EMAIL Y GENERO
    driver.find_element(By.ID, "userEmail").send_keys("ana.gomez@example.com")
    driver.find_element(By.XPATH, "//label[@for='gender-radio-2']").click() 
    
    #RELLENAR CAMPO TELEFONO
    driver.find_element(By.ID, "userNumber").send_keys("9876543210")

    # Seleccionar fecha de nacimiento
    driver.find_element(By.ID, "dateOfBirthInput").click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__year-select"))).send_keys("1985")
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__month-select"))).send_keys("February")
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='5']"))).click()

    # Subir archivo (ajusta el nombre si es necesario)
    ruta_imagen = os.path.expanduser("~/Downloads/CR7.jpg") 
    driver.find_element(By.ID, "uploadPicture").send_keys(ruta_imagen)

    # Enviar formulario
    driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "submit"))

    # Esperar modal y tomar screenshot
    time.sleep(2)
    driver.save_screenshot("Screenshots Proyecto/formulario_enviado.png")

finally:
    # Cerrar el navegador
    input("Presiona Enter para cerrar...")
    driver.quit()


    