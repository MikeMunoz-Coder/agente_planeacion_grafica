import pandas as pd


RUTA_CSV = "base_datos/ordenes_produccion.csv"


def cargar_ordenes():
    """
    Carga el archivo CSV histórico de órdenes de producción.
    """

    df = pd.read_csv(RUTA_CSV)

    return df



def buscar_por_op(numero_op):
    """
    Busca una orden específica por número de OP.
    """

    df = cargar_ordenes()

    resultado = df[
        df["numero_op"].str.upper() == numero_op.upper()
    ]

    return resultado



def buscar_por_cliente(cliente):
    """
    Busca todas las órdenes realizadas para un cliente.
    """

    df = cargar_ordenes()

    resultado = df[
        df["cliente"].str.upper() == cliente.upper()
    ]

    return resultado

#Paso 17

def buscar_ultima_op_cliente(cliente):
    """
    Busca la última orden de producción realizada
    para un cliente específico.
    """

    df = cargar_ordenes()

    resultado = df[
        df["cliente"].str.upper() == cliente.upper()
    ]

    if resultado.empty:
        return resultado

    resultado["fecha_produccion"] = pd.to_datetime(
        resultado["fecha_produccion"]
    )

    ultima_op = resultado.sort_values(
        by="fecha_produccion",
        ascending=False
    ).iloc[0]

    return ultima_op

# Paso 18 

def buscar_trabajos_similares(texto_busqueda):
    """
    Busca trabajos similares dentro del histórico
    utilizando coincidencias de texto.
    """

    df = cargar_ordenes()

    texto_busqueda = texto_busqueda.lower()

    columnas_busqueda = [
        "nombre_trabajo",
        "tipo_producto",
        "material",
        "observaciones"
    ]

    filtro = False

    for columna in columnas_busqueda:
        filtro = filtro | (
            df[columna]
            .astype(str)
            .str.lower()
            .str.contains(texto_busqueda)
        )

    resultado = df[filtro]

    return resultado