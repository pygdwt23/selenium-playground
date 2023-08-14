
# Selenium Playground

Welcome to the **Selenium Playground** repository! This repository serves as a collection of demo projects utilizing LambdaTest and Selenium for automated testing. Explore and experiment with Selenium to enhance your testing practices.

## Installation

Before you get started, ensure you have the necessary packages installed. You can install them using the following command:

```bash
pip install selenium pytest openpyxl allure-pytest webdriver-manager bs4 geckodriver-autoinstaller json5 nltk xlrd pandas pypdf2 urlextract pyodbc excelreader
```

## How to Run Tests

You can run the tests using the following command:

```bash
pytest -v -s [test_file_name]
```

Replace `[test_file_name]` with the name of the test file you want to execute.

## Generating Allure Reports

If you're interested in generating Allure reports for your test runs, follow these steps:

1. Run tests with Allure integration:

```bash
pytest -v -s --alluredir="[allure_directory]" [test_file_name]
```

Replace `[allure_directory]` with the path where you want to store the Allure report artifacts, and `[test_file_name]` with the name of the test file.

2. Viewing Allure Reports:

To view the generated Allure report, follow these steps:

- Open a command prompt or terminal.
- Navigate to the directory where you executed the tests.
- Run the following command:

```bash
allureserve [allure_directory]
```

Replace `[allure_directory]` with the path to the directory containing the Allure report artifacts. This command will launch a local web server and automatically open the Allure report in your default web browser.

Feel free to explore the various features and insights provided by the Allure report to gain a better understanding of your test results.

Happy testing with Selenium in the