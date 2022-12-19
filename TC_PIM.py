import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import TC_Login

class TestAdmin(unittest.TestCase):
    LoginPage = TC_Login.TestLogin()

    def setUp(self):
       self.driver = webdriver.Edge()
       self.LoginPage.driver = self.driver

    def test_a_Daftar_Employee_dan_Akun(self):
       self.LoginPage.test_e_success_Login()
       driver = self.driver

       self.driver.find_element(By.LINK_TEXT, "PIM").click()
       time.sleep(2)
       self.driver.find_element(By.LINK_TEXT, "Admin").click()
       time.sleep(2)
       self.driver.find_element(By.LINK_TEXT, "PIM").click()
       time.sleep(2)
       
       self.driver.find_element(By.CSS_SELECTOR, ".bi-plus").click()
       time.sleep(2)
       self.driver.find_element(By.NAME,"firstName").send_keys("Dion")
       time.sleep(2)
       self.driver.find_element(By.NAME,"middleName").send_keys("Rioko")
       time.sleep(1)
       self.driver.find_element(By.NAME,"lastName").send_keys("Arifin")
       time.sleep(1)
       self.driver.find_element(By.CSS_SELECTOR, ".oxd-switch-input").click()
       time.sleep(1)
       
       self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input").send_keys("dion_rioko")
       time.sleep(1)

       self.driver.find_element(By.CSS_SELECTOR, ".oxd-input-group:nth-child(2) label").click()
       time.sleep(1)
       self.driver.find_element(By.CSS_SELECTOR, ".oxd-input-group:nth-child(1) label").click()
       time.sleep(1)
       self.driver.find_element(By.CSS_SELECTOR, ".oxd-input-group:nth-child(2) label").click()
       time.sleep(1)

       self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input").send_keys("@Dionrioko123")
       time.sleep(1)
       self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input").send_keys("@Dionrioko123")
       time.sleep(1)
       self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
       time.sleep(2)

       self.driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-icon").click() 
       time.sleep(1)
       self.driver.find_element(By.LINK_TEXT, "Logout").click()
       time.sleep(1)

    def test_b_Daftar_Employee_Tanpa_Akun(self):
       self.LoginPage.test_e_success_Login()
       driver = self.driver

       self.driver.find_element(By.LINK_TEXT, "PIM").click()
       time.sleep(2)
       self.driver.find_element(By.LINK_TEXT, "Admin").click()
       time.sleep(2)
       self.driver.find_element(By.LINK_TEXT, "PIM").click()
       time.sleep(2)
       
       self.driver.find_element(By.CSS_SELECTOR, ".bi-plus").click()
       time.sleep(2)
       self.driver.find_element(By.NAME,"firstName").send_keys("Damara")
       time.sleep(2)
       self.driver.find_element(By.NAME,"middleName").send_keys("Jika")
       time.sleep(1)
       self.driver.find_element(By.NAME,"lastName").send_keys("Arifin")
       time.sleep(1)
       self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
       time.sleep(2)

       self.driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-icon").click() 
       time.sleep(2)
       self.driver.find_element(By.LINK_TEXT, "Logout").click()
       time.sleep(2)

    def test_c_Daftar_Employee_Tanpa_Input_Firstname(self):
       self.LoginPage.test_e_success_Login()
       driver = self.driver

       self.driver.find_element(By.LINK_TEXT, "PIM").click()
       time.sleep(2)
       self.driver.find_element(By.LINK_TEXT, "Admin").click()
       time.sleep(2)
       self.driver.find_element(By.LINK_TEXT, "PIM").click()
       time.sleep(2)
       
       self.driver.find_element(By.CSS_SELECTOR, ".bi-plus").click()
       time.sleep(2)
       self.driver.find_element(By.NAME,"firstName").send_keys("")
       time.sleep(2)
       self.driver.find_element(By.NAME,"middleName").send_keys("Kole")
       time.sleep(1)
       self.driver.find_element(By.NAME,"lastName").send_keys("Bagas")
       time.sleep(1)
       self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
       time.sleep(2)

       assert self.driver.find_element(By.CSS_SELECTOR, ".oxd-text--span").text == "Required"
       time.sleep(1)

       self.driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-icon").click() 
       time.sleep(1)
       self.driver.find_element(By.LINK_TEXT, "Logout").click()
       time.sleep(1)

    def test_d_Daftar_Employee_Tanpa_Input_Lastname(self):
       self.LoginPage.test_e_success_Login()
       driver = self.driver

       self.driver.find_element(By.LINK_TEXT, "PIM").click()
       time.sleep(2)
       self.driver.find_element(By.LINK_TEXT, "Admin").click()
       time.sleep(2)
       self.driver.find_element(By.LINK_TEXT, "PIM").click()
       time.sleep(2)
       
       self.driver.find_element(By.CSS_SELECTOR, ".bi-plus").click()
       time.sleep(2)
       self.driver.find_element(By.NAME,"firstName").send_keys("")
       time.sleep(2)
       self.driver.find_element(By.NAME,"middleName").send_keys("Kole")
       time.sleep(1)
       self.driver.find_element(By.NAME,"lastName").send_keys("")
       time.sleep(1)
       self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
       time.sleep(2)

       assert self.driver.find_element(By.CSS_SELECTOR, ".oxd-text--span").text == "Required"
       time.sleep(1)

       self.driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-icon").click() 
       time.sleep(1)
       self.driver.find_element(By.LINK_TEXT, "Logout").click()
       time.sleep(1)

    def test_e_Membatalkan_Daftar_Employee(self):
       self.LoginPage.test_e_success_Login()
       driver = self.driver

       self.driver.find_element(By.LINK_TEXT, "PIM").click()
       time.sleep(2)
       self.driver.find_element(By.LINK_TEXT, "Admin").click()
       time.sleep(2)
       self.driver.find_element(By.LINK_TEXT, "PIM").click()
       time.sleep(2)
       
       self.driver.find_element(By.CSS_SELECTOR, ".bi-plus").click()
       time.sleep(2)
       self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[1]").click()
       time.sleep(2)

       self.driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-icon").click() 
       time.sleep(1)
       self.driver.find_element(By.LINK_TEXT, "Logout").click()
       time.sleep(1)
    #    assert self.driver.find_element(By.CSS_SELECTOR, ".oxd-text--span").text == "Required"
    #    time.sleep(1)

    #    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").click()
    #    self.driver.find_element(By.XPATH, "//*[@id=\'app\']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input").send_keys("Rioko")
    #    time.sleep(1)
    #    self.driver.find_element(By.XPATH, "//*[@id=\'app\']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input").send_keys("Rioko")
    #    time.sleep(1)
    #    self.driver.find_element(By.XPATH, "//*[@id=\'app\']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input").send_keys("Riosko")
    #    time.sleep(1)

       
      #  self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").send_keys("tiararahayu")
      # #  self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").send_keys("Arifin Syarif")
      # #  self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input")
      # #  self.driver.find_element(By.NAME,"password").send_keys("admin123")
      # # 13 | click | css=.oxd-input--focus | 
      #  self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").click()
      # # 14 | type | css=.oxd-input--focus | tiararahayu
      #  self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").send_keys("tiararahayu")
      # # 15 | click | css=.oxd-input-group:nth-child(2) .oxd-radio-input | 
      #  self.driver.find_element(By.CSS_SELECTOR, ".oxd-input-group:nth-child(2) .oxd-radio-input").click()
      # # 16 | click | css=.oxd-input-group:nth-child(1) > div > .oxd-radio-wrapper .oxd-radio-input | 
      #  self.driver.find_element(By.CSS_SELECTOR, ".oxd-input-group:nth-child(1) > div > .oxd-radio-wrapper .oxd-radio-input").click()
      #  time.sleep(2)
      # # 17 | click | css=.oxd-input--focus | 
      #  self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").click()
      #  time.sleep(2)
      # # 18 | type | css=.oxd-input--focus | @Tiara123
      #  self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").send_keys("@Tiara123")
      #  time.sleep(2)
      # # 19 | click | css=.oxd-input--focus | 
      #  self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").click()
      #  time.sleep(2)
      # # 20 | type | css=.oxd-input--focus | @Tiara123
      #  self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").send_keys("@Tiara123")
      #  time.sleep(2)
      # # 21 | click | css=.oxd-button--secondary | 
      #  self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--secondary").click()
      #  time.sleep(2)
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
