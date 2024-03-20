import unittest

from utils.read_file import read_file


class ReadFileTest(unittest.TestCase):
    """
    1. Dado que o arquivo não existe, então a aplicação deve retornar um erro.
    2. Dado que o arquivo de clientes existe, então a aplicação deve retornar sucesso.
    """
    
    def test_read_file_not_exists(self):
        """
        1. Dado que o arquivo não existe, então a aplicação deve retornar um erro.
        """
        file = 'not_exists.txt'
        # must throw an error
        self.assertRaises(FileNotFoundError, read_file, file)

    def test_read_pagamentos_file(self):
        """
        2. Dado que o arquivo de clientes existe, então a aplicação deve retornar sucesso.
        """
        file = 'tests/read_file/pagamentos_file_test.txt'
        # must return the file content
        self.assertEqual(read_file(file), 'Hello World!')
