from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Crear carpetas necesarias
os.makedirs("Screenshots Proyecto", exist_ok=True)
os.makedirs("Descargas Proyecto", exist_ok=True)

# Inicializar navegador
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://demoqa.com/alerts")

    #Alerta de confirmación
    driver.find_element(By.ID, "confirmButton").click()
    confirm_alert = wait.until(EC.alert_is_present())
    print("Texto de confirmación:", confirm_alert.text)
    time.sleep(2)  # Esperar para ver la alerta
    confirm_alert.accept()

    time.sleep(2)  # Esperar para ver el resultado en pantalla
    confirm_result = driver.find_element(By.ID, "confirmResult").text
    print("Resultado visible:", confirm_result)
    assert "You selected Ok" in confirm_result

    driver.save_screenshot("Screenshots Proyecto/alerta_confirmacion.png")

    #Alerta de Prompt
    driver.find_element(By.ID, "promtButton").click()
    prompt_alert = wait.until(EC.alert_is_present())
    print("Texto del prompt:", prompt_alert.text)
    time.sleep(2)  
    nombre = "Ana Gómez"
    prompt_alert.send_keys(nombre)
    prompt_alert.accept()

    time.sleep(2) 
    prompt_result = driver.find_element(By.ID, "promptResult").text
    print("Resultado visible:", prompt_result)
    assert nombre in prompt_result

    driver.save_screenshot("Screenshots Proyecto/alerta_prompt.png")

finally:
    input("Presiona Enter para cerrar...")
    driver.quit()
