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

class inputFormSubmit:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def test_input_form_validations(self):
        if WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(((By.XPATH, '//h1[.="Selenium Playground"]')))).is_displayed():
            logging.info("Selenium Playground Heading is displayed")
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(((By.XPATH, '//a[.="Input Form Submit"]')))).click()
            logging.info("Clicked on [Input Form Submit] Link")
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(((By.XPATH, '//h1[.="Form Demo"]')))).is_displayed()
            logging.info("Redirected to Input Form Validations Page")
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']"))).click()
            logging.info("Clicked on [submit] button without inputs")
            errorMsg = self.driver.find_element(By.XPATH, "//input[@id='name']").get_attribute(name="validationMessage")
            time.sleep(5)
            if errorMsg in ["Fill out this field", "Please fill out this field.", "This is a required field"]:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_input_form_validation_negative_PASS", attachment_type=AttachmentType.PNG)
                assert True
                logging.info("Error message validation [PASS]")
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="test_input_form_validation_negative_FAIL", attachment_type=AttachmentType.PNG)
                assert False
                logging.error("Error message validation [FAIL]")

            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='name']"))).send_keys(fake.name())
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Email']"))).send_keys(fake.ascii_safe_email())
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))).send_keys("LambdaTest@2023")
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='company']"))).send_keys(fake.company())
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='websitename']"))).send_keys(fake.url())
            countrySelect = Select(self.driver.find_element(By.XPATH, "//select[@name='country']"))
            # countrySelect.select_by_value("ID")
            countryText = str(fake.country())
            countrySelect.select_by_visible_text(countryText)
            logging.info(f'Selected Country: {countryText}')
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inputCity']"))).send_keys(fake.city())
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Address 1']"))).send_keys(fake.address())
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Address 2']"))).send_keys(fake.address())
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inputState']"))).send_keys(fake.country())
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='inputZip']"))).send_keys(fake.postcode())
            time.sleep(5)
            allure.attach(self.driver.get_screenshot_as_png(), name="test_input_form_validation_positive_summary", attachment_type=AttachmentType.PNG)
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']"))).click()
            if WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//p[@class='success-msg hidden']"))).is_displayed():
                successMsg = self.driver.find_element(By.XPATH, "//p[@class='success-msg hidden']").text
                logging.info("Actual submission message captured from UI: [%s]" %successMsg)
                expectedSuccessMsg = "Thanks for contacting us, we will get back to you shortly."
                if expectedSuccessMsg == successMsg:
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_input_form_validation_positive_PASS", attachment_type=AttachmentType.PNG)
                    assert True
                    logging.info("Submission message validations [PASS]")
                else:
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_input_form_validation_positive_FAIL", attachment_type=AttachmentType.PNG)
                    assert False
                    logging.error("Submission message validations [FAIL]")
            time.sleep(5)
