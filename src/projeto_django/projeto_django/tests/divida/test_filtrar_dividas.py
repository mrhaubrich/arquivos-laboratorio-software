from django.test import TestCase
from datetime import date, datetime

from lab_software.models import Cliente, Pagamento



class TestFiltrarDividas(TestCase):
    """
    1. Dado que os dados de pagamentos estão vazios, a funcionalidade deve retornar uma lista vazia.
    2. Dado que os dados de pagamentos estão nulos, a funcionalidade deve retornar um erro.
    4. Dado que os dados de pagamentos estão corretos, a funcionalidade deve retornar uma lista de dívidas.
    """

    def test_dados_vazios(self):
        """Dado que os dados de pagamentos estão vazios, a funcionalidade deve retornar uma lista vazia."""
        dividas = Pagamento.objects.get_dividas()
        self.assertEqual(dividas, {})

    def test_dados_corretos(self):
        """Dado que os dados de pagamentos estão corretos, a funcionalidade deve retornar uma lista de dívidas."""
        # Cliente.objects.bulk_create(Cliente(54564654, "João Silva"), Cliente(1654654, "Maria Souza")]
        Cliente.objects.create(id=54564654, nome="João Silva")
        Cliente.objects.create(id=1654654, nome="Maria Souza")
        data = date.today()
        pagamento = Pagamento(cliente_id=54564654, data=data, valor=100, pago=False)
        pagamento.save()
        pagamento = Pagamento(cliente_id=1654654, data=data, valor=50, pago=False)
        pagamento.save()

        dividas = list(Pagamento.objects.get_dividas().values())
        self.assertEqual(len(dividas), 2)
        self.assertEqual(dividas[0].cliente.id, 54564654)
        self.assertEqual(dividas[0].cliente.nome, "João Silva")
        self.assertEqual(dividas[0].data, data)
        self.assertEqual(dividas[0].valor, 100)
        self.assertEqual(dividas[0].pago, False)

        self.assertEqual(dividas[1].cliente.id, 1654654)
        self.assertEqual(dividas[1].cliente.nome, "Maria Souza")
        self.assertEqual(dividas[1].data, data)
        self.assertEqual(dividas[1].valor, 50)
        self.assertEqual(dividas[1].pago, False)
