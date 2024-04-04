from django.core.management.base import BaseCommand
from lab_software.models import Pagamento
from lab_software.utils.read_file import read_file


class Command(BaseCommand):
    help = "Importa pagamentos de um arquivo CSV."

    def add_arguments(self, parser):
        parser.add_argument("file", type=str, help="Caminho do arquivo CSV.")

    def handle(self, *args, **kwargs):
        file = kwargs["file"]
        file = read_file(file)
        Pagamento.from_csv(file)
        self.stdout.write(
            "Pagamentos importados com sucesso.", style_func=self.style.SUCCESS
        )
