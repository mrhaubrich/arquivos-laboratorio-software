from csv import reader
from datetime import datetime
from typing import Union

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

    objects: list["Pagamento"] = []

    def __init__(self, cliente: Cliente, data: datetime, valor: float, pago: bool) -> None:
        self.cliente = cliente
        self.data = data
        self.valor = valor
        self.pago = pago

    @staticmethod
    def get_dividas(
        clientes: Union[list["Cliente"], None],
        pagamentos_nao_pagos: Union[list["Pagamento"], None],
    ) -> list["Pagamento"]:
        """
        Retorna uma lista de dívidas.
        """
        if clientes is None or pagamentos_nao_pagos is None:
            raise ValueError("Dados de clientes ou pagamentos nulos.")

        dividas: list[Pagamento] = []
        for pagamento in pagamentos_nao_pagos:
            dividas.append(Pagamento(pagamento.cliente, pagamento.data, pagamento.valor, pagamento.pago))

        return dividas

    @staticmethod
    def group_dividas(dividas: Union[list["Pagamento"], None]) -> list["Pagamento"]:
        """
        Agrupa as dívidas por cliente, somando os valores e colocando como pagamento.
        """
        if dividas is None:
            raise Exception("Dados de dívidas nulos")
        
        dividas_agrupadas: list[Pagamento] = []

        for divida in dividas:
            divida_agrupada = Pagamento(divida.cliente, divida.data, divida.valor, divida.pago)
            for divida_agrupada in dividas_agrupadas:
                if divida_agrupada.cliente.id == divida.cliente.id:
                    divida_agrupada.valor += divida.valor
                    break
            else:
                dividas_agrupadas.append(divida)

        return dividas_agrupadas
    
    @staticmethod
    def filter_pagos(
        pagamentos: Union[list["Pagamento"], None]
    ) -> list["Pagamento"]:
        """
        Filtra os pagamentos que foram pagos.
        """
        if pagamentos is None:
            raise ValueError("Dados de pagamentos nulos.")

        return [pagamento for pagamento in pagamentos if pagamento.pago]