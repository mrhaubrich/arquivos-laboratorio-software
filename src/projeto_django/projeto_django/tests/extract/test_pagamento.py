from datetime import date

from django.test import TestCase

from lab_software.models import Cliente, Pagamento


class TestPagamentoExtraction(TestCase):
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
        cliente = Cliente.objects.create(id=0, nome="Cliente 0")
        Pagamento.from_csv(pagamentos_csv, raise_exceptions=True)
        pagamentos = Pagamento.objects.all()

        self.assertEqual(pagamentos.count(), 1)

        self.assertEqual(pagamentos.get(valor=2).cliente, cliente)
        self.assertEqual(pagamentos.get(valor=2).data, date(2014, 2, 8))
        self.assertEqual(pagamentos.get(valor=2).valor, 2)
        self.assertEqual(pagamentos.get(valor=2).pago, True)

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
        Cliente.objects.create(id=1, nome="Cliente 1")

        self.assertRaises(ValueError, Pagamento.from_csv, pagamentos_csv, True)
