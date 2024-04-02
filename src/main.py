from classes.cliente import Cliente
from classes.pagamento import Pagamento
from presentation.presentation import Presentation
from utils.read_file import read_file


def main():
    """Main function of the program."""
    clientes_file = read_file("assets/clientes.txt")
    pagamentos_file = read_file("assets/pagamentos.txt")
    Cliente.from_csv(clientes_file)
    Pagamento.from_csv(pagamentos_file)

    clientes = Cliente.objects
    pagamentos = Pagamento.objects

    presentation = Presentation()

    if len(Cliente.exceptions) > 0:
        presentation.print_exceptions(Cliente.exceptions, "Cliente")
        presentation.pause()

    if len(Pagamento.exceptions) > 0:
        presentation.print_exceptions(Pagamento.exceptions, "Pagamento")
        presentation.pause()

    option = presentation.show_menu()
    while option != "Sair":
        handle_option(option, clientes, pagamentos, presentation)
        option = presentation.show_menu()


def handle_option(option, clientes, pagamentos, presentation):
    """Handle the option chosen by the user"""
    if option == "Listar dívidas":
        nao_pagos = Pagamento.filter_nao_pagos(pagamentos)
        dividas = Pagamento.get_dividas(clientes, nao_pagos)
        dividas_agrupadas = Pagamento.group_dividas(dividas)
        presentation.list_dividas(dividas_agrupadas)
        presentation.pause()
    elif option == "Listar pagamentos":
        pagos = Pagamento.filter_pagos(pagamentos)
        pagamentos_agrupados = Pagamento.group_dividas(pagos)
        presentation.list_dividas(pagamentos_agrupados)
        presentation.pause()
    elif option == "Sair":
        return
    else:
        print(option)
        presentation.print("Opção inválida")


if __name__ == "__main__":
    main()
