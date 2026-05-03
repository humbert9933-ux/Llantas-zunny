import PyPDF2
import os

# Configuración del archivo
archivo_pdf = "Llantas.pdf"

def extraer_precios():
    print("--- INICIANDO LECTURA DE CATÁLOGO ---")
    
    # Verificar que el archivo esté ahí
    if not os.path.exists(archivo_pdf):
        print(f"Error: No se encuentra el archivo '{archivo_pdf}'")
        print("Archivos en esta carpeta:", os.listdir())
        return

    try:
        with open(archivo_pdf, "rb") as f:
            # Creamos el lector de PDF
            pdf_reader = PyPDF2.PdfReader(f)
            num_paginas = len(pdf_reader.pages)
            
            print(f"Archivo abierto: {archivo_pdf}")
            print(f"Total de páginas a procesar: {num_paginas}\n")

            for i in range(num_paginas):
                pagina = pdf_reader.pages[i]
                texto = pagina.extract_text()
                
                if texto:
                    print(f"--- DATOS PÁGINA {i+1} ---")
                    print(texto)
                    print("-" * 30)
                else:
                    print(f"[Página {i+1} no contiene texto extraíble]")

        print("\n--- EXTRACCIÓN COMPLETADA ---")

    except Exception as e:
        print(f"Ocurrió un fallo al leer el PDF: {e}")

if __name__ == "__main__":
    extraer_precios()
