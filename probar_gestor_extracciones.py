from gestor_extracciones import obtener_extraccion



def analisis_simulado(ruta):

    print(
        "Ejecutando análisis simulado..."
    )


    return {

        "numero_op": "OP-1050",
        "cliente": "JGB",
        "material": "Vinilo adhesivo blanco"

    }

resultado = obtener_extraccion(
    "orden_produccion_OP1050.pdf",
    analisis_simulado
)


print("\nResultado:")
print(resultado)