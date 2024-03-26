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

    def print_exceptions(self, exceptions: list[str], exc_type: str):
        """Print the exceptions that occurred during the execution of the program"""
        # red
        table = Table(title=f"{exc_type} Exceptions", show_header=True, header_style="bold magenta", style="bold red", title_style="bold red")
        table.add_column("Exception")
        for exception in exceptions:
            table.add_row(exception)

        self.console.print(table)

