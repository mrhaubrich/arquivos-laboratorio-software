from behave import *
from lab_software.utils.read_file import read_file

@given("that the file does not exist")
def step_impl(context):
    context.file = "not_exists.txt"

@when("the application reads the file")
def step_impl(context):
    try:
        read_file(context.file)
    except FileNotFoundError as e:
        context.exception = e

@then("the application should return an error")
def step_impl(context):
    assert isinstance(context.exception, FileNotFoundError)

