import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class Testtime(unittest.TestCase):

    def setUp(self):
       self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def Test_timesheet_Search_Employee_tanpa_data(self):
        
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(1)
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Time").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, ".//button[contains(@class, 'oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space')]").click()
        time.sleep(2) 
  
        assert self.driver.find_element(By.CSS_SELECTOR, ".oxd-input-field-error-message").text == "Required"
        time.sleep(5)
       
    def test_timesheet_Search_Employee(self):
        
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(1)
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Time").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, ".//div[contains(@class, 'oxd-autocomplete-text-input--before").send_keys("Odis  Adalwin")
        time.sleep(5)        
        # self.driver.find_element(By.XPATH, ".//button[contains(@class, 'oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space')]").click()
        # time.sleep(2) 
  
        # assert self.driver.find_element(By.CSS_SELECTOR, ".oxd-input-field-error-message").text == ""
        # time.sleep(5)
        
    def test_my_timesheet_submit_attandance_sukses(self):
        
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(1)
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(2)
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Time").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, ".//span[contains(@class, 'oxd-topbar-body-nav-tab-item')]").click()
        time.sleep(3)
        self.driver.find_elements(By.XPATH, ".//a[contains(@class, 'oxd-topbar-body-nav-tab-link')]")[0].click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, ".//button[contains(@class, 'oxd-button oxd-button--medium oxd-button--ghost')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, ".//button[contains(@class, 'oxd-button oxd-button--medium oxd-button--secondary')]").click()
        time.sleep(4)
        assert self.driver.find_element(By.XPATH, ".//div[contains(@class, 'orangehrm-timesheet-footer')]").text == ""
        time.sleep(5)
        
    def test_my_timesheet_myrecord_search(self):
        
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(1)
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(2)
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Time").click()
        time.sleep(3)
        self.driver.find_elements(By.XPATH, ".//span[contains(@class, 'oxd-topbar-body-nav-tab-item')]")[1].click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, ".//a[contains(@class, 'oxd-topbar-body-nav-tab-link')]").click()
        time.sleep(3)
        self.driver.find_elements(By.XPATH, ".//input[contains(@class, 'oxd-input oxd-input--active')]")[1].send_keys("2022-12-01")
        time.sleep(3)
        self.driver.find_element(By.XPATH, ".//div[contains(@class, 'oxd-form-actions')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, ".//button[contains(@class, 'oxd-button oxd-button--medium oxd-button--secondary')]").click()
        time.sleep(5)

        assert self.driver.find_element(By.XPATH, ".//div[contains(@class, 'orangehrm-timesheet-footer')]").text == ""
        time.sleep(5)
        
    def test_my_timesheet_myrecord_search(self):
        
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(1)
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(2)
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Time").click()
        time.sleep(3)
        self.driver.find_elements(By.XPATH, ".//span[contains(@class, 'oxd-topbar-body-nav-tab-item')]")[1].click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, ".//a[contains(@class, 'oxd-topbar-body-nav-tab-link')]").click()
        time.sleep(3)
        self.driver.find_elements(By.XPATH, ".//input[contains(@class, 'oxd-input oxd-input--active')]")[1].send_keys(Keys.CONTROL, 'a')
        time.sleep(3)
        self.driver.find_element(By.XPATH, ".//input[contains(@class, 'oxd-input oxd-input--focus')]").send_keys("2020-09-14")
        time.sleep(3)
        self.driver.find_element(By.XPATH, ".//div[contains(@class, 'oxd-form-actions')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, ".//button[contains(@class, 'oxd-button oxd-button--medium oxd-button--secondary')]").click()
        time.sleep(5)
        
        # assert self.driver.find_element(By.XPATH, ".//div[contains(@class, 'orangehrm-paper-container')]").text == ""
        # time.sleep(5)

    def test_my_timesheet_projectinfo_add_customer(self):
        
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(1)
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(2)
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Time").click()
        time.sleep(3)
        self.driver.find_elements(By.XPATH, ".//span[contains(@class, 'oxd-topbar-body-nav-tab-item')]")[3].click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, ".//a[contains(@class, 'oxd-topbar-body-nav-tab-link')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, ".//button[contains(@class, 'oxd-button oxd-button--medium oxd-button--secondary')]").click()
        time.sleep(3)
        self.driver.find_elements(By.XPATH, ".//input[contains(@class, 'oxd-input oxd-input--active')]")[1].send_keys("ini customer")
        time.sleep(3)
        self.driver.find_element(By.XPATH, ".//textarea[contains(@class, 'oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical')]").send_keys("ini comment")
        time.sleep(3)
        self.driver.find_element(By.XPATH, ".//button[contains(@class, 'oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space')]").click()
        time.sleep(5)

        assert self.driver.find_element(By.XPATH, ".//div[contains(@class, 'oxd-layout-footer')]").text == ""
        time.sleep(5)        
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':

    unittest.main()
