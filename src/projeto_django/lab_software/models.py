from csv import reader
from datetime import datetime
from typing import Union
from django.db import models

from lab_software.classes.csv_file_data import CSVFileData


# Create your models here.
class Cliente(models.Model, CSVFileData):
    """
    Classe que representa um cliente.
    """

    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)

    exceptions: list[str] = []

    @staticmethod
    def from_csv(file: Union[str, None], raise_exceptions: bool = False):
        """
        Extrai os dados de clientes de um arquivo CSV.
        """
        if file is None:
            raise ValueError("Dados de clientes nulos.")
        csv_reader = reader(file.split("\n"), delimiter=";")
        csv_reader = list(csv_reader)

        if len(csv_reader) == 0:
            raise ValueError("Dados de clientes vazios ou nulos.")

        for row in csv_reader:
            if len(row) != 6 or not row[0].isdigit():
                if raise_exceptions:
                    raise ValueError(f"Dados de clientes incorretos. Linha: {row}")
                else:
                    Cliente.exceptions.append(
                        f"Dados de clientes incorretos. Linha: {row}"
                    )
                    continue

            Cliente.objects.create(id=row[0], nome=row[1])

    @staticmethod
    def get(
        cliente_id: Union[int, None], clientes: Union[list["Cliente"], None]
    ) -> "Cliente":
        """
        Retorna um cliente a partir de um ID.
        """
        if cliente_id is None:
            raise ValueError("ID do cliente nulo.")
        if clientes is None:
            raise ValueError("Lista de clientes nula.")
        for cliente in clientes:
            if cliente.id == cliente_id:
                return cliente
        raise ValueError("Cliente não encontrado.")

    def __eq__(self, other: "Cliente") -> bool:
        return self.id == other.id and self.nome == other.nome

    def __str__(self):
        return str(self.nome)


class PagamentoManager(models.Manager):
    """
    Manager para a classe Pagamento.
    """

    def filter_nao_pagos(self):
        """
        Filtra os pagamentos que não foram pagos.
        """
        return super().get_queryset().filter(pago=False)

    def get_dividas(self):
        """
        Retorna uma lista de dívidas.
        """


class Pagamento(models.Model):
    """
    Classe que representa um pagamento.
    """

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateField()
    valor = models.FloatField()
    pago = models.BooleanField()

    objects = PagamentoManager()

    exceptions: list[str] = []

    @staticmethod
    def from_csv(file: Union[str, None], raise_exceptions: bool = False):
        """
        Extrai os dados de pagamentos de um arquivo CSV.
        """
        if file is None:
            raise ValueError("Dados de pagamentos nulos.")

        csv_reader = reader(file.split("\n"), delimiter=";")
        csv_reader = list(csv_reader)

        if len(csv_reader) == 0:
            raise ValueError("Dados de pagamentos vazios ou nulos.")

        cliente_ids = [row[2] for row in csv_reader]

        # Bulk query to check existence of Cliente objects
        existing_clientes = {
            cliente.id: cliente
            for cliente in Cliente.objects.filter(id__in=cliente_ids)
        }

        pagamentos = []
        for row in csv_reader:
            if (
                len(row) != 6
                or not row[0].isdigit()
                or not row[3].replace(".", "").isdigit()
                or row[4] not in ["t", "f"]
            ):
                if raise_exceptions:
                    raise ValueError(f"Dados de pagamentos incorretos. Linha: {row}")
                else:
                    Pagamento.exceptions.append(
                        f"Dados de pagamentos incorretos. Linha: {row}"
                    )
                    continue

            try:
                data = datetime.strptime(row[1], "%d%m%Y")
            except ValueError as e:
                e.args = (f"Data do pagamento incorreta. Linha: {row}",)
                if raise_exceptions:
                    raise e
                else:
                    Pagamento.exceptions.append(
                        f"Data do pagamento incorreta. Linha: {row}"
                    )
                    continue

            cliente_id = int(row[2])
            cliente = existing_clientes.get(cliente_id)
            if not cliente:
                if raise_exceptions:
                    raise ValueError(f"Cliente do pagamento incorreto. Linha: {row}")
                else:
                    Pagamento.exceptions.append(
                        f"Cliente do pagamento incorreto. Linha: {row}"
                    )
                    continue

            pagamentos.append(
                Pagamento(
                    cliente=cliente,
                    data=data,
                    valor=float(row[3].replace(",", ".")),
                    pago=row[4] == "t",
                )
            )

        print(f'Inserindo {len(pagamentos)} pagamentos')

        Pagamento.objects.bulk_create(pagamentos, batch_size=200)

    @staticmethod
    def filter_nao_pagos() -> list["Pagamento"]:
        """
        Filtra os pagamentos que não foram pagos.
        """
        return list(Pagamento.objects.filter(pago=False))

    @staticmethod
    def get_dividas() -> list["Pagamento"]:
        """
        Retorna uma lista de dívidas.
        """

    def __str__(self):
        return f"{self.cliente} - {self.data} - {self.valor} - {self.pago}"
