import unittest
from datetime import datetime

from classes.cliente import Cliente
from classes.pagamento import Pagamento


class TestFiltrarDividas(unittest.TestCase):
    """
    1. Dado que os dados de pagamentos estão vazios, a funcionalidade deve retornar uma lista vazia.
    2. Dado que os dados de pagamentos estão nulos, a funcionalidade deve retornar um erro.
    4. Dado que os dados de pagamentos estão corretos, a funcionalidade deve retornar uma lista de dívidas.
    """

    def test_dados_vazios(self):
        """Dado que os dados de pagamentos estão vazios, a funcionalidade deve retornar uma lista vazia."""
        clientes = []
        pagamentos_nao_pagos = []
        dividas = Pagamento.get_dividas(clientes, pagamentos_nao_pagos)
        self.assertEqual(dividas, [])

    def test_dados_nulos(self):
        """Dado que os dados de pagamentos estão nulos, a funcionalidade deve retornar um erro."""
        clientes = None
        pagamentos_nao_pagos = None
        with self.assertRaises(ValueError):
            Pagamento.get_dividas(clientes, pagamentos_nao_pagos)

    def test_dados_corretos(self):
        """Dado que os dados de pagamentos estão corretos, a funcionalidade deve retornar uma lista de dívidas."""
        clientes = [Cliente(54564654, "João Silva"), Cliente(1654654, "Maria Souza")]
        data = datetime.now()
        pagamentos_nao_pagos = [
            Pagamento(Cliente(54564654, "João Silva"), data, 100, False)
        ]
        dividas = Pagamento.get_dividas(clientes, pagamentos_nao_pagos)
        self.assertEqual(len(dividas), 1)
        self.assertEqual(dividas[0].cliente.id, 54564654)
        self.assertEqual(dividas[0].cliente.nome, "João Silva")
        self.assertEqual(dividas[0].data, data)
        self.assertEqual(dividas[0].valor, 100)
        self.assertEqual(dividas[0].pago, False)
