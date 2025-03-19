import os
import csv
import time
import logging
import requests
import argparse
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configuración de logging
logging.basicConfig(
    filename="scraper.log", level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def configurar_driver():
    """Configura y devuelve el WebDriver de Selenium."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Modo headless para mayor eficiencia
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    return driver

def limpiar_nombre_archivo(nombre):
    """Limpia el nombre del archivo eliminando caracteres no permitidos."""
    return re.sub(r'[\\/*?:"<>|]', "_", nombre)

def extraer_informacion_producto(driver):
    """Extrae información del producto de la página actual."""
    try:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        
        # Extracción de datos básicos
        nombre = soup.select_one("h1.product-meta__title")
        sku = soup.select_one("span.product-meta__sku-number")
        descripcion = soup.select_one("div.card__section.expandable-content .rte.text--pull p")
        precio = soup.select_one("div.price-list .price.price--highlight")
        imagen_element = soup.select_one("img.product-gallery__image")
        
        datos = {
            "Nombre": nombre.text.strip() if nombre else "N/A",
            "SKU": sku.text.strip() if sku else "N/A",
            "Descripción": descripcion.text.strip() if descripcion else "N/A",
            "Precio": precio.text.strip() if precio else "N/A",
            "URL Imagen": "https:" + imagen_element["data-zoom"] if imagen_element else "N/A"
        }
        
        # Extracción de información adicional desde la tabla
        additional_info = {}
        table_rows = soup.select("div.rte.text--pull table tr")
        for row in table_rows:
            cols = row.find_all("td")
            if len(cols) == 2:
                key = cols[0].text.strip().replace(":", "")
                value = cols[1].text.strip()
                additional_info[key] = value
        
        datos.update(additional_info)
        return datos
    except Exception as e:
        logging.error(f"Error al extraer información del producto: {e}")
        return None

def guardar_datos_csv(datos, archivo="productos.csv"):
    """Guarda los datos en un archivo CSV."""
    existe = os.path.exists(archivo)
    
    with open(archivo, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=datos.keys())
        if not existe:
            writer.writeheader()
        writer.writerow(datos)

def descargar_imagen(url, nombre):
    """Descarga y guarda una imagen desde la URL especificada."""
    if url == "N/A":
        return
    
    os.makedirs("imagenes", exist_ok=True)
    ruta = os.path.join("imagenes", limpiar_nombre_archivo(nombre) + ".jpg")
    
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(ruta, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            logging.info(f"Imagen guardada en: {ruta}")
        else:
            logging.warning(f"No se pudo descargar la imagen: {url}")
    except Exception as e:
        logging.error(f"Error al descargar la imagen {url}: {e}")

def navegar_pagina(driver, url):
    """Navega a la URL especificada y espera que la página se cargue."""
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    
    datos = extraer_informacion_producto(driver)
    if datos:
        guardar_datos_csv(datos)
        descargar_imagen(datos["URL Imagen"], datos["Nombre"])

def main():
    parser = argparse.ArgumentParser(description="Scraper de productos")
    parser.add_argument("url", help="URL del producto a extraer")
    args = parser.parse_args()
    
    driver = configurar_driver()
    
    try:
        navegar_pagina(driver, args.url)
    finally:
        driver.quit()
    
    logging.info("Scraping completado.")

if __name__ == "__main__":
    main()
