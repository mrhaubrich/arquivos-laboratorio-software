import abc


class CSVFileData(metaclass=abc.ABCMeta):
    """
    Classe abstrata que define o comportamento de classes que podem ser instanciadas a partir de um arquivo CSV.
    """

    @abc.abstractmethod
    @staticmethod
    def from_csv(file: str) -> list["CSVFileData"]:
        """
        Método estático que cria uma instância da classe a partir de um arquivo CSV.
        """
        raise NotImplementedError
