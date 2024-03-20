from datetime import datetime

from classes.cliente import Cliente
from classes.csv_file_data import CSVFileData


class Pagamento(CSVFileData):
    cliente: Cliente
    data: datetime
    valor: float
    pago: bool