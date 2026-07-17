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