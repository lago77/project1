from ast import Num
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
class Dashboard():
    def __init__(self, driver: WebDriver):
    # def __init__(self, driver):
        self.driver = driver
        """This class is injected with a driver on intialization"""
        print("test")
        time.sleep(4)
        self.username_input = ""
        self.password_input = ""
        self.submitrequest = ""
        self.num_elements=0
        self.cancelbutton=""
        self.approve =""
        self.deny=""
    def insert_request(self, description, amount):

        self.description_input = self.driver.find_element(By.ID, "description")
        self.amount_input = self.driver.find_element(By.ID, "amount")
        self.submitrequest = self.driver.find_element(By.ID, "submitrequest")

        self.description_input.send_keys(description)
        self.amount_input.send_keys(amount)
        self.submitrequest.click()

    def element_count(self):
        elements=self.driver.find_elements(By.ID,'data')
        self.num_elements=len(elements)
        return self.num_elements

    def cancel(self):
        self.cancelbutton=self.driver.find_element(By.ID, "cancel")
        self.cancelbutton.click()

    def process(self,result):
        if result=="approve":
            newvalue="testing"
            # self.approve=self.driver.find_element(By.ID, "approve")
            print("self approve")
           
            print("the value is")
        
            # statusinput=self.driver.find_element(By.ID, "status")
            # newvalue=statusinput.get_attribute("value")
            # print(newvalue)



            # element= self.driver.find_element(By.ID, "status")
            # myatt=element.get_attribute("value") 
            # element.setAttribute("Deny")
            mybutton=self.driver.find_element(By.ID, "approve")
            print("at status")
            status=self.driver.find_element(By.ID, "status")
            
            # mystatus=status.get_attribute("value")
            # print("my status",mystatus)
            # mybutton.click()
            # time.sleep(3)
            # status=self.driver.find_element(By.ID, "status")
            # mystatus=status.get_attribute("value")
            # print("my new status",mystatus)

            element= self.driver.find_element(By.ID, "status")
            myatt=element.get_attribute("value") 
            # element.setAttribute("Deny")
            mybutton=self.driver.find_element(By.ID, "approve")
            status=self.driver.find_element(By.ID, "status")
            mystatus=status.get_attribute("value")
            print("my status",mystatus)
            mybutton.click()
            status=self.driver.find_element(By.ID, "status")
            mystatus=status.get_attribute("value")
            print("my status",mystatus)
            print("my attribute",myatt)  


            return mystatus
        if result=="deny":
            self.deny=self.driver.find_element(By.ID, "deny")
            self.deny.click()
            self.deny.get_attribute("value")




    # mybutton=driver.find_element(By.ID, "approve")
    # status=driver.find_element(By.ID, "status")
    # mystatus=status.get_attribute("value")
    # print("my status",mystatus)
    # mybutton.click()
    # status=driver.find_element(By.ID, "status")
    # mystatus=status.get_attribute("value")