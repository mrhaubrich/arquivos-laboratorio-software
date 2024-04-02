from datetime import datetime

import inquirer
from rich.console import Console
from rich.table import Table

from classes.pagamento import Pagamento

# from classes.divida import Divida


class Presentation:
    """
    Presentation class to handle the output of the application
    """

    def __init__(self):
        self.console = Console()

    def print(self, message):
        """Print a message to the console"""
        self.console.print(message)

    def pause(self):
        """Pause the execution of the program"""
        self.console.input("Pressione Enter para continuar...")
        self.console.clear()

    def print_pagamentos(self, pagamentos: list[Pagamento], title: str):
        """Print the debts of the clients"""
        table = Table(title=title)
        table.add_column("ID")
        table.add_column("Nome")
        table.add_column("Valor Devido")
        table.add_column("Data")
        for pagamento in pagamentos:
            table.add_row(
                str(pagamento.cliente.id),
                pagamento.cliente.nome,
                f"R$ {pagamento.valor:.2f}",
                datetime.strftime(pagamento.data, "%d/%m/%Y"),
            )

        self.console.print(table)

    def print_exceptions(self, exceptions: list[str], exc_type: str):
        """Print the exceptions that occurred during the execution of the program"""
        # red
        table = Table(
            title=f"{exc_type} Exceptions",
            show_header=True,
            header_style="bold magenta",
            style="bold red",
            title_style="bold red",
        )
        table.add_column("Exception")
        for exception in exceptions:
            table.add_row(exception)

        self.console.print(table)

    def show_menu(self):
        """Show the main menu of the application"""
        self.console.clear()
        questions = [
            inquirer.List(
                "menu",
                message="Escolha uma opção",
                choices=[
                    "Listar dívidas",
                    "Listar pagamentos",
                    "Sair",
                ],
            )
        ]

        choice = inquirer.prompt(questions)

        if choice is None:
            return

        return choice["menu"]

    def list_dividas(self, dividas: list[Pagamento]):
        """List the debts of the clients"""
        # order by date or by value
        questions = [
            inquirer.List(
                "order",
                message="Escolha a ordem de exibição",
                choices=["Data", "Valor"],
            )
        ]

        order = inquirer.prompt(questions)
        if order is None:
            return

        order = order["order"]

        if order == "Data":
            dividas = sorted(dividas, key=lambda divida: divida.data)
        else:
            dividas = sorted(dividas, key=lambda divida: divida.valor)

        self.print_pagamentos(dividas, "Dívidas")
