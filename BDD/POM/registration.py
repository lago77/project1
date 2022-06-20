from ast import Num
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

import time
class Registration():
    def __init__(self, driver: WebDriver):
    # def __init__(self, driver):
        self.driver = driver
        """This class is injected with a driver on intialization"""
        print("test")
        time.sleep(4)
        self.username_input = ""
        self.password_input = ""
        self.submit = ""
        self.role=""
        self.register =""
    def go_register(self):
        self.register = self.driver.find_element(By.ID, "register")
        self.register.click()
    def Register(self, username, password):

        self.username_input = self.driver.find_element(By.ID, "username")
        self.password_input = self.driver.find_element(By.ID, "password")
        selection = Select(self.driver.find_element(By.ID,'roles'))
     

        selection= Select(self.driver.find_element(By.ID,'roles'))
        selection.select_by_value('Employee')
        myselection=selection.first_selected_option
        self.role=myselection.text

        self.submit = self.driver.find_element(By.ID, "submit")

        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.submit.click()

    def element_count(self):
        elements=self.driver.find_elements(By.ID,'data')
        self.num_elements=len(elements)
        return self.num_elements
