# Author: Prayogo Dewantoro
# Created Date: 2023-08-11
# Description: This script demonstrates the implementation of a Selenium playground using the Page Object Model (POM) design pattern.
# The script includes various test cases and configurations for web automation, along with generating Allure reports for better test visualization.


import allure
import pytest
import logging
from pages.simple_form_demo import simpleFormDemo
from pages.input_form_submit import inputFormSubmit
from pages.upload_file_demo import uploadFileDemo
from pages.drag_and_drop_sliders import dragAndDropSliders

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

@allure.title("TC004 - Upload File Demo")
@allure.severity(allure.severity_level.NORMAL)
def test_TC004(conftest):
    tc004 = uploadFileDemo(conftest)
    tc004.test_upload_file_demo()

@allure.title("TC005 - Drag and Drop Sliders Demo")
@allure.severity(allure.severity_level.NORMAL)
def test_TC005(conftest):
    tc005 = dragAndDropSliders(conftest)
    tc005.test_drag_and_drop_sliders_1()
    tc005.test_drag_and_drop_sliders_2()
    tc005.test_drag_and_drop_sliders_3()
    tc005.test_drag_and_drop_sliders_4()
    tc005.test_drag_and_drop_sliders_5()
    tc005.test_drag_and_drop_sliders_6()
    tc005.test_drag_and_drop_sliders_7()
    tc005.test_drag_and_drop_sliders_8()
