from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

target = webdriver.Chrome(ChromeDriverManager().install())

# put website in ""
target.get("")
target.set_window_size(100,600)
while True:
    # put id of the element in ""
    target.find_element("id", "").click()
    time.sleep(0.5)