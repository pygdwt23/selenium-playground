import allure
import pytest
import logging
from pages.simple_form_demo import simpleFormDemo
from pages.input_form_submit import inputFormSubmit

@allure.title("TC001 - Single Input Field")
@allure.severity(allure.severity_level.NORMAL)
def test_TC001(conftest):
    tc001 = simpleFormDemo(conftest)
    tc001.test_single_input_field()

@allure.title("TC002 - Two Input Field")
@allure.severity(allure.severity_level.NORMAL)
def test_TC002(conftest):
    tc002 = simpleFormDemo(conftest)
    tc002.test_two_input_field()

@allure.title("TC003 - Input Form Validations")
@allure.severity(allure.severity_level.NORMAL)
def test_TC003(conftest):
    tc003 = inputFormSubmit(conftest)
    tc003.test_input_form_validations()