import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class TestLogin(unittest.TestCase):

    def setUp(self):
       self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_apply_leave_tanpa_data(self):

        # Login
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(1)
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Leave").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab:nth-child(1)").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        time.sleep(2)
        
        assert self.driver.find_element(By.CSS_SELECTOR, ".oxd-grid-2 .oxd-input-group > .oxd-text").text == "Required"
        time.sleep(5)
       
    def test_apply_leave_tanpa_setting_date(self):

        # Login
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(1)
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Leave").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab:nth-child(1)").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-select-text-input").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-grid-item:nth-child(1) .oxd-input").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        time.sleep(2)        
        assert self.driver.find_element(By.CSS_SELECTOR, ".oxd-grid-2 .oxd-input-group > .oxd-text").text == "Required"
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()