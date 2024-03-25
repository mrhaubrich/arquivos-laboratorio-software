# Extrair dados de cliente para classe
import unittest

from classes.cliente import Cliente

class TestClienteExtraction(unittest.TestCase):
    """
        1. Dado que os dados de clientes estão corretos, então a aplicação deve instanciar objetos que representam o cliente.
        2. Dado que os dados de clientes estão incorretos, então a aplicação deve retornar um erro.
        3. Dado que os dados de clientes estão vazios, então a aplicação deve retornar um erro.
        4. Dado que os dados de clientes estão nulos, então a aplicação deve retornar um erro.
    """
    
    def test_extract_cliente(self):
        """
        Dado que os dados de clientes estão corretos, então a aplicação deve instanciar objetos que representam o cliente.
        """
        clientes_csv = "0;0000;0;0;Cliente Sauna;\n1;;;;Cliente 1;"

        clientes = Cliente.from_csv(clientes_csv)

        self.assertEqual(len(clientes), 2)

        self.assertEqual(clientes[0].id, 0)
        self.assertEqual(clientes[0].nome, "Cliente Sauna")

        self.assertEqual(clientes[1].id, 1)
        self.assertEqual(clientes[1].nome, "Cliente 1")

    def test_extract_cliente_incorrect_data(self):
        """
        Dado que os dados de clientes estão incorretos, então a aplicação deve retornar um erro.
        """
        clientes_csv = "0;0000;0;0;Cliente Sauna;\n1;;;;Cliente 1;\n2;;;;"

        self.assertRaises(ValueError, Cliente.from_csv, clientes_csv)


    def test_extract_cliente_empty_data(self):
        """
        Dado que os dados de clientes estão vazios, então a aplicação deve retornar um erro.
        """
        clientes_csv = ""

        self.assertRaises(ValueError, Cliente.from_csv, clientes_csv)

    def test_extract_cliente_null_data(self):
        """
        Dado que os dados de clientes estão nulos, então a aplicação deve retornar um erro.
        """
        clientes_csv = None

        self.assertRaises(ValueError, Cliente.from_csv, clientes_csv)

