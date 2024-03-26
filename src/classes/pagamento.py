from csv import reader
from datetime import datetime
from typing import Union

from classes.csv_file_data import CSVFileData


class Pagamento(CSVFileData):
    """
    Classe que representa um pagamento.
    """

    cliente: int
    data: datetime
    valor: float
    pago: bool
    exceptions: list[str] = []

    objects: list["Pagamento"] = []

    def __init__(self, cliente: int, data: datetime, valor: float, pago: bool) -> None:
        self.cliente = cliente
        self.data = data
        self.valor = valor
        self.pago = pago

    @staticmethod
    def from_csv(file: Union[str, None], raise_exceptions: bool = False):
        """
        Extrai os dados de pagamentos de um arquivo CSV.
        """
        if file is None:
            raise ValueError("Dados de pagamentos nulos.")
        csv_reader = reader(file.split("\n"), delimiter=";")
        csv_reader = list(csv_reader)

        if len(csv_reader) == 0:
            raise ValueError("Dados de pagamentos vazios ou nulos.")

        pagamentos: list[Pagamento] = []

        for row in csv_reader:
            if len(row) != 6 or not row[0].isdigit() or not row[3].replace(".", "").isdigit() or row[4] not in ["t", "f"]:
                if raise_exceptions:
                    raise ValueError(f"Dados de pagamentos incorretos. Linha: {row}")
                else:
                    Pagamento.exceptions.append(f"Dados de pagamentos incorretos. Linha: {row}")
                    continue
            try:
                data = datetime.strptime(row[1], "%d%m%Y")
            except ValueError as e:
                e.args = (f"Data do pagamento incorreta. Linha: {row}",)
                if raise_exceptions:
                    raise e
                else:
                    Pagamento.exceptions.append(f"Data do pagamento incorreta. Linha: {row}")
                    continue
            pagamentos.append(
                Pagamento(int(row[0]), data, float(row[3]), row[4] == "t")
            )

        Pagamento.objects = pagamentos

    @staticmethod
    def filter_nao_pagos(
        pagamentos: Union[list["Pagamento"], None]
    ) -> list["Pagamento"]:
        """
        Filtra os pagamentos que não foram pagos.
        """
        if pagamentos is None:
            raise ValueError("Dados de pagamentos nulos.")

        return [pagamento for pagamento in pagamentos if not pagamento.pago]
