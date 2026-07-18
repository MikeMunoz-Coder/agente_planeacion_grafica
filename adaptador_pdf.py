from herramienta_analisis_pdf import HerramientaAnalisisPDF



def analizar_pdf_con_gemini(ruta_pdf):

    herramienta = HerramientaAnalisisPDF()

    resultado = herramienta._run(
        ruta_pdf
    )

    return resultado