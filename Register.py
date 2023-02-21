import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestRegister(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_success_register(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # click button sign up
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#name_register").send_keys("testerajagan") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#email_register").send_keys("Irvann@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password_register").send_keys("testerjago") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.CLASS_NAME,"swal2-title").text
        response_message = browser.find_element(By.CLASS_NAME,"swal2-content").text

        self.assertIn('berhasil', response_data)
        self.assertEqual(response_message, 'created user!')

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
 unittest.main()