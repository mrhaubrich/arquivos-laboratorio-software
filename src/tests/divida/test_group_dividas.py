import unittest
from classes.divida import Divida
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
        dividas_agrupadas = Divida.group_dividas(dividas)
        self.assertEqual(dividas_agrupadas, [])

    def test_dados_nulos(self):
        """Dado que os dados de dívidas estão nulos, a funcionalidade deve retornar um erro."""
        dividas = None
        with self.assertRaises(Exception):
            Divida.group_dividas(dividas)

    def test_dados_corretos(self):
        """Dado que os dados de dívidas estão corretos, a funcionalidade deve retornar uma lista de dívidas agrupadas por cliente."""
        clientes = [
            Cliente(54564654, "João Silva"),
            Cliente(1654654, "Maria Souza")
        ]
        pagamentos_nao_pagos = [
            Pagamento(54564654, 1654654, 100, False),
            Pagamento(54564654, 1654654, 200, False),
            Pagamento(1654654, 54564654, 500, False)
        ]
        dividas = Divida.get_dividas(clientes, pagamentos_nao_pagos)
        dividas_agrupadas = Divida.group_dividas(dividas)
        self.assertEqual(len(dividas_agrupadas), 2)
        self.assertEqual(dividas_agrupadas[0].cliente.id, 54564654)
        self.assertEqual(dividas_agrupadas[0].cliente.nome, "João Silva")
        self.assertEqual(dividas_agrupadas[0].pagamento.valor, 300)
        self.assertEqual(dividas_agrupadas[0].pagamento.pago, False)

        self.assertEqual(dividas_agrupadas[1].cliente.id, 1654654)
        self.assertEqual(dividas_agrupadas[1].cliente.nome, "Maria Souza")
        self.assertEqual(dividas_agrupadas[1].pagamento.valor, 500)
        self.assertEqual(dividas_agrupadas[1].pagamento.pago, False)


    