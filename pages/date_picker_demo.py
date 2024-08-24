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
from datetime import datetime
import calendar
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

    def test_date_picker_by_send_keys(self, from_date, to_date):
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

    def test_date_picker_by_condition(self, from_date, to_date):
        if WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(((By.XPATH, '//h1[.="Selenium Playground"]')))).is_displayed():
            logging.info("Selenium Playground Heading is displayed")
            WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(((By.XPATH, '//a[.="JQuery Date Picker"]')))).click()
            logging.info("Clicked on [JQuery Date Picker] Link")
            WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(((By.XPATH, '//h1[.="JQuery Date Picker Demo"]')))).is_displayed()
            logging.info("Redirected to [JQuery Date Picker Demo] page")

        # FROM DATE
        self.driver.find_element(By.XPATH, '//input[@id="from"]').click()

        # formatted_date = datetime.strptime(from_date, "%Y-%m-%d %H:%M:%S")
        formatted_date = datetime.strptime(from_date, "%m/%d/%Y")
        expected_from_day = formatted_date.day
        expected_from_month = formatted_date.month
        expected_from_year = formatted_date.year

        formatted_from_date = formatted_date.strftime("%m/%d/%Y")

        from_month_str = calendar.month_abbr[expected_from_month]
        current_from_year_str = self.driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
        current_from_year_int = int(current_from_year_str)

        while current_from_year_int < expected_from_year:
            self.driver.find_element(By.XPATH, "//a[@title='Next']").click()
            current_from_year_str = self.driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
            current_from_year_int = int(current_from_year_str)

        while current_from_year_int > expected_from_year:
            self.driver.find_element(By.XPATH, "//a[@title='Prev']").click()
            current_from_year_str = self.driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
            current_from_year_int = int(current_from_year_str)

        logging.info("Selected Year: [%s]" %current_from_year_str)
        select_month = Select(self.driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
        select_month.select_by_visible_text(from_month_str)
        logging.info("Selected Month: [%s]" %from_month_str)
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//a[normalize-space()="'+str(expected_from_day)+'"]').click()
        logging.info("Selected Day: [%s]" %expected_from_day)

        # Validation / Assertion
        from_date_selected = self.driver.find_element(By.XPATH, "//input[@id='from']").get_attribute("value")
        logging.info("Expected date from testdata: [%s]" %formatted_from_date)
        logging.info("Captured date from UI: [%s]" %from_date_selected)
        if from_date_selected == formatted_from_date:
            logging.info("From date validation: [PASSED]")
            assert True
        else:
            logging.error("From date validation: [FAILED]")
            assert False
        allure.attach(self.driver.get_screenshot_as_png(), name="test_date_picker_from_condition", attachment_type=AttachmentType.PNG)
        time.sleep(5)

        # TO DATE
        self.driver.find_element(By.XPATH, "//input[@id='to']").click()

        # formatted_date = datetime.strptime(to_date, "%Y-%m-%d %H:%M:%S")
        formatted_date = datetime.strptime(to_date, "%m/%d/%Y")
        expected_to_day = formatted_date.day
        expected_to_month = formatted_date.month
        expected_to_year = formatted_date.year

        formatted_to_date = formatted_date.strftime("%m/%d/%Y")

        to_month_str = calendar.month_abbr[expected_to_month]
        current_to_year_str = self.driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
        current_to_year_int = int(current_to_year_str)

        while current_to_year_int < expected_to_year:
            self.driver.find_element(By.XPATH, "//a[@title='Next']").click()
            current_to_year_str = self.driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
            current_to_year_int = int(current_to_year_str)

        while current_to_year_int > expected_to_year:
            self.driver.find_element(By.XPATH, "//a[@title='Prev']").click()
            current_to_year_str = self.driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
            current_to_year_int = int(current_to_year_str)

        logging.info("Selected Year: [%s]" %current_to_year_str)
        select_month = Select(self.driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
        select_month.select_by_visible_text(to_month_str)
        logging.info("Selected Month: [%s]" %to_month_str)
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//a[normalize-space()="'+str(expected_to_day)+'"]').click()
        logging.info("Selected Day: [%s]" %expected_to_day)

        # Validation / Assertion
        to_date_selected = self.driver.find_element(By.XPATH, "//input[@id='to']").get_attribute("value")
        logging.info("Expected to date from testdata: [%s]" % formatted_to_date)
        logging.info("Captured to date from UI: [%s]" % to_date_selected)
        if to_date_selected == formatted_to_date:
            logging.info("To date validation: [PASSED]")
            assert True
        else:
            logging.error("To date validation: [FAILED]")
            assert False
        allure.attach(self.driver.get_screenshot_as_png(), name="test_date_picker_to_condition", attachment_type=AttachmentType.PNG)
        time.sleep(5)
