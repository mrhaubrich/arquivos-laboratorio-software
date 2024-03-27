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

    nao_pagos = Pagamento.filter_nao_pagos(pagamentos)
    dividas = Pagamento.get_dividas(clientes, nao_pagos)
    dividas_agrupadas = Pagamento.group_dividas(dividas)
    dividas_agrupadas = sorted(
        dividas_agrupadas, key=lambda divida: divida.valor, reverse=True
    )

    presentation = Presentation()

    if len(Cliente.exceptions) > 0:
        presentation.print_exceptions(Cliente.exceptions, "Cliente")

    if len(Pagamento.exceptions) > 0:
        presentation.print_exceptions(Pagamento.exceptions, "Pagamento")

    presentation.print_pagamentos(dividas_agrupadas, "Dívidas")

    pagos = Pagamento.filter_pagos(pagamentos)
    pagamentos_agrupados = Pagamento.group_dividas(pagos)
    pagamentos_agrupados = sorted(
        pagamentos_agrupados, key=lambda pagamento: pagamento.valor, reverse=True
    )

    presentation.print_pagamentos(pagamentos_agrupados, "Pagamentos Quitados")


if __name__ == "__main__":
    main()
