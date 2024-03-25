import unittest

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
        pagamentos = [
            Pagamento(0, 0, 0, False),
            Pagamento(1, 1, 1, True),
            Pagamento(2, 2, 2, False),
        ]

        lancamentos_nao_pagos = Pagamento.filter_nao_pagos(pagamentos)

        self.assertEqual(len(lancamentos_nao_pagos), 2)

        self.assertEqual(lancamentos_nao_pagos[0].cliente, 0)
        self.assertEqual(lancamentos_nao_pagos[0].data, 0)
        self.assertEqual(lancamentos_nao_pagos[0].valor, 0)
        self.assertEqual(lancamentos_nao_pagos[0].pago, False)

        self.assertEqual(lancamentos_nao_pagos[1].cliente, 2)
        self.assertEqual(lancamentos_nao_pagos[1].data, 2)
        self.assertEqual(lancamentos_nao_pagos[1].valor, 2)
        self.assertEqual(lancamentos_nao_pagos[1].pago, False)