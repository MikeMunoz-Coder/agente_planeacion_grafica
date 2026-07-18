from guardar_extraccion import guardar_json



datos = {

    "numero_op": "OP-1050",
    "cliente": "JGB",
    "material": "Vinilo adhesivo blanco",
    "cantidad": "5000 unidades"

}



ruta = guardar_json(
    "orden_produccion_OP1050.pdf",
    datos
)



print("Archivo JSON creado:")
print(ruta)