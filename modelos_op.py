from pydantic import BaseModel, Field
from typing import List


class OrdenProduccion(BaseModel):

    numero_op: str = Field(
        description="Número de la orden de producción asociada al trabajo."
    )

    cliente: str = Field(
        description="Nombre del cliente para quien se realizó el trabajo."
    )

    nombre_trabajo: str = Field(
        description="Nombre o descripción comercial del trabajo realizado."
    )

    fecha_produccion: str = Field(
        description="Fecha en la que fue producido el trabajo."
    )

    cantidad: str = Field(
        description="Cantidad o tiraje producido."
    )

    material: str = Field(
        description="Material utilizado en la fabricación del producto gráfico."
    )

    numero_tintas: str = Field(
        description="Cantidad de tintas utilizadas en impresión."
    )

    troquel: str = Field(
        description="Código o descripción del troquel utilizado."
    )

    dimensiones: str = Field(
        description="Medidas finales del producto."
    )

    tipo_producto: str = Field(
        description="Tipo de producto gráfico fabricado."
    )

    observaciones: str = Field(
        description="Información adicional o características especiales del trabajo."
    )

    etiquetas: List[str] = Field(
        description="Palabras clave relacionadas con el trabajo."
    )