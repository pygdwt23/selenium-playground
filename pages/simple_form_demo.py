import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
import time
import pytest
import logging
import os

LOGGER = logging.getLogger(__name__)

fake = Faker()

class simpleFormDemo:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def test_single_input_field(self):
        if WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(((By.XPATH, '//h1[.="Selenium Playground"]')))).is_displayed():
            logging.info("Selenium Playground Heading is displayed")
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(((By.XPATH, '//a[.="Simple Form Demo"]')))).click()
            logging.info("Clicked on Simple Form Demo Link")
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(((By.XPATH, '//h1[.="Simple Form Demo"]')))).is_displayed()
            logging.info("Redirected to Simple Form Demo Page")
            message = "Hello! " + fake.name() + ", Welcome to the LambdaTest Selenium Playground."
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(((By.XPATH, '//input[@id="user-message"]')))).send_keys(message)
            logging.info("Entered message [%s]" %message)
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(((By.XPATH, '//button[.="Get Checked Value"]')))).click()
            logging.info("Clicked on [Get Checked Value] button")
            actual_msg = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(((By.XPATH, '//p[@id="message"]')))).text
            logging.info("Actual message captured from UI: [%s]" %actual_msg)

            if message in actual_msg:
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="test_single_input_field_PASS", attachment_type=AttachmentType.PNG)
                logging.info("Message assertion [PASS]")
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_single_input_field_FAIL", attachment_type=AttachmentType.PNG)
                assert False
                logging.error("Message assertion [FAIL]")
            time.sleep(5)

    def test_two_input_field(self):
        if WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(((By.XPATH, '//h1[.="Selenium Playground"]')))).is_displayed():
            logging.info("Selenium Playground Heading is displayed")
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(((By.XPATH, '//a[.="Simple Form Demo"]')))).click()
            logging.info("Clicked on Simple Form Demo Link")
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(((By.XPATH, '//h1[.="Simple Form Demo"]')))).is_displayed()
            logging.info("Redirected to Simple Form Demo Page")
            val_one = fake.pyint()
            val_two = fake.pyint()
            total_sum = val_one + val_two
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(((By.XPATH, '//input[@id="sum1"]')))).send_keys(val_one)
            logging.info("Entered first value = [%s]" %val_one)
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(((By.XPATH, '//input[@id="sum2"]')))).send_keys(val_two)
            logging.info("Entered second value = [%s]" %val_two)
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(((By.XPATH, '//button[.="Get Sum"]')))).click()
            logging.info("Clicked on [Get Sum] button")
            logging.info("Expected total summary from code = [%s]" %total_sum)
            actual_sum = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(((By.XPATH, '//p[@id="addmessage"]')))).text
            logging.info("Actual summary captured from UI = [%s]" %actual_sum)
            if int(total_sum) == int(actual_sum):
                assert True
                allure.attach(self.driver.get_screenshot_as_png(), name="test_single_input_field_PASS", attachment_type=AttachmentType.PNG)
                logging.info("Total Summary validation [PASS]")
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_two_input_field_FAIL", attachment_type=AttachmentType.PNG)
                assert False
                logging.error("Total Summary validation [FAIL]")
            time.sleep(5)




