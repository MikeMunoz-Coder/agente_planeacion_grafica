from orquestador import AgenteOrquestador


def iniciar_chat():

    print("=" * 50)
    print(" AGENTE DE PLANEACIÓN GRÁFICA IA ")
    print("=" * 50)

    print(
        """
Puedes realizar consultas como:

- ¿Cuál es la información de la OP-1050?
- ¿Cuál es la última OP del cliente JGB?
- Busca trabajos similares relacionados con stickers.
- Analiza un documento PDF.

Escribe 'salir' para terminar.
        """
    )


    agente = AgenteOrquestador()


    while True:

        pregunta = input("\nUsuario: ")


        if pregunta.lower() == "salir":
            print("Finalizando agente...")
            break


        respuesta = agente.ejecutar(
            pregunta
        )


        print("\nRespuesta:")
        print(respuesta["output"])



if __name__ == "__main__":
    iniciar_chat()