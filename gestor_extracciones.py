import os

from consultar_extraccion import buscar_extraccion
from guardar_extraccion import guardar_json



def obtener_extraccion(
        nombre_pdf,
        funcion_analisis
):
    """
    Gestiona la extracción de información
    de un documento PDF.

    Si existe un JSON previo:
        devuelve la información guardada.

    Si no existe:
        ejecuta análisis,
        guarda resultado,
        devuelve información.
    """


    nombre_archivo = os.path.basename(
        nombre_pdf
    )


    # 1. Buscar extracción existente

    resultado = buscar_extraccion(
        nombre_archivo
    )


    if resultado:

        print(
            "Extracción encontrada en memoria JSON."
        )

        return resultado



    # 2. Si no existe,
    # analizar documento

    print(
        "No existe extracción previa. Analizando PDF..."
    )


    resultado = funcion_analisis(
        nombre_pdf
    )


    # 3. Guardar resultado

    guardar_json(
        nombre_archivo,
        resultado
    )


    return resultado