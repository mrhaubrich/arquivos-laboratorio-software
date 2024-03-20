from datetime import datetime

from classes.cliente import Cliente
from classes.csv_file_data import CSVFileData


class Pagamento(CSVFileData):
    """
    Classe que representa um pagamento.
    """

    cliente: Cliente
    data: datetime
    valor: float
    pago: bool

    @staticmethod
    def from_csv(file: str) -> list["Pagamento"]:
        raise NotImplementedError
