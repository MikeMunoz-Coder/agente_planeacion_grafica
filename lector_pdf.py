from pypdf import PdfReader


def leer_pdf(ruta_pdf):
    """
    Lee un archivo PDF y extrae todo el texto disponible.
    """

    lector = PdfReader(ruta_pdf)

    texto = ""

    for pagina in lector.pages:
        texto += pagina.extract_text()

    return texto