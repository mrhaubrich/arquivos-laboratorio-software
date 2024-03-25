from classes.cliente import Cliente
from classes.pagamento import Pagamento


class Divida:
    """Classe Divida para representar a dívida de um cliente"""

    cliente: Cliente
    pagamento: Pagamento

    def __init__(self, cliente: Cliente, pagamento: Pagamento):
        self.cliente = cliente
        self.pagamento = pagamento

    @staticmethod
    def get_dividas(
        clientes: list["Cliente"], pagamentos_nao_pagos: list[Pagamento]
    ) -> list["Divida"]:
        """
        Retorna uma lista de dívidas.
        """
        dividas: list[Divida] = []
        for pagamento in pagamentos_nao_pagos:
            cliente = Cliente.get(pagamento.cliente, clientes)
            dividas.append(Divida(cliente, pagamento))

        return dividas

    @staticmethod
    def group_dividas(dividas: list["Divida"]) -> list["Divida"]:
        """
        Agrupa as dívidas por cliente, somando os valores e colocando como pagamento.
        """
        if dividas is None:
            raise Exception("Dados de dívidas nulos")

        dividas_agrupadas: list[Divida] = []
        for divida in dividas:
            divida_agrupada = Divida(divida.cliente, divida.pagamento)
            for divida_agrupada in dividas_agrupadas:
                if divida_agrupada.cliente.id == divida.cliente.id:
                    divida_agrupada.pagamento.valor += divida.pagamento.valor
                    break
            else:
                dividas_agrupadas.append(divida)

        return dividas_agrupadas
