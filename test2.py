from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
driver.maximize_window()

class DemoFindElementById():
    def locate_by_id_demo(self):
        driver.get("https://www.facebook.com/")
        driver.find_element(By.ID, 'email').send_keys('test@test.com')

findbyid =DemoFindElementById()
findbyid.locate_by_id_demo()


