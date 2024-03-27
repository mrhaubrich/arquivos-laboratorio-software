from csv import reader
from typing import Union

from classes.csv_file_data import CSVFileData


class Cliente(CSVFileData):
    """
    Classe que representa um cliente.
    """

    id: int
    nome: str
    exceptions: list[str] = []

    objects: list["Cliente"] = []

    def __init__(self, cliente_id: int, nome: str) -> None:
        self.id = cliente_id
        self.nome = nome

    @staticmethod
    def from_csv(file: Union[str, None], raise_exceptions: bool = False):
        """
        Extrai os dados de clientes de um arquivo CSV.
        """
        if file is None:
            raise ValueError("Dados de clientes nulos.")
        csv_reader = reader(file.split("\n"), delimiter=";")
        csv_reader = list(csv_reader)

        if len(csv_reader) == 0:
            raise ValueError("Dados de clientes vazios ou nulos.")

        clientes: list[Cliente] = []

        for row in csv_reader:
            if len(row) != 6 or not row[0].isdigit():
                if raise_exceptions:
                    raise ValueError(f"Dados de clientes incorretos. Linha: {row}")
                else:
                    Cliente.exceptions.append(f"Dados de clientes incorretos. Linha: {row}")
                    continue
            clientes.append(Cliente(int(row[0]), row[4]))

        Cliente.objects = clientes

    @staticmethod
    def get(
        cliente_id: Union[int, None], clientes: Union[list["Cliente"], None]
    ) -> "Cliente":
        """
        Retorna um cliente a partir de um ID.
        """
        if cliente_id is None:
            raise ValueError("ID do cliente nulo.")
        if clientes is None:
            raise ValueError("Lista de clientes nula.")
        for cliente in clientes:
            if cliente.id == cliente_id:
                return cliente
        raise ValueError("Cliente não encontrado.")

    def __eq__(self, other: "Cliente") -> bool:
        return self.id == other.id and self.nome == other.nome
