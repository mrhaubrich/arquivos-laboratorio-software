from rich.console import Console
from rich.table import Table

from classes.divida import Divida


class Presentation:
    """
    Presentation class to handle the output of the application
    """

    def __init__(self):
        self.console = Console()

    def print(self, message):
        """Print a message to the console"""
        self.console.print(message)

    def print_dividas(self, dividas: list[Divida]):
        """Print the debts of the clients"""
        table = Table(title="Clientes Devedores")
        table.add_column("ID")
        table.add_column("Nome")
        table.add_column("Valor Devido")
        for divida in dividas:
            table.add_row(
                str(divida.cliente.id),
                divida.cliente.nome,
                f"R$ {divida.pagamento.valor:.2f}",
            )

        self.console.print(table)