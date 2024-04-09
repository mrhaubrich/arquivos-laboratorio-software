from datetime import date

from django.test import TestCase

from lab_software.models import Cliente, Pagamento


class TestFilterLancamentosNaoPagos(TestCase):
    """
    1. Dado que os dados de pagamentos estão vazios, a funcionalidade deve retornar uma lista vazia.
    2. Dado que os dados de pagamentos estão nulos, a funcionalidade deve retornar um erro.
    3. Dado que os dados de pagamentos estão corretos, a funcionalidade deve retornar uma lista de pagamentos já pagos além do valor não pago.
    """

    def test_filter_lancamentos_nao_pagos_empty_data(self):
        """
        Dado que os dados de pagamentos estão vazios, a funcionalidade deve retornar uma lista vazia.
        """
        lancamentos_nao_pagos = Pagamento.objects.filter_quitados()

        self.assertEqual(lancamentos_nao_pagos.count(), 0)

    def test_filter_lancamentos_nao_pagos(self):
        """
        Dado que os dados de pagamentos estão corretos, a funcionalidade deve retornar uma lista de pagamentos já pagos além do valor não pago.
        """
        data = date.today()
        cliente0 = Cliente(id=0, nome="João Silva")
        cliente1 = Cliente(id=1, nome="Maria Souza")
        cliente2 = Cliente(id=2, nome="José Santos")

        clientes = [
            cliente0,
            cliente1,
            cliente2,
        ]

        Cliente.objects.bulk_create(clientes)

        pagamentos = [
            Pagamento(cliente=cliente0, data=data, valor=0, pago=False),
            Pagamento(cliente=cliente1, data=data, valor=1, pago=True),
            Pagamento(cliente=cliente2, data=data, valor=2, pago=False),
        ]

        Pagamento.objects.bulk_create(pagamentos)

        lancamentos_nao_pagos = Pagamento.objects.filter_quitados()

        self.assertEqual(lancamentos_nao_pagos.count(), 1)

        self.assertEqual(lancamentos_nao_pagos[0].cliente, cliente1)
        self.assertEqual(lancamentos_nao_pagos[0].data, data)
        self.assertEqual(lancamentos_nao_pagos[0].valor, 1)
        self.assertEqual(lancamentos_nao_pagos[0].pago, True)
