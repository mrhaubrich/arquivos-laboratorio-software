""" Given that a client exists
    Given that a payment exists
    Given that the payment is associated with the client
    Given that the payment was paid
    When I filter the debts
    Then the debt must not be returned
"""
from datetime import date
from behave import given, when, then
from lab_software.models import Cliente, Pagamento

@given("that a client exists for payed debts")
def step_impl(context):
    context.cliente = Cliente.objects.create(id=54564654, nome="João Silva")

@given("that a payment exists for payed debts")
def step_impl(context):
    data = date.today()
    context.pagamento = Pagamento(cliente_id=context.cliente.id, data=data, valor=100, pago=True)
    context.pagamento.save()

@given("that the payment is associated with the client for payed debts")
def step_impl(context):
    assert context.pagamento.cliente.id == context.cliente.id

@given("that the payment was paid")
def step_impl(context):
    assert context.pagamento.pago == True

@when("I filter the payed debts")
def step_impl(context):
    context.quitados = Pagamento.objects.filter_quitados()

@then("the payed debts must be returned")
def step_impl(context):
    assert context.quitados.count() == 1
    assert context.quitados[0].valor == 100
    assert context.quitados[0].pago == True
    assert context.quitados[0].cliente.id == context.cliente.id
    assert context.quitados[0].cliente.nome == "João Silva"
    assert context.quitados[0].data == date.today()
    