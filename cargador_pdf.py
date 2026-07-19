import os
import shutil


#CARPETA_DESTINO = "uploads/pdfs"

CARPETA_DESTINO = os.path.join(
    "uploads",
    "pdfs"
)


def validar_pdf(nombre_archivo):
    """
    Verifica que el archivo tenga extensión PDF.
    """

    return nombre_archivo.lower().endswith(".pdf")



def guardar_pdf(ruta_archivo):
    """
    Copia un archivo PDF hacia uploads/pdfs.

    Retorna la ruta final del archivo guardado.
    """

    nombre_archivo = os.path.basename(ruta_archivo)


    if not validar_pdf(nombre_archivo):
        raise ValueError(
            "El archivo seleccionado no es un PDF."
        )


    if not os.path.exists(CARPETA_DESTINO):
        os.makedirs(CARPETA_DESTINO)


    ruta_destino = os.path.join(
        CARPETA_DESTINO,
        nombre_archivo
    )


    shutil.copy(
        ruta_archivo,
        ruta_destino
    )


    return ruta_destino