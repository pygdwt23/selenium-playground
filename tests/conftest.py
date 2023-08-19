# Author: Prayogo Dewantoro
# Created Date: 2023-08-11
# Description: This script demonstrates the implementation of a Selenium playground using the Page Object Model (POM) design pattern.
# The script includes various test cases and configurations for web automation, along with generating Allure reports for better test visualization.

import logging
import pytest
import os
import sys
import json
import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.ie.options import Options

CONFIG_PATH = '/Users/admin/PycharmProjects/selenium-playground/config.json'
baseurl = "https://www.lambdatest.com/selenium-playground/"

@pytest.fixture(scope='session')
def config():
    # open the config file and read json data to return it as dict
    with open(CONFIG_PATH) as config_file:
        if os.path.isfile(CONFIG_PATH):
            data = json.load(config_file)
            return data
        else:
            raise Exception('File does not exists in the path')

@pytest.fixture(scope='session')
def browser(config):
    return config['browser']

@pytest.fixture()
def conftest(browser):
    if browser in ['Chrome', 'chrome']:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('start-maximized')
        # chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--test-type')
        chrome_options.add_argument('--ignore-ssl-errors=yes')
        chropath = '/Users/admin/Downloads/chrome-mac-x64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing'
        chrome_options.binary_location = chropath
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        service= Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        # driver = webdriver.Chrome(options=chrome_options)
    elif browser in ['IE', 'edge', 'Edge']:
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument('--incognito')
        edge_options.add_argument('start-maximized')
        # chrome_options.add_argument('--ignore-certificate-errors')
        edge_options.add_argument('--test-type')
        edge_options.add_argument('--ignore-ssl-errors=yes')
        edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        edge_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        service= Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=edge_options)

    driver.delete_all_cookies()
    print('Run started at:' +str(datetime.datetime.today()))
    logging.info("Base URL: %s" %baseurl)
    driver.implicitly_wait(10)
    driver.get(baseurl)

    yield driver
    driver.quit()
