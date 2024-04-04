import unittest
from datetime import datetime

from classes.cliente import Cliente
from classes.pagamento import Pagamento


class TestFilterLancamentosNaoPagos(unittest.TestCase):
    """
    1. Dado que os dados de pagamentos estão vazio, a funcionalidade deve retornar uma lista vazia.
    2. Dado que os dados de pagamentos estão nulos, a funcionalidade deve retornar um erro.
    3. Dado que os dados de pagamentos estão corretos, a funcionalidade deve retornar uma lista de pagamentos não pagos.
    """

    def test_filter_lancamentos_nao_pagos_empty_data(self):
        """
        Dado que os dados de pagamentos estão vazio, a funcionalidade deve retornar uma lista vazia.
        """
        pagamentos = []

        lancamentos_nao_pagos = Pagamento.filter_nao_pagos(pagamentos)

        self.assertEqual(len(lancamentos_nao_pagos), 0)

    def test_filter_lancamentos_nao_pagos_null_data(self):
        """
        Dado que os dados de pagamentos estão nulos, a funcionalidade deve retornar um erro.
        """
        pagamentos = None

        self.assertRaises(ValueError, Pagamento.filter_nao_pagos, pagamentos)

    def test_filter_lancamentos_nao_pagos(self):
        """
        Dado que os dados de pagamentos estão corretos, a funcionalidade deve retornar uma lista de pagamentos não pagos.
        """
        date = datetime.now()
        Cliente.objects = [
            Cliente(0, "João Silva"),
            Cliente(1, "Maria Souza"),
            Cliente(2, "José Santos"),
        ]
        pagamentos = [
            Pagamento(Cliente(0, "João Silva"), date, 0, False),
            Pagamento(Cliente(1, "Maria Souza"), date, 1, True),
            Pagamento(Cliente(2, "José Santos"), date, 2, False),
        ]

        lancamentos_nao_pagos = Pagamento.filter_nao_pagos(pagamentos)

        self.assertEqual(len(lancamentos_nao_pagos), 2)

        self.assertEqual(lancamentos_nao_pagos[0].cliente, Cliente(0, "João Silva"))
        self.assertEqual(lancamentos_nao_pagos[0].data, date)
        self.assertEqual(lancamentos_nao_pagos[0].valor, 0)
        self.assertEqual(lancamentos_nao_pagos[0].pago, False)

        self.assertEqual(lancamentos_nao_pagos[1].cliente, Cliente(2, "José Santos"))
        self.assertEqual(lancamentos_nao_pagos[1].data, date)
        self.assertEqual(lancamentos_nao_pagos[1].valor, 2)
        self.assertEqual(lancamentos_nao_pagos[1].pago, False)
