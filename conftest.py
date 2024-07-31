# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose language: es, ru, fr, etc.")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_argument(f"--lang={language}")
    
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    
    yield browser
    browser.quit()
