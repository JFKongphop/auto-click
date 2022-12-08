from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# example by popcat to click
target = webdriver.Chrome(ChromeDriverManager().install())
target.get("https://popcat.click/")
target.set_window_size(100,600)
while True:
    # id of the element cat to click
    target.find_element("id", "app").click()
    time.sleep(0.5)
