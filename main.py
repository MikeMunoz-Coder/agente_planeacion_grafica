from orquestador import AgenteOrquestador


agente = AgenteOrquestador()


respuesta = agente.ejecutar(
    "¿Cuál es la información de la OP-1050?"
    #"¿Cuál es la última orden de producción realizada para el cliente JGB?"
    # "Busca trabajos similares relacionados con stickers adhesivos"
    """
    Analiza el documento PDF:
    documentos/orden_produccion_OP1050.pdf

    Extrae los datos más importantes:
    número de OP, cliente, producto, fecha,
    cantidad, material, tintas, troquel y dimensiones. 
    """
)


print(respuesta)