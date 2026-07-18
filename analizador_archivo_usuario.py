from cargador_pdf import guardar_pdf
from gestor_extracciones import obtener_extraccion
from adaptador_pdf import analizar_pdf_con_gemini



def analizar_pdf_usuario(ruta_archivo):


    # 1. Guardar archivo recibido

    ruta_guardada = guardar_pdf(
        ruta_archivo
    )


    # 2. Gestionar extracción

    resultado = obtener_extraccion(
        ruta_guardada,
        analizar_pdf_con_gemini
    )


    return resultado