import logging
import json

from os import makedirs
from os.path import exists

from pyppeteer import launch
from pyppeteer.errors import TimeoutError

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s:%(message)s')

RESULT_DIR = 'results'

exists(RESULT_DIR) or makedirs(RESULT_DIR)

INDEX_URL = 'https://spa2.scrape.center/page/{page}'
TIMEOUT = 10
TOTAL_PAGE = 10
WINDOW_WIDTH, WINDOW_HEIGHT = 1366, 768
HEADLESS = False
RESULTS_DIR = 'results'

browser, tab = None, None


async def init():
    global browser, tab
    browser = await launch(headless=HEADLESS,
                           args=['--disable-infobars',
                                 f'--window-size={WINDOW_WIDTH}, {WINDOW_HEIGHT}'])
    tab = await browser.newPage()
    await tab.setViewport({'width': WINDOW_WIDTH, 'height': WINDOW_HEIGHT})


async def scrape_page(url, selector):
    logging.info('scraping %s', url)
    try:
        await tab.goto(url)
        await tab.waitForSelector(selector, options={'timeout': TIMEOUT * 1000})
    except TimeoutError:
        logging.error('error occured while scraping %s', url, exc_info=True)
