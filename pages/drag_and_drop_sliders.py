# Author: Prayogo Dewantoro
# Created Date: 2023-08-11
# Description: This script demonstrates the implementation of a Selenium playground using the Page Object Model (POM) design pattern.
# The script includes various test cases and configurations for web automation, along with generating Allure reports for better test visualization.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
import allure
from allure_commons.types import AttachmentType
import time
import pytest
import logging
import os

LOGGER = logging.getLogger(__name__)

fake = Faker()

class dragAndDropSliders:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def test_drag_and_drop_sliders_1(self):
        if WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(((By.XPATH, '//h1[.="Selenium Playground"]')))).is_displayed():
            logging.info("Selenium Playground Heading is displayed")
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(((By.XPATH, '//a[.="Drag & Drop Sliders"]')))).click()
            logging.info("Clicked on [Drag and Drop Sliders] Link")
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(((By.XPATH, '//h1[.="Slider Demo"]')))).is_displayed()
            logging.info("Redirected to [Slider Demo] page")
            default_value = self.driver.find_element(By.XPATH, '//output[@id="range"]').text
            logging.info("Default value of slider1 before drag and drop = %s" %default_value)
            slider1 = self.driver.find_element(By.XPATH, '//input[@value="5"]')
            x_offset1 = 95
            self.action.drag_and_drop_by_offset(slider1, x_offset1, 0).perform()
            logging.info("Drag and drop by X offset value: %s" %x_offset1)
            time.sleep(5)
            after_value = self.driver.find_element(By.XPATH, '//output[@id="range"]').text
            logging.info("Slider1 value after drag and drop = %s" %after_value)
            if after_value != default_value:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_drag_and_drop_sliders_1_PASS", attachment_type=AttachmentType.PNG)
                logging.info("Slider1 drag and drop [PASS]")
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_drag_and_drop_sliders_1_FAIL", attachment_type=AttachmentType.PNG)
                logging.error("Slider1 drag and drop [FAIL]")
                assert False

    def test_drag_and_drop_sliders_2(self):
        default_value = self.driver.find_element(By.XPATH, '//output[@id="rangePrimary"]').text
        logging.info("Default value of slider2 before drag and drop = %s" % default_value)
        slider2 = self.driver.find_element(By.XPATH, '//input[@value="20"]')
        x_offset2 = -200
        self.action.drag_and_drop_by_offset(slider2, x_offset2, 0).perform()
        logging.info("Drag and drop by X offset value: %s" % x_offset2)
        time.sleep(5)
        after_value = self.driver.find_element(By.XPATH, '//output[@id="rangePrimary"]').text
        logging.info("Slider2 value after drag and drop = %s" % after_value)
        if after_value != default_value:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_drag_and_drop_sliders_2_PASS", attachment_type=AttachmentType.PNG)
            logging.info("Slider2 drag and drop [PASS]")
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_drag_and_drop_sliders_2_FAIL", attachment_type=AttachmentType.PNG)
            logging.error("Slider2 drag and drop [FAIL]")
            assert False

    def test_drag_and_drop_sliders_3(self):
        default_value = self.driver.find_element(By.XPATH, '//output[@id="rangeSuccess"]').text
        logging.info("Default value of slider3 before drag and drop = %s" % default_value)
        slider3 = self.driver.find_element(By.XPATH, '//input[@value="15"]')
        x_offset3 = 190
        self.action.drag_and_drop_by_offset(slider3, x_offset3, 0).perform()
        logging.info("Drag and drop by X offset value: %s" % x_offset3)
        time.sleep(5)
        after_value = self.driver.find_element(By.XPATH, '//output[@id="rangeSuccess"]').text
        logging.info("Slider3 value after drag and drop = %s" % after_value)
        if after_value != default_value:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_drag_and_drop_sliders_3_PASS", attachment_type=AttachmentType.PNG)
            logging.info("Slider3 drag and drop [PASS]")
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_drag_and_drop_sliders_3_FAIL", attachment_type=AttachmentType.PNG)
            logging.error("Slider3 drag and drop [FAIL]")
            assert False

    def test_drag_and_drop_sliders_4(self):
        default_value = self.driver.find_element(By.XPATH, '//output[@id="rangeInfo"]').text
        logging.info("Default value of slider4 before drag and drop = %s" % default_value)
        slider4 = self.driver.find_element(By.XPATH, '//input[@value="50"]')
        x_offset4 = -150
        self.action.drag_and_drop_by_offset(slider4, x_offset4, 0).perform()
        logging.info("Drag and drop by X offset value: %s" % x_offset4)
        time.sleep(5)
        after_value = self.driver.find_element(By.XPATH, '//output[@id="rangeInfo"]').text
        logging.info("Slider4 value after drag and drop = %s" % after_value)
        if after_value != default_value:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_drag_and_drop_sliders_4_PASS", attachment_type=AttachmentType.PNG)
            logging.info("Slider4 drag and drop [PASS]")
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_drag_and_drop_sliders_4_FAIL", attachment_type=AttachmentType.PNG)
            logging.error("Slider4 drag and drop [FAIL]")
            assert False

    def test_drag_and_drop_sliders_5(self):
        default_value = self.driver.find_element(By.XPATH, '//output[@id="rangeWarning"]').text
        logging.info("Default value of slider5 before drag and drop = %s" % default_value)
        slider5 = self.driver.find_element(By.XPATH, '//input[@value="25"]')
        x_offset5 = 175
        self.action.drag_and_drop_by_offset(slider5, x_offset5, 0).perform()
        logging.info("Drag and drop by X offset value: %s" % x_offset5)
        time.sleep(5)
        after_value = self.driver.find_element(By.XPATH, '//output[@id="rangeWarning"]').text
        logging.info("Slider5 value after drag and drop = %s" % after_value)
        if after_value != default_value:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_drag_and_drop_sliders_5_PASS", attachment_type=AttachmentType.PNG)
            logging.info("Slider5 drag and drop [PASS]")
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_drag_and_drop_sliders_5_FAIL", attachment_type=AttachmentType.PNG)
            logging.error("Slider5 drag and drop [FAIL]")
            assert False

    def test_drag_and_drop_sliders_6(self):
        default_value = self.driver.find_element(By.XPATH, '//output[@id="rangeDanger"]').text
        logging.info("Default value of slider6 before drag and drop = %s" % default_value)
        slider6 = self.driver.find_element(By.XPATH, '//input[@value="30"]')
        x_offset6 = -125
        self.action.drag_and_drop_by_offset(slider6, x_offset6, 0).perform()
        logging.info("Drag and drop by X offset value: %s" % x_offset6)
        time.sleep(5)
        after_value = self.driver.find_element(By.XPATH, '//output[@id="rangeDanger"]').text
        logging.info("Slider6 value after drag and drop = %s" % after_value)
        if after_value != default_value:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_drag_and_drop_sliders_6_PASS", attachment_type=AttachmentType.PNG)
            logging.info("Slider6 drag and drop [PASS]")
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_drag_and_drop_sliders_6_FAIL", attachment_type=AttachmentType.PNG)
            logging.error("Slider6 drag and drop [FAIL]")
            assert False

    def test_drag_and_drop_sliders_7(self):
        default_value = self.driver.find_element(By.XPATH, '//div[@id="slider7"]//output[@id="rangeWarning"]').text
        logging.info("Default value of slider7 before drag and drop = %s" % default_value)
        slider7 = self.driver.find_element(By.XPATH, '//input[@value="40"]')
        x_offset7 = 80
        self.action.drag_and_drop_by_offset(slider7, x_offset7, 0).perform()
        logging.info("Drag and drop by X offset value: %s" % x_offset7)
        time.sleep(5)
        after_value = self.driver.find_element(By.XPATH, '//div[@id="slider7"]//output[@id="rangeWarning"]').text
        logging.info("Slider7 value after drag and drop = %s" % after_value)
        if after_value != default_value:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_drag_and_drop_sliders_7_PASS", attachment_type=AttachmentType.PNG)
            logging.info("Slider7 drag and drop [PASS]")
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_drag_and_drop_sliders_7_FAIL", attachment_type=AttachmentType.PNG)
            logging.error("Slider7 drag and drop [FAIL]")
            assert False

    def test_drag_and_drop_sliders_8(self):
        default_value = self.driver.find_element(By.XPATH, '//div[@id="slider8"]//output[@id="rangeDanger"]').text
        logging.info("Default value of slider8 before drag and drop = %s" % default_value)
        slider8 = self.driver.find_element(By.XPATH, '//input[@value="80"]')
        x_offset8 = -225
        self.action.drag_and_drop_by_offset(slider8, x_offset8, 0).perform()
        logging.info("Drag and drop by X offset value: %s" % x_offset8)
        time.sleep(5)
        after_value = self.driver.find_element(By.XPATH, '//div[@id="slider8"]//output[@id="rangeDanger"]').text
        logging.info("Slider8 value after drag and drop = %s" % after_value)
        if after_value != default_value:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_drag_and_drop_sliders_8_PASS", attachment_type=AttachmentType.PNG)
            logging.info("Slider8 drag and drop [PASS]")
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_drag_and_drop_sliders_8_FAIL", attachment_type=AttachmentType.PNG)
            logging.error("Slider8 drag and drop [FAIL]")
            assert False