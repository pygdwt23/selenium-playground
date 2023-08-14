# Selenium Playground

Welcome to the **selenium-playground** repository! This repository contains a collection of demo projects that showcase how to use Selenium with the Page Object Model (POM) design pattern. These demos are designed to help you get started with using Selenium for web automation in conjunction with various libraries and tools.

## Installation

To use the demo projects in this repository, you'll need to install some packages. You can install them using `pip` with the following command:

```bash
pip install selenium pytest openpyxl allure-pytest webdriver-manager bs4 geckodriver-autoinstaller json5 nltk xlrd pandas pypdf2 urlextract pyodbc excelreader
```

## How to Run Tests

You can run the tests using the `pytest` command followed by the specific test file name. Here's an example:

```bash
pytest -v -s [test_file_name]
```

Replace `[test_file_name]` with the actual name of the test file you want to run.

## Generating Allure Reports

If you'd like to generate Allure reports for your test runs, you can do so by using the following command:

```bash
pytest -v -s --alluredir="[allure_directory]" [test_file_name]
```

Replace `[allure_directory]` with the path where you want to store the generated Allure report and `[test_file_name]` with the name of the test file you want to run.

## Viewing Allure Reports

To view the generated Allure report, follow these steps:

1. Open your command prompt or terminal.
2. Navigate to the directory where your project is located.
3. Run the following command:

```bash
allureserve [allure_directory]
```

Replace `[allure_directory]` with the path to the directory where you generated the Allure report. This command will start a web server that allows you to interactively explore and analyze the test execution results.

Feel free to explore the demo projects and learn how to use Selenium effectively with the POM design pattern. Happy testing!