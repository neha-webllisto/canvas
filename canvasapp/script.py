from selenium import webdriver
import time
 
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
driver = webdriver.Chrome(chrome_options=options, executable_path="chromedriver")
driver.get('http://127.0.0.1:8001/demo')

# html = driver.page_source
# print(html)
btn = "//button[@id='submit']"
driver.find_element_by_xpath(btn).click()