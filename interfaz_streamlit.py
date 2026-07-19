import streamlit as st

from analizador_archivo_usuario import analizar_pdf_usuario
from herramienta_chat_op import responder_sobre_op

st.set_page_config(
    page_title="Agente Planeación Gráfica IA",
    page_icon="📄"
)

# ------------------------------------
# Memoria temporal de Streamlit
# ------------------------------------

if "op_actual" not in st.session_state:

    st.session_state.op_actual = None

if "historial_chat" not in st.session_state:

    st.session_state.historial_chat = []


# ------------------------------------
# Función para mostrar información OP
# ------------------------------------

def mostrar_orden_produccion(datos):

    st.subheader(
        "📄 Información de Orden de Producción"
    )


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "Número OP",
            datos.get(
                "numero_op",
                "No disponible"
            )
        )


        st.write("**Cliente:**")

        st.write(
            datos.get(
                "cliente",
                "No disponible"
            )
        )


        st.write("**Nombre del trabajo:**")

        st.write(
            datos.get(
                "nombre_trabajo",
                "No disponible"
            )
        )


        st.write("**Fecha producción:**")

        st.write(
            datos.get(
                "fecha_produccion",
                "No disponible"
            )
        )


    with col2:

        st.write("**Cantidad:**")

        st.write(
            datos.get(
                "cantidad",
                "No disponible"
            )
        )


        st.write("**Material:**")

        st.write(
            datos.get(
                "material",
                "No disponible"
            )
        )


        st.write("**Número de tintas:**")

        st.write(
            datos.get(
                "numero_tintas",
                "No disponible"
            )
        )


        st.write("**Troquel:**")

        st.write(
            datos.get(
                "troquel",
                "No disponible"
            )
        )


    st.divider()


    st.write("**Dimensiones:**")

    st.write(
        datos.get(
            "dimensiones",
            "No disponible"
        )
    )


    st.write("**Tipo de producto:**")

    st.write(
        datos.get(
            "tipo_producto",
            "No disponible"
        )
    )


    st.write("**Observaciones:**")

    st.write(
        datos.get(
            "observaciones",
            "No disponible"
        )
    )



# ------------------------------------
# Configuración inicial de la página
# ------------------------------------


st.title(
    "📄 Agente de Planeación Gráfica IA"
)


st.write(
    """
Carga una Orden de Producción en PDF.
El agente analizará el documento y recuperará
la información del trabajo realizado.
"""
)



# ------------------------------------
# Carga del archivo PDF
# ------------------------------------

archivo = st.file_uploader(
    "Seleccione un archivo PDF",
    type=["pdf"]
)



if archivo:


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
            "Consultando información..."
        ):


            resultado = analizar_pdf_usuario(
                ruta_temporal
            )


        mostrar_orden_produccion(
            resultado
        )

        # Guardar OP actual
        st.session_state.op_actual = resultado


# ------------------------------------
# Chat sobre la OP cargada
# ------------------------------------

st.divider()


st.subheader(
    "💬 Consultar sobre la Orden de Producción"
)

# Mostrar historial anterior

for mensaje in st.session_state.historial_chat:

    st.write(
        "👤 Usuario:",
        mensaje["usuario"]
    )

    st.write(
        "🤖 IA:",
        mensaje["asistente"]
    )

    st.divider()

# Permitir nueva pregunta

if st.session_state.op_actual:

    pregunta = st.text_input(
        "Escriba su pregunta:"
    )


    if st.button(
        "Enviar pregunta"
    ):


        if pregunta:


            with st.spinner(
                "Generando respuesta..."
            ):


                respuesta = responder_sobre_op(
                    st.session_state.op_actual,
                    pregunta,
                    st.session_state.historial_chat
                )


            st.write(
                respuesta
            )

            st.session_state.historial_chat.append(
            {
                "usuario": pregunta,
                "asistente": respuesta
            }
)


        else:

            st.warning(
                "Ingrese una pregunta."
            )


else:


    st.info(
        "Primero cargue y analice una Orden de Producción."
    )