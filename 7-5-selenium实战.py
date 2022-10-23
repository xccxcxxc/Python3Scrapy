from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s:%(message)s')

INDEX_URL = 'https://spa2.scrape.center/page/{page}'
TIMEOUT = 10
TOTAL_PAGE = 10
RESULTS_DIR = 'results'

options = Options()
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ['enable-automation'])

browser = webdriver.Chrome(chrome_options=options)
wait = WebDriverWait(browser, TIMEOUT)
