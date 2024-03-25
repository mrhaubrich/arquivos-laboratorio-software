from classes.csv_file_data import CSVFileData
from csv import reader


class Cliente(CSVFileData):
    """
    Classe que representa um cliente.
    """

    id: int
    nome: str

    def __init__(self, cliente_id: int, nome: str) -> None:
        self.id = cliente_id
        self.nome = nome

    @staticmethod
    def from_csv(file: str|None) -> list["Cliente"]:
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
            if len(row) != 6:
                raise ValueError("Dados de clientes incorretos.")
            clientes.append(Cliente(int(row[0]), row[4]))

        return clientes
