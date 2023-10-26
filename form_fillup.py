from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class G_form:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options, service=Service(ChromeDriverManager().install()))
        self.driver.get("https://forms.gle/XNYg119TM5q6QNKWA")
        self.driver.maximize_window()

    def input_price(self, price_data):
        self.price_field = self.driver.find_element(By.XPATH,
                                                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        self.price_field.click()
        self.price_field.send_keys(price_data)

    def input_address(self, address_data):
        self.address_field = self.driver.find_element(By.XPATH,
                                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
        self.address_field.click()
        self.address_field.send_keys(address_data)

    def input_link(self, link_data):
        self.link_field = self.driver.find_element(By.XPATH,
                                                   '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        self.link_field.click()
        self.link_field.send_keys(link_data)

    def submit(self):
        self.submit_button = self.driver.find_element(By.XPATH,
                                                      '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        self.submit_button.click()

    def return_to_form(self):
        self.return_link = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        self.return_link.click()

