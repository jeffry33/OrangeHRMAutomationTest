import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class TestLeave(unittest.TestCase):

    def setUp(self):
       self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_apply_leave_tanpa_data(self):

        
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
        self.driver.find_element(By.XPATH, ".//a[contains(@class, 'oxd-topbar-body-nav-tab-item')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, ".//div[contains(@class, 'oxd-select-text-input')]").click()
        time.sleep(2)
        self.driver.find_elements(By.XPATH, ".//div[contains(@class, 'oxd-select-option')]")[1].click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, ".//button[contains(@class, 'oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space')]").click()
        time.sleep(2)

        assert self.driver.find_element(By.XPATH, ".//span[contains(@class, 'oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message')]").text == "Required"
        time.sleep(5)

    def test_apply_leave_tanpa_komen(self):


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
        self.driver.find_elements(By.XPATH, ".//a[contains(@class, 'oxd-topbar-body-nav-tab-item')]")[1].click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, ".//div[contains(@class, 'oxd-select-text-input')]").click()
        time.sleep(2)
        self.driver.find_elements(By.XPATH, ".//div[contains(@class, 'oxd-select-option')]")[1].click()
        time.sleep(2)
        container = self.driver.find_element(By.XPATH, ".//div[contains(@class, 'oxd-date-input')]")
        container.find_element(By.XPATH, ".//input[contains(@class, 'oxd-input oxd-input--active')]").send_keys("2022-12-01")
        time.sleep(2)
        self.driver.find_element(By.XPATH, ".//div[contains(@class, 'orangehrm-card-container')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, ".//button[contains(@class, 'oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space')]").click()
        time.sleep(2)

        assert self.driver.find_element(By.XPATH, ".//p[contains(@class, 'oxd-text oxd-text--p orangehrm-leave-balance-text')]").text == "13.00 Day(s)"
        time.sleep(5)      

    def test_apply_leave_sukses(self):


        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(2)
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Leave").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, ".//a[contains(@class, 'oxd-topbar-body-nav-tab-item')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, ".//div[contains(@class, 'oxd-select-text-input')]").click()
        time.sleep(2)
        self.driver.find_elements(By.XPATH, ".//div[contains(@class, 'oxd-select-option')]")[1].click()
        time.sleep(2)
        container = self.driver.find_element(By.XPATH, ".//div[contains(@class, 'oxd-date-input')]")
        container.find_element(By.XPATH, ".//input[contains(@class, 'oxd-input oxd-input--active')]").send_keys("2022-12-01")
        time.sleep(2)
        self.driver.find_element(By.XPATH, ".//div[contains(@class, 'orangehrm-card-container')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, ".//textarea[contains(@class, 'oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical')]").send_keys("comment")
        time.sleep(2)
        self.driver.find_element(By.XPATH, ".//button[contains(@class, 'oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space')]").click()
        time.sleep(2)

        assert self.driver.find_element(By.XPATH, ".//p[contains(@class, 'oxd-text oxd-text--p orangehrm-leave-balance-text')]").text == "13.00 Day(s)"
        time.sleep(5)            
    def test_my_leave_tanpa_data(self):

        
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
        self.driver.find_elements(By.XPATH, ".//a[contains(@class, 'oxd-topbar-body-nav-tab-item')]")[1].click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, ".//button[contains(@class, 'oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space')]").click()
        time.sleep(2)
        assert self.driver.find_element(By.XPATH, ".//button[contains(@class, 'oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space')]").text == "Search"
        time.sleep(5)

    def test_my_leave_add_comment(self):

        
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
        self.driver.find_elements(By.XPATH, ".//a[contains(@class, 'oxd-topbar-body-nav-tab-item')]")[1].click()
        time.sleep(3)
        self.driver.find_elements(By.XPATH, ".//i[contains(@class, 'oxd-icon bi-three-dots-vertical')]")[1].click()
        time.sleep(3)
        self.driver.find_elements(By.XPATH, ".//p[contains(@class, 'oxd-text oxd-text--p')]")[2].click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, ".//button[contains(@class, 'oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, ".//textarea[contains(@class, 'oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical')]").send_keys("ini comment")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-form-actions > .oxd-button--secondary").click()
        time.sleep(2)
        # assert self.driver.find_element(By.XPATH, ".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')]").text == "2022-12-29 - 2022-12-30"
        # time.sleep(5)

    def test_my_leave_view_detail_data(self):

        
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
        self.driver.find_elements(By.XPATH, ".//a[contains(@class, 'oxd-topbar-body-nav-tab-item')]")[1].click()
        time.sleep(3)
        self.driver.find_elements(By.XPATH, ".//i[contains(@class, 'oxd-icon bi-three-dots-vertical')]")[1].click()
        time.sleep(3)
        self.driver.find_elements(By.XPATH, ".//p[contains(@class, 'oxd-text oxd-text--p')]")[2].click()
        time.sleep(5)

        assert self.driver.find_element(By.XPATH, ".//div[contains(@class, 'oxd-table-cell oxd-padding-cell')]").text == "2022-12-29 - 2022-12-30"
        time.sleep(5)     

    def test_my_leave_view_detail_PIM(self):

        
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
        self.driver.find_elements(By.XPATH, ".//a[contains(@class, 'oxd-topbar-body-nav-tab-item')]")[1].click()
        time.sleep(3)
        self.driver.find_elements(By.XPATH, ".//i[contains(@class, 'oxd-icon bi-three-dots-vertical')]")[1].click()
        time.sleep(3)
        self.driver.find_elements(By.XPATH, ".//p[contains(@class, 'oxd-text oxd-text--p')]")[3].click()
        time.sleep(5)

        assert self.driver.find_element(By.XPATH, ".//p[contains(@class, 'oxd-text oxd-text--p orangehrm-leave-balance-text')]").text == "13.00 Day(s)"
        time.sleep(5) 
          
    def test_my_leave_add_entitlement_tanpa_data(self):

        
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
        self.driver.find_element(By.XPATH, ".//i[contains(@class, 'oxd-icon bi-chevron-down')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, ".//a[contains(@class, 'oxd-topbar-body-nav-tab-link')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, ".//button[contains(@class, 'oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space')]").click()
        time.sleep(3)
        assert self.driver.find_element(By.XPATH, ".//span[contains(@class, 'oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message')]").text == "Required"
        time.sleep(5)           

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()