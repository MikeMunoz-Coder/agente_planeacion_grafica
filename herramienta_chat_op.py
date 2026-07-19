from langchain_google_genai import ChatGoogleGenerativeAI

from my_keys import GEMINI_API_KEY
from my_models import GEMINI_PRIMARY



def responder_sobre_op(
        informacion_op,
        pregunta
):


    llm = ChatGoogleGenerativeAI(
        api_key=GEMINI_API_KEY,
        model=GEMINI_PRIMARY,
        temperature=0
    )


    prompt = f"""

    Eres un asistente experto en planeación gráfica.

    Responde únicamente utilizando
    la información de esta Orden de Producción:

    {informacion_op}


    Pregunta del usuario:

    {pregunta}


    Si la información no está disponible,
    indica que no existe ese dato
    en la orden de producción.

    """


    respuesta = llm.invoke(
        prompt
    )


    return respuesta.content