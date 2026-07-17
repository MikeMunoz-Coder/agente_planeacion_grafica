from langchain.tools import BaseTool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser

from my_keys import GEMINI_API_KEY
#from my_models import GEMINI_FLASH
from my_models import GEMINI_PRIMARY
from lector_pdf import leer_pdf
from modelos_op import OrdenProduccion


class HerramientaAnalisisPDF(BaseTool):

    name: str = "analizar_documento_pdf"

    description: str = """
    Analiza documentos PDF relacionados con órdenes
    de producción.

    Utiliza esta herramienta cuando el usuario entregue
    un archivo PDF y necesite extraer información del trabajo.

    Devuelve:
    Número de OP,
    cliente,
    trabajo,
    cantidad,
    material,
    tintas,
    troquel,
    dimensiones
    y observaciones.
    """

    def _run(self, ruta_pdf: str):

        texto_documento = leer_pdf(ruta_pdf)


        llm = ChatGoogleGenerativeAI(
            api_key=GEMINI_API_KEY,
            model=GEMINI_PRIMARY,
            temperature=0
        )


        parser = JsonOutputParser(
            pydantic_object=OrdenProduccion
        )


        prompt = f"""
        Analiza la siguiente información de una orden
        de producción.

        Extrae los datos importantes y responde únicamente
        utilizando el formato JSON solicitado.

        Información del documento:

        {texto_documento}


        {parser.get_format_instructions()}
        """


        respuesta = llm.invoke(prompt)


        resultado = parser.parse(
            respuesta.content
        )


        return resultado