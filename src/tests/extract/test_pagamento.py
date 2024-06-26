import unittest

from datetime import datetime

from classes.pagamento import Pagamento
from classes.cliente import Cliente


class TestPagamentoExtraction(unittest.TestCase):
    """
        1. Dado que os dados de pagamentos estão corretos, então a aplicação deve instanciar objetos que representam o pagamento.
        2. Dado que os dados de pagamentos estão incorretos, então a aplicação deve retornar um erro.
        3. Dado que os dados de pagamentos estão vazios, então a aplicação deve retornar um erro.
        4. Dado que os dados de pagamentos estão nulos, então a aplicação deve retornar um erro.
        5. Dado que a data do pagamento está incorreta, então a aplicação deve retornar um erro.
        6. Dado que o cliente do pagamento não existe, então a aplicação deve retornar um erro.
    """

    def test_extract_pagamento(self):
        """
        Dado que os dados de pagamentos estão corretos, então a aplicação deve instanciar objetos que representam o pagamento.
        """
        pagamentos_csv = "0;8022014;1;2;t;"
        Cliente.objects = [Cliente(0, "Cliente 0")]
        Pagamento.from_csv(pagamentos_csv, raise_exceptions=True)
        pagamentos = Pagamento.objects

        self.assertEqual(len(pagamentos), 1)

        self.assertEqual(pagamentos[0].cliente, Cliente(0, "Cliente 0"))
        self.assertEqual(pagamentos[0].data, datetime(2014, 2, 8))
        self.assertEqual(pagamentos[0].valor, 2)
        self.assertEqual(pagamentos[0].pago, True)

    def test_extract_pagamento_incorrect_data(self):
        """
        Dado que os dados de pagamentos estão incorretos, então a aplicação deve retornar um erro.
        """
        pagamentos_csv = "0;8022014;1;2;t;\n1;8022014;1;2;t;\n2;8022014;1;2;"

        self.assertRaises(ValueError, Pagamento.from_csv, pagamentos_csv, True)

    def test_extract_pagamento_empty_data(self):
        """
        Dado que os dados de pagamentos estão vazios, então a aplicação deve retornar um erro.
        """
        pagamentos_csv = ""

        self.assertRaises(ValueError, Pagamento.from_csv, pagamentos_csv, True)

    def test_extract_pagamento_null_data(self):
        """
        Dado que os dados de pagamentos estão nulos, então a aplicação deve retornar um erro.
        """
        pagamentos_csv = None

        self.assertRaises(ValueError, Pagamento.from_csv, pagamentos_csv, True)

    def test_extract_pagamento_incorrect_date(self):
        """
        Dado que a data do pagamento está incorreta, então a aplicação deve retornar um erro.
        """
        pagamentos_csv = "0;3122014;1;2;t;"

        self.assertRaises(ValueError, Pagamento.from_csv, pagamentos_csv, True)

    def test_extract_pagamento_incorrect_cliente(self):
        """
        Dado que o cliente do pagamento não existe, então a aplicação deve retornar um erro.
        """
        pagamentos_csv = "0;8022014;1;2;t;"
        Cliente.objects = [Cliente(1, "Cliente 1")]

        self.assertRaises(ValueError, Pagamento.from_csv, pagamentos_csv, True)

        


