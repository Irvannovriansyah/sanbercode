import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestCheckout(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_success_checkout(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('PRODUCTS', response_data)

        driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click() # click add to cart
        time.sleep(1)
        driver.find_element(By.CLASS_NAME,"shopping_cart_link").click() # click keranjang
        time.sleep(1)
        driver.find_element(By.ID,"checkout").click() # click checkout
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#first-name").send_keys("irvan") # isi first name
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#last-name").send_keys("novri") # isi last name
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"input#postal-code").send_keys("12345") # isi postal code
        time.sleep(1)
        driver.find_element(By.ID,"continue").click() # click continue
        time.sleep(1)
        driver.find_element(By.ID,"finish").click() # click finish
        time.sleep(1)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
  unittest.main()