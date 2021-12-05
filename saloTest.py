import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, executable_path=r'C:/Users/admin/Desktop/chromedriver.exe')
URL = 'https://profile.w3schools.com/log-in'
driver.get(URL);
driver.maximize_window()

email = driver.find_element(By.NAME, "email")
password = driver.find_element(By.NAME, "current-password")
elem = driver.find_element(By.NAME, "current-password")

class TestLogin(unittest.TestCase):

	def test_01_succesful(self):
		email.send_keys("vovgank@mail.ru")
		password.send_keys("abcDEF1!" + Keys.ENTER)
		time.sleep(3)
		RedirectCheck = driver.title
		self.assertEqual(RedirectCheck, "Home | My learning | W3Schools")
		driver.find_element_by_class_name("_W0vjl").click()

	@unittest.expectedFailure	
	def test_02_wrong_email(self):
		driver.get(URL);
		email.send_keys("vovgank@mail.com")
		password.send_keys("abcDEF1!" + Keys.ENTER)
		time.sleep(3)  
		RedirectCheck = driver.title
		self.assertEqual(RedirectCheck, "Home | My learning | W3Schools")
		driver.find_element_by_class_name("_W0vjl").click()

	@unittest.expectedFailure
	def test_03_wrong_password(self):
		driver.get(URL);
		email.send_keys("vovgank@mail.ru")
		password.send_keys("1" + Keys.ENTER)
		time.sleep(3)  
		RedirectCheck = driver.title
		self.assertEqual(RedirectCheck, "Home | My learning | W3Schools")
		driver.find_element_by_class_name("_W0vjl").click()

	def test_04_forgot_password(self):
		driver.get(URL);
		driver.find_element_by_css_selector("._Sg7KA").click()
		time.sleep(3) 
		RedirectCheck = driver.title
		self.assertEqual(RedirectCheck, "Reset password - W3Schools")

	@unittest.expectedFailure
	def test_05_password_copy_paste(self):
		driver.get(URL);
		elem.send_keys("password")
		elem.send_keys(Keys.CONTROL, 'a') 
		elem.send_keys(Keys.CONTROL, 'c')
		elem.send_keys(Keys.CONTROL, 'v') 
		value = password.get_attribute("value")
		self.assertEqual(value, "passwordpassword")

if __name__ == '__main__':
    unittest.main(verbosity=3)

