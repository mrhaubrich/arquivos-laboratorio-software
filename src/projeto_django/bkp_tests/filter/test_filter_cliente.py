import unittest

from classes.cliente import Cliente


class TestFilterCliente(unittest.TestCase):
    """
    1. Dado que o ID do cliente não existe, a funcionalidade deve retornar um erro.
    2. Dado que o ID do cliente existe, a funcionalidade deve retornar o cliente.
    3. Dado que o ID do cliente está vazio, a funcionalidade deve retornar um erro.
    4. Dado que o ID do cliente está nulo, a funcionalidade deve retornar um erro.
    """

    def test_filter_cliente_id_not_exists(self):
        """
        Dado que o ID do cliente não existe, a funcionalidade deve retornar um erro.
        """
        cliente_id = 0
        clientes = [
            Cliente(1, "Cliente 1"),
            Cliente(2, "Cliente 2"),
            Cliente(3, "Cliente 3"),
        ]

        self.assertRaises(ValueError, Cliente.get, cliente_id, clientes)

    def test_filter_cliente_id_exists(self):
        """
        Dado que o ID do cliente existe, a funcionalidade deve retornar o cliente.
        """
        cliente_id = 2
        clientes = [
            Cliente(1, "Cliente 1"),
            Cliente(2, "Cliente 2"),
            Cliente(3, "Cliente 3"),
        ]

        cliente = Cliente.get(cliente_id, clientes)

        self.assertEqual(cliente.id, 2)
        self.assertEqual(cliente.nome, "Cliente 2")

    def test_filter_cliente_id_empty(self):
        """
        Dado que o ID do cliente está vazio, a funcionalidade deve retornar um erro.
        """
        cliente_id = ""
        clientes = [
            Cliente(1, "Cliente 1"),
            Cliente(2, "Cliente 2"),
            Cliente(3, "Cliente 3"),
        ]

        self.assertRaises(ValueError, Cliente.get, cliente_id, clientes)

    def test_filter_cliente_id_null(self):
        """
        Dado que o ID do cliente está nulo, a funcionalidade deve retornar um erro.
        """
        cliente_id = None
        clientes = [
            Cliente(1, "Cliente 1"),
            Cliente(2, "Cliente 2"),
            Cliente(3, "Cliente 3"),
        ]

        self.assertRaises(ValueError, Cliente.get, cliente_id, clientes)
