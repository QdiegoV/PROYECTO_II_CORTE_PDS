from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

#Descarga y Carga de Archivos

# Crear carpetas necesarias
os.makedirs("Screenshots Proyecto", exist_ok=True)
descargas_path = os.path.abspath("Descargas Proyecto")
os.makedirs(descargas_path, exist_ok=True)

# Inicializar navegador
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://demoqa.com/upload-download")

    # Descargar archivo
    driver.find_element(By.ID, "downloadButton").click()
    time.sleep(5)  # Esperar a que se descargue el archivo

    # Subir archivo (ajusta la ruta si es necesario)
    ruta_imagen = os.path.expanduser("~/Downloads/CR7.jpg") 
    driver.find_element(By.ID, "uploadFile").send_keys(ruta_imagen)

    # Espera para asegurar que el nombre aparezca en la página (opcional)
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "uploadedFilePath"))
    )

    # Screenshot de resultado (aunque en headless, sirve para guardar evidencia)
    driver.save_screenshot("Screenshots Proyecto/carga_y_descarga.png")

finally:
    input("Presiona Enter para cerrar...")
    driver.quit()
