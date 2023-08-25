# Author: Prayogo Dewantoro
# Created Date: 2023-08-11
# Description: This script demonstrates the implementation of a Selenium playground using the Page Object Model (POM) design pattern.
# The script includes various test cases and configurations for web automation, along with generating Allure reports for better test visualization.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
import datetime
import allure
from allure_commons.types import AttachmentType
import time
import pytest
import logging
import os

LOGGER = logging.getLogger(__name__)

fake = Faker()

class datePickerDemo:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def test_date_picker(self, from_date, to_date):
        if WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(((By.XPATH, '//h1[.="Selenium Playground"]')))).is_displayed():
            logging.info("Selenium Playground Heading is displayed")
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(((By.XPATH, '//a[.="JQuery Date Picker"]')))).click()
            logging.info("Clicked on [JQuery Date Picker] Link")
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(((By.XPATH, '//h1[.="JQuery Date Picker Demo"]')))).is_displayed()
            logging.info("Redirected to [JQuery Date Picker Demo] page")
            self.driver.find_element(By.XPATH, '//input[@id="from"]').send_keys(from_date)
            self.driver.find_element(By.XPATH, '//input[@id="from"]').send_keys(Keys.RETURN)
            allure.attach(self.driver.get_screenshot_as_png(), name="test_date_picker_from", attachment_type=AttachmentType.PNG)
            logging.info("From date: %s" %from_date)
            self.driver.find_element(By.XPATH, '//input[@id="to"]').send_keys(to_date)
            self.driver.find_element(By.XPATH, '//input[@id="to"]').send_keys(Keys.RETURN)
            allure.attach(self.driver.get_screenshot_as_png(), name="test_date_picker_to", attachment_type=AttachmentType.PNG)
            logging.info("To date: %s" %to_date)
            time.sleep(3)
