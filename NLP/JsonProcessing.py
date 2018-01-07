import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import json

def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def populate_lists(url, text, ex_path, checker):
    # Some options...
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_experimental_option("detach", True)

    # Choose the browser (default is Firefox)
    driver = webdriver.Chrome(executable_path=ex_path, options=options)

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

with open('C:\\Users\\Maria\\Desktop\\teste.json', encoding="utf-8") as data_file:#de modificat path-ul pt cine vrea sa ruleze
    data = json.loads(data_file.read())
    for i in data:
        if i['q'] == "question1":  # aici trebuie luat din interfata!! hardcodat, momentan
            correct_answer = i['correct']

user_answer="Răspunsul utilizatorului" # aici trebuie luat din interfata!! hardcodat, momentan
#pt rulare, de modificat path-urile de mai jos
print("Rezultat din json:")
# printing a list of lists for WebPosRo-json
print("PosTagger:")
webpos_json = populate_lists(r"http://nlptools.info.uaic.ro/WebPosRo/", correct_answer, r"C:\Users\Maria\Desktop\chromedriver", 1)
print(webpos_json)

# printing a list of lists for WebNpChunkerRo-json
print("NpChunker:")
webchunk_json = populate_lists(r"http://nlptools.info.uaic.ro/WebNpChunkerRo/", correct_answer, r"C:\Users\Maria\Desktop\chromedriver", 0)
print(webchunk_json)
print("\n")
print("Rezultat utilizator:")
# printing a list of lists for WebPosRo-utilizator
print("PosTagger:")
webpos_user = populate_lists(r"http://nlptools.info.uaic.ro/WebPosRo/", user_answer, r"C:\Users\Maria\Desktop\chromedriver", 1)
print(webpos_user)

# printing a list of lists for WebNpChunkerRo-utilizator
print("NpChucker:")
webchunk_user = populate_lists(r"http://nlptools.info.uaic.ro/WebNpChunkerRo/", user_answer, r"C:\Users\Maria\Desktop\chromedriver", 0)
print(webchunk_user)

# the format is: word from text - lemma - POS