from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


options = Options()
#options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
