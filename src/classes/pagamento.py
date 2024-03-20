from datetime import datetime

from classes.cliente import Cliente


class Pagamento:
    cliente: Cliente
    data: datetime
    valor: float
    pago: bool