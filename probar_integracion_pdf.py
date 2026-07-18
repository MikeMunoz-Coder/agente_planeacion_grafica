from analizador_archivo_usuario import analizar_pdf_usuario



respuesta = analizar_pdf_usuario(
    "documentos/orden_produccion_OP1050.pdf"
)


print("\nRespuesta del agente:")
print(respuesta["output"])