# 🛠 Web Scraping de Productos 🚀

Este proyecto es un **Web Scraper** desarrollado en Python que extrae información de productos de e-commerce usando **Selenium y BeautifulSoup**.  
Puede **adaptarse** a diferentes tiendas en línea como **Amazon, eBay, Mercado Libre** y más.

---

## 📦 Instalación de Dependencias 📥

Para ejecutar este script, primero asegúrate de tener **Python 3** instalado. Luego, instala las dependencias con:

```sh
pip install -r requirements.txt
```

Si aún no tienes el archivo `requirements.txt`, créalo y agrega las siguientes líneas:

```
requests
beautifulsoup4
selenium
webdriver-manager
```

---

## 🚀 Ejecución del Script 🖥️

Para iniciar el scraping, usa el siguiente comando:

```sh
python web-scraping-productos.py "URL_DEL_PRODUCTO"
```

📌 **Ejemplo de uso:**
```sh
python web-scraping-productos.py "https://www.ejemplo.com/producto"
```

Los datos extraídos se guardarán en `productos.csv`, y las imágenes se almacenarán en la carpeta `imagenes/`.

---

## 🔄 Adaptabilidad del Script 🔧

Este **Web Scraper** es **modificable** según las necesidades del cliente. Algunas personalizaciones posibles incluyen:

✅ **Scraping en otras plataformas**: Amazon, eBay, AliExpress, Mercado Libre, etc.  
✅ **Filtrar información específica**: Solo productos con descuento, más vendidos, en stock, etc.  
✅ **Exportar datos a diferentes formatos**: Excel, JSON, bases de datos SQL.  
✅ **Automatización programada**: Scraping diario/semanal.  
✅ **Integración con APIs externas** para análisis avanzado.  

💡 *Si necesitas una adaptación personalizada, ¡contáctame para discutir los detalles!*  

---

## 📂 Estructura del Proyecto 📁

```
web-scraping-productos/
│── imagenes/              # Carpeta donde se guardan las imágenes descargadas
│── productos.csv          # Archivo con la información extraída
│── web-scraping-productos.py  # Script principal de scraping
│── README.md              # Documentación del proyecto
│── requirements.txt       # Lista de dependencias necesarias
│── scraper.log            # Registro de errores y actividad
```

---

## 📸 Ejemplo de Resultado 📊

Aquí puedes ver cómo se guarda la información extraída en `productos.csv`:

![Ejemplo CSV](https://github.com/DavidGarcia08084/web-scraping-productos/blob/main/Captura%20de%20pantalla%202025-03-19%20181206.png?raw=true)

---

## 📧 Contacto 💼

Estoy disponible para proyectos en:  
🔹 [Upwork](https://www.upwork.com/freelancers/~0175d00bb47d61d93f)  
🔹 [Fiverr](https://es.fiverr.com/jose_garcia_08/buying?source=avatar_menu_profile)  
🔹 [Freelancer](https://www.freelancer.com/u/josedavidg)    

📩 **Email:** j.david.08084@gmail.com  
📩 **Si necesitas automatizar procesos con Web Scraping, contáctame.** 🚀





