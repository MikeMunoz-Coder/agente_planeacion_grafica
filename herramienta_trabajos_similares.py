from langchain.tools import BaseTool
from lector_csv import buscar_trabajos_similares


class HerramientaTrabajosSimilares(BaseTool):

    name: str = "buscar_trabajos_similares"

    description: str = """
    Utiliza esta herramienta cuando necesites encontrar
    trabajos anteriores similares dentro del histórico
    de producción.

    Entrada esperada:
    Una palabra o descripción del producto.

    Ejemplos:
    sticker
    etiqueta adhesiva
    vinilo
    material POP

    Retorna trabajos similares realizados anteriormente.
    """

    def _run(self, texto_busqueda: str):

        resultado = buscar_trabajos_similares(
            texto_busqueda
        )

        if resultado.empty:
            return (
                f"No se encontraron trabajos similares "
                f"para: {texto_busqueda}"
            )

        return resultado.to_string(index=False)