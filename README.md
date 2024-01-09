Introduction
------------

This repository contains basic example of usage PageObject
pattern with Selenium and Python (PyTest + Selenium).
This repository contains a set of tests for the authorization page on the Rostelecom website
-----

[conftest.py](conftest.py) contains all the required code to catch failed test cases and make screenshot
of the page in case any test case will fail.

[pages/base.py](pages/base.py) contains PageObject pattern implementation for Python.

[pages/elements.py](pages/elements.py) contains helper class to define web elements on web pages.

[tests/test_pozitive.py](tests/test_pozitive.py) contains 11 positive tests for Rostelecom (https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution=46e66c9f-3355-48c4-ba6d-72b0d29add60&client_id=lk_b2c&tab_id=zp2DbybzlYM)

[tests/test_negative.py](tests/test_negative.py.py) contains 9 negative tests for Rostelecom (https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution=46e66c9f-3355-48c4-ba6d-72b0d29add60&client_id=lk_b2c&tab_id=zp2DbybzlYM)

How To Run Tests
----------------

1) Install all requirements:

    ```bash
    pip3 install -r requirements
    ```

2) Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

3) Run tests:

    ```bash
    python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
    ```

