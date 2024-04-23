""" Dado que um cliente existe
 Dado que um pagamento existe
 Dado que o pagamento está associado ao cliente
 Dado que o pagamento não foi pago
 Quando eu filtrar as dívidas
 Então a dívida deve ser retornada
"""
from datetime import date
from behave import given, when, then
from lab_software.models import Cliente, Pagamento

@given("that a client exists for debts")
def step_impl(context):
    context.cliente = Cliente.objects.create(id=54564654, nome="João Silva")

@given("that a payment exists for debts")
def step_impl(context):
    data = date.today()
    context.pagamento = Pagamento(cliente_id=context.cliente.id, data=data, valor=100, pago=False)
    context.pagamento.save()

@given("that the payment is associated with the client for debts")
def step_impl(context):
    assert context.pagamento.cliente.id == context.cliente.id

@given("that the payment was not paid")
def step_impl(context):
    assert context.pagamento.pago == False

@when("I filter the debts")
def step_impl(context):
    context.dividas = Pagamento.objects.get_dividas()

@then("the debt must be returned")
def step_impl(context):
    assert context.dividas[context.cliente.id].valor == 100
    assert context.dividas[context.cliente.id].pago == False
    assert context.dividas[context.cliente.id].cliente.id == context.cliente.id
    assert context.dividas[context.cliente.id].cliente.nome == "João Silva"
    assert context.dividas[context.cliente.id].data == date.today()