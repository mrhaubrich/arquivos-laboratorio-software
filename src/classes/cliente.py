from classes.csv_file_data import CSVFileData


class Cliente(CSVFileData):
    """
    Classe que representa um cliente.
    """

    id: int
    nome: str

    @staticmethod
    def from_csv(file: str) -> list["Cliente"]:
        raise NotImplementedError
