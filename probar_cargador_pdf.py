from cargador_pdf import guardar_pdf

ruta_guardada = guardar_pdf(
    "documentos/orden_produccion_OP1050.pdf"
)

# ruta_guardada = guardar_pdf(
#     "documentos/imagen_producto.jpg"
# )

print("Archivo guardado correctamente:")
print(ruta_guardada)