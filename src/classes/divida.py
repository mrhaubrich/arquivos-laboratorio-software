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
    def get_dividas(clientes: list["Cliente"], pagamentos_nao_pagos: list[Pagamento]) -> list["Divida"]:
        """
        Retorna uma lista de dívidas.
        """
        dividas: list[Divida] = []
        for pagamento in pagamentos_nao_pagos:
            cliente = Cliente.get(pagamento.cliente, clientes)
            dividas.append(Divida(cliente, pagamento))

        return dividas