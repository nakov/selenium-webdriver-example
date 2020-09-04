# Selenium WebDriver - Example with GitHub Actions
![selenium-tests](https://github.com/nakov/selenium-webdriver-example/workflows/selenium-tests/badge.svg)

Example of using Selenium WebDriver to automate Chrome Web browser from Python.
Selenium tests are automatically executed when the code is changed.
Testing is implemented as GitHub workflow, using GitHub Actions.

## Running the Example

This app is based on "**poetry**" package manager for Python.

First, install `poetry`.

Then run the following commands:

```
poetry install
```

```
poetry run python main.py
```

Try to comment uncomment the following lines, if Chrome fails to start:
```
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
```

## Source Code
https://github.com/nakov/selenium-webdriver-example

## Automated Build in GitHub Actions
https://github.com/nakov/selenium-webdriver-example/actions

## Live Example at Repl.it
https://repl.it/@nakov/selenium-webdriver-example
