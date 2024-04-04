from csv import reader
from typing import Union

from classes.csv_file_data import CSVFileData


class Cliente(CSVFileData):
    """
    Classe que representa um cliente.
    """

    id: int
    nome: str

    objects: list["Cliente"] = []

    def __init__(self, cliente_id: int, nome: str) -> None:
        self.id = cliente_id
        self.nome = nome

    