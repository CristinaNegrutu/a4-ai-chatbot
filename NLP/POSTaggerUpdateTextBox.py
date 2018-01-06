import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options

# Some options...
options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

# Choose the browser (default is Firefox)
driver = webdriver.Chrome(executable_path='C:\\Users\\Reflex\\Desktop\\chromedriver', options=options)


# Fill in the url
driver.get("http://nlptools.info.uaic.ro/WebPosRo/")

# Clear default text and fill in what you want
elem = driver.find_element_by_id("sentText")
elem.clear()
elem.send_keys("Bine ati venit dragilor!")

# Click button
driver.find_element_by_id('tagBtn').click()
