import streamlit as st

from analizador_archivo_usuario import analizar_pdf_usuario



st.set_page_config(
    page_title="Agente Planeación Gráfica IA",
    page_icon="📄"
)


st.title(
    "📄 Agente de Planeación Gráfica IA"
)


st.write(
    """
Carga una Orden de Producción en PDF
y el agente extraerá la información
del trabajo realizado.
"""
)


archivo = st.file_uploader(
    "Seleccione un archivo PDF",
    type=["pdf"]
)



if archivo:

    # ruta_temporal = (
    #     "uploads/pdfs/"
    #     + archivo.name
    # )
    
    ruta_temporal = archivo.name

    with open(
        ruta_temporal,
        "wb"
    ) as f:

        f.write(
            archivo.getbuffer()
        )


    st.success(
        "Archivo cargado correctamente."
    )


    if st.button(
        "Analizar documento"
    ):


        with st.spinner(
            "Analizando documento..."
        ):


            resultado = analizar_pdf_usuario(
                ruta_temporal
            )


        st.subheader(
            "Resultado del análisis"
        )


        st.json(
            resultado
        )