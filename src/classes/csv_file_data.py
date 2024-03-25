import abc
from typing import Union


class CSVFileData(metaclass=abc.ABCMeta):
    """
    Classe abstrata que define o comportamento de classes que podem ser instanciadas a partir de um arquivo CSV.
    """

    @staticmethod
    @abc.abstractmethod
    def from_csv(file: Union[str, None]) -> list["CSVFileData"]:
        """
        Método estático que cria uma instância da classe a partir de um arquivo CSV.
        """
        raise NotImplementedError
