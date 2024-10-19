from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.google.com")

search_box = driver.find_element("name", "q")
search_box.send_keys("Automated scripting with Python")
search_box.send_keys(Keys.RETURN)

driver.implicitly_wait(5) 
driver.quit()  
