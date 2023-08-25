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

class progressBarModal:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def test_progress_bar_modal(self):
        if WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(((By.XPATH, '//h1[.="Selenium Playground"]')))).is_displayed():
            logging.info("Selenium Playground Heading is displayed")
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(((By.XPATH, '//a[.="Progress Bar Modal"]')))).click()
            logging.info("Clicked on [Progress Bar Modal] Link")
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(((By.XPATH, '//h1[.="Bootstrap Progress Bar Dialog Demo"]')))).is_displayed()
            logging.info("Redirected to [Bootstrap Progress Bar Demo] page")
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(((By.XPATH, "//button[contains(text(),'Show dialog (Autoclose after 2 seconds)')]")))).click()
            logging.info("Clicked on [Show dialog Autoclose after 2 secs] button")
            dialog_1 = self.driver.find_element(By.XPATH, '//h3[contains(text(),\'Loading\')]').text
            logging.info("Captured dialog 1 message from UI: %s" %dialog_1)
            if dialog_1 == "Loading":
                allure.attach(self.driver.get_screenshot_as_png(), name="test_progress_bar_dialog1_PASS", attachment_type=AttachmentType.PNG)
                logging.info("Dialog 1 message validation [PASS]")
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_progress_bar_dialog1_FAIL", attachment_type=AttachmentType.PNG)
                logging.error("Dialog 1 message validation [FAIL]")
                assert False

            time.sleep(3)
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(((By.XPATH, "//button[contains(text(),'Show dialog (Autoclose after 3 seconds)')]")))).click()
            logging.info("Clicked on [Show dialog Autoclose after 3 secs] button")
            dialog_2 = self.driver.find_element(By.XPATH, '//div[@class="modal fade show"]//h3[contains(text(),\'Custom message\')]').text
            logging.info("Captured dialog 2 message from UI: %s" % dialog_2)
            if dialog_2 == "Custom message":
                allure.attach(self.driver.get_screenshot_as_png(), name="test_progress_bar_dialog2_PASS", attachment_type=AttachmentType.PNG)
                logging.info("Dialog 2 message validation [PASS]")
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_progress_bar_dialog2_PASS", attachment_type=AttachmentType.PNG)
                logging.error("Dialog 2 message validation [FAIL]")
                assert False

            time.sleep(5)
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(((By.XPATH, "//button[contains(text(),'Show dialog (Autoclose after 5 seconds)')]")))).click()
            logging.info("Clicked on [Show dialog Autoclose after 5 secs] button")
            dialog_3 = self.driver.find_element(By.XPATH, '//div[@class="modal fade show"]//h3[contains(text(),\'Hello Mr. Alert !\')]').text
            logging.info("Captured dialog 2 message from UI: %s" % dialog_3)
            if dialog_3 == "Hello Mr. Alert !":
                allure.attach(self.driver.get_screenshot_as_png(), name="test_progress_bar_dialog3_PASS", attachment_type=AttachmentType.PNG)
                logging.info("Dialog 3 message validation [PASS]")
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_progress_bar_dialog2_PASS", attachment_type=AttachmentType.PNG)
                logging.error("Dialog 3 message validation [FAIL]")
                assert False

