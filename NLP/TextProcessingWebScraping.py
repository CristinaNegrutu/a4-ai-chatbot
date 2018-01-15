import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import os

PHANTOMJS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'phantomjs.exe')


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def populate_lists(url, text, checker):
    # Some options...
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_experimental_option("detach", True)

    # Choose the browser (default is Firefox)
    driver = webdriver.PhantomJS(executable_path=PHANTOMJS_PATH)

    # Fill in the url
    driver.get(url)

    # Clear default text and fill in what you want
    elem = driver.find_element_by_id("sentText")
    elem.clear()
    elem.send_keys(text)

    # Click button
    driver.find_element_by_id('tagBtn').click()
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, "lxml")

    if checker:
        attr = 'div'
    else:
        attr = 'span'

    rows = len(soup.find_all(attr, attrs={'class': 'pretty_word'}))
    columns = 3
    matrix = [[0 for x in range(columns)] for y in range(rows)]
    i = 0

    for word in soup.find_all(attr, attrs={'class': 'pretty_word'}):
        matrix[i][0] = word.get_text()
        matrix[i][1] = find_between(str(word), r'LEMMA:"', r'"')
        matrix[i][2] = find_between(str(word), r'POS:"', r'"')
        i = i + 1

    return matrix


# # printing a list of lists for WebPosRo
webpos = populate_lists(r"http://nlptools.info.uaic.ro/WebPosRo/", r"Textul nr. 1 pentru WebPosRo.", 1)
print(webpos)
#
# # printing a list of lists for WebNpChunkerRo
webchunk = populate_lists(r"http://nlptools.info.uaic.ro/WebNpChunkerRo/", r"Înserare text numărul doi.", 0)
print(webchunk)
#
# # the format is: word from text - lemma - POS
