import os
import json


CARPETA_SALIDA = os.path.join(
    "salidas",
    "extracciones_json"
)



def guardar_json(nombre_archivo, datos):

    """
    Guarda la extracción de un documento PDF
    en formato JSON.
    """


    if not os.path.exists(
        CARPETA_SALIDA
    ):

        os.makedirs(
            CARPETA_SALIDA
        )


    nombre_json = (
        nombre_archivo.rsplit(
            ".",
            1
        )[0]
        + ".json"
    )


    ruta_json = os.path.join(
        CARPETA_SALIDA,
        nombre_json
    )


    with open(
        ruta_json,
        "w",
        encoding="utf-8"
    ) as archivo:


        json.dump(
            datos,
            archivo,
            indent=4,
            ensure_ascii=False
        )


    return ruta_json