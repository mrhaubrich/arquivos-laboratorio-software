from classes.cliente import Cliente
from classes.pagamento import Pagamento
from classes.divida import Divida
from presentation.presentation import Presentation
from utils.read_file import read_file


def main():
    """Main function of the program."""
    clientes_file = read_file("assets/clientes.txt")
    pagamentos_file = read_file("assets/pagamentos.txt")
    clientes = Cliente.from_csv(clientes_file)
    pagamentos = Pagamento.from_csv(pagamentos_file)

    nao_pagos = Pagamento.filter_nao_pagos(pagamentos)
    dividas = Divida.get_dividas(clientes, nao_pagos)

    presentation = Presentation()
    presentation.print_dividas(dividas)
    

if __name__ == "__main__":
    main()