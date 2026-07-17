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