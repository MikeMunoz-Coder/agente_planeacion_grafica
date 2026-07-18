from cargador_pdf import guardar_pdf
from orquestador import AgenteOrquestador



def analizar_pdf_usuario(ruta_archivo):

    # 1. Guardar archivo recibido
    ruta_guardada = guardar_pdf(
        ruta_archivo
    )


    # 2. Crear agente
    agente = AgenteOrquestador()


    # 3. Enviar ruta al agente

    pregunta = f"""
    Analiza el siguiente documento PDF:

    {ruta_guardada}

    Extrae la información más importante:
    número de OP,
    cliente,
    nombre del trabajo,
    fecha,
    cantidad,
    material,
    tintas,
    troquel
    y dimensiones.
    """


    respuesta = agente.ejecutar(
        pregunta
    )


    return respuesta