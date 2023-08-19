# Author: Prayogo Dewantoro
# Created Date: 2023-08-11
# Description: This script demonstrates the implementation of a Selenium playground using the Page Object Model (POM) design pattern.
# The script includes various test cases and configurations for web automation, along with generating Allure reports for better test visualization.

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

picpath = '/Users/admin/PycharmProjects/selenium-playground/assets/pytest.png'

class uploadFileDemo:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def test_upload_file_demo(self):
        if WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(((By.XPATH, '//h1[.="Selenium Playground"]')))).is_displayed():
            logging.info("Selenium Playground Heading is displayed")
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH, '//a[.="Upload File Demo"]'))
            logging.info("Clicked on [Upload File Demo] link")
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(((By.XPATH, '//h1[.="Upload File Demo"]')))).is_displayed()
            logging.info("Redirected successfully to [Upload File Demo] page")
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//input[@id="file"]').send_keys(picpath)
            logging.info("Image is uploaded")
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(((By.XPATH, '//div[@id="error"]')))).is_displayed()
            success_msg = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(((By.XPATH, '//div[@id="error"]')))).text
            logging.info("Image uploaded successfully and success message captured from UI: [%s]" %success_msg)
            if success_msg == 'File Successfully Uploaded':
                allure.attach(self.driver.get_screenshot_as_png(), name="test_upload_file_PASS", attachment_type=AttachmentType.PNG)
                logging.info("Success message validation = [PASS]")
                assert True
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_upload_file_FAIL", attachment_type=AttachmentType.PNG)
                logging.info("Success message validation = [FAIL]")
                assert False
