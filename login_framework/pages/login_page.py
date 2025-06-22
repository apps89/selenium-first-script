from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, 'email')
        self.password_input = (By.ID, 'pass')
        self.login_button = (By.NAME, 'login')

    def load(self):
        self.driver.get("https://www.facebook.com/")

    def login(self, username, password):
        self.driver.find_element(*self.email_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()