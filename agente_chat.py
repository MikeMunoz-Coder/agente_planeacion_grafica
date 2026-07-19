from orquestador import AgenteOrquestador



class AgenteChat:


    def __init__(self):

        self.agente = AgenteOrquestador()



    def responder(
            self,
            pregunta
    ):


        resultado = self.agente.ejecutar(
            pregunta
        )


        return resultado["output"]