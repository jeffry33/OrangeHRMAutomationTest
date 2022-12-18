import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
       self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_failed_Login_Tanpa_Password(self):

        # Login
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(1)
        self.driver.find_element(By.NAME,"password").send_keys("")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        time.sleep(5)

        assert self.driver.find_element(By.CSS_SELECTOR, ".oxd-text--span").text == "Required"
        time.sleep(5)
    
    def test_b_failed_Login_Tanpa_Username(self):

        # Login
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        self.driver.find_element(By.NAME,"username").send_keys("")
        time.sleep(1)
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        time.sleep(5)

        assert self.driver.find_element(By.CSS_SELECTOR, ".oxd-text--span").text == "Required"
        time.sleep(5)
        
    def test_c_failed_Login_Salah_Username(self):

        # Login
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        self.driver.find_element(By.NAME,"username").send_keys("Toni")
        time.sleep(1)
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        time.sleep(5)

        assert self.driver.find_element(By.CSS_SELECTOR, ".oxd-text--p").text == "Invalid"
        time.sleep(5)
        
    def test_d_failed_Login_Salah_Password(self):

        # Login
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(1)
        self.driver.find_element(By.NAME,"password").send_keys("Rudi123")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        time.sleep(5)

        assert self.driver.find_element(By.CSS_SELECTOR, ".oxd-text--p").text == "Invalid"
        time.sleep(5)
        
    def test_e_success_Login(self):

        # Login
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(1)
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        time.sleep(10)
        
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
