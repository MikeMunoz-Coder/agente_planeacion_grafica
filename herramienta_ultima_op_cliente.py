from langchain.tools import BaseTool
from lector_csv import buscar_ultima_op_cliente


class HerramientaUltimaOPCliente(BaseTool):

    name: str = "buscar_ultima_op_cliente"

    description: str = """
    Utiliza esta herramienta cuando necesites encontrar
    la última Orden de Producción realizada para un cliente.

    Entrada esperada:
    Nombre del cliente.

    Ejemplo:
    JGB

    Retorna la información de la última OP registrada
    según la fecha de producción.
    """

    def _run(self, cliente: str):

        resultado = buscar_ultima_op_cliente(cliente)

        if resultado.empty:
            return (
                f"No se encontraron órdenes "
                f"para el cliente {cliente}"
            )

        return resultado.to_string()