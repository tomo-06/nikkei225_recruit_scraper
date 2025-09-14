from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options

# Chromeのオプション設定
chrome_options = Options()
chrome_options.add_argument("--lang=ja")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--headless=new")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.socionext.com/jp/")
time.sleep(3)

soup = BeautifulSoup(driver.page_source, "html.parser")
for a in soup.find_all("a", href=True):
    print(a.get_text(strip=True), a["href"])

driver.quit()
