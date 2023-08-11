import pytest
import logging
from pages.simple_form_demo import simpleFormDemo

logging.basicConfig(level=logging.DEBUG)


def test_TC001(conftest):
    tc001 = simpleFormDemo(conftest)
    tc001.test_single_input_field()

def test_TC002(conftest):
    tc002 = simpleFormDemo(conftest)
    tc002.test_two_input_field()