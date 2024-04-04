import unittest
from datetime import datetime

from classes.cliente import Cliente
from classes.pagamento import Pagamento


class TestGroupDividas(unittest.TestCase):
    """
    1. Dado que os dados de dívidas estão vazios, a funcionalidade deve retornar uma lista vazia.
    2. Dado que os dados de dívidas estão nulos, a funcionalidade deve retornar um erro.
    3. Dado que os dados de dívidas estão corretos, a funcionalidade deve retornar uma lista de dívidas agrupadas por cliente.
    """

    def test_dados_vazios(self):
        """Dado que os dados de dívidas estão vazios, a funcionalidade deve retornar uma lista vazia."""
        dividas = []
        dividas_agrupadas = Pagamento.group_dividas(dividas)
        self.assertEqual(dividas_agrupadas, [])

    def test_dados_nulos(self):
        """Dado que os dados de dívidas estão nulos, a funcionalidade deve retornar um erro."""
        dividas = None
        with self.assertRaises(Exception):
            Pagamento.group_dividas(dividas)

    def test_dados_corretos(self):
        """Dado que os dados de dívidas estão corretos, a funcionalidade deve retornar uma lista de dívidas agrupadas por cliente."""
        data = datetime.now()
        clientes = [Cliente(54564654, "João Silva"), Cliente(1654654, "Maria Souza")]
        pagamentos_nao_pagos = [
            Pagamento(Cliente(54564654, "João Silva"), data, 100, False),
            Pagamento(Cliente(54564654, "João Silva"), data, 200, False),
            Pagamento(Cliente(1654654, "Maria Souza"), data, 500, False),
        ]
        dividas = Pagamento.get_dividas(clientes, pagamentos_nao_pagos)
        dividas_agrupadas = Pagamento.group_dividas(dividas)
        self.assertEqual(len(dividas_agrupadas), 2)
        self.assertEqual(dividas_agrupadas[0].cliente.id, 54564654)
        self.assertEqual(dividas_agrupadas[0].cliente.nome, "João Silva")
        self.assertEqual(dividas_agrupadas[0].valor, 300)
        self.assertEqual(dividas_agrupadas[0].pago, False)

        self.assertEqual(dividas_agrupadas[1].cliente.id, 1654654)
        self.assertEqual(dividas_agrupadas[1].cliente.nome, "Maria Souza")
        self.assertEqual(dividas_agrupadas[1].valor, 500)
        self.assertEqual(dividas_agrupadas[1].pago, False)
