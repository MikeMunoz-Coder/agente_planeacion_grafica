import os
import json


CARPETA_JSON = os.path.join(
    "salidas",
    "extracciones_json"
)



def buscar_extraccion(nombre_pdf):

    """
    Busca si existe una extracción previa
    del documento PDF.
    """


    nombre_json = (
        nombre_pdf.rsplit(
            ".",
            1
        )[0]
        + ".json"
    )


    ruta_json = os.path.join(
        CARPETA_JSON,
        nombre_json
    )


    if not os.path.exists(
        ruta_json
    ):

        return None



    with open(
        ruta_json,
        "r",
        encoding="utf-8"
    ) as archivo:


        datos = json.load(
            archivo
        )


    return datos