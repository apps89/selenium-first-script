import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.base import get_driver
from pages.login_page import LoginPage

def main():
    driver = get_driver()
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("test@test.com", "invalidpassword")
    input("\nPress Enter to close the browser...")
    driver.quit()

if __name__ == "__main__":
    main()
