from langchain.tools import BaseTool
from lector_csv import buscar_por_op


class HerramientaConsultaOP(BaseTool):

    #name = "consulta_orden_produccion"
    name: str = "consulta_orden_produccion"

    description: str = """
    Utiliza esta herramienta cuando necesites consultar información
    específica de una Orden de Producción (OP).

    Entrada esperada:
    Número de OP, por ejemplo:
    OP-1050

    Retorna información del cliente, trabajo,
    material, cantidad, tintas, troquel,
    dimensiones y demás datos registrados.
    """

    def _run(self, numero_op: str):

        resultado = buscar_por_op(numero_op)

        if resultado.empty:
            return (
                f"No se encontró información para la orden "
                f"de producción {numero_op}"
            )

        return resultado.to_string(index=False)