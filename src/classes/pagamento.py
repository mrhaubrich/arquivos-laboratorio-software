from typing import Union
from csv import reader
from classes.csv_file_data import CSVFileData


class Pagamento(CSVFileData):
    """
    Classe que representa um pagamento.
    """

    cliente: int
    data: int
    valor: float
    pago: bool

    def __init__(self, cliente: int, data: int, valor: float, pago: bool) -> None:
        self.cliente = cliente
        self.data = data
        self.valor = valor
        self.pago = pago

    @staticmethod
    def from_csv(file: Union[str, None]) -> list["Pagamento"]:
        """
        Extrai os dados de pagamentos de um arquivo CSV.
        """
        # idCliente;data;inutil;valor;pago;
        if file is None:
            raise ValueError("Dados de pagamentos nulos.")
        csv_reader = reader(file.split("\n"), delimiter=";")
        csv_reader = list(csv_reader)

        if len(csv_reader) == 0:
            raise ValueError("Dados de pagamentos vazios ou nulos.")

        pagamentos: list[Pagamento] = []

        for row in csv_reader:
            if len(row) != 6:
                raise ValueError("Dados de pagamentos incorretos.")
            pagamentos.append(
                Pagamento(int(row[0]), int(row[1]), float(row[3]), row[4] == "t")
            )

        return pagamentos
