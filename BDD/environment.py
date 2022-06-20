from behave.runner import Context
from selenium import webdriver
# from BDD.POM.registration import Registration
from POM.login import Login
from POM.dashboard import Dashboard
from POM.registration import Registration
def before_all(context: Context):
    # We need to add a driver to the context
    context.driver = webdriver.Chrome("utils/Driver/chromedriver.exe")
    # We need to add all POMS to the context
    print("in before all")
    context.login = Login(context.driver)
    context.dashboard=Dashboard(context.driver)
    context.registration=Registration(context.driver)
    print("login context")
    print(context.login)
    # We add an implicit wait to work with latency issues
    context.driver.implicitly_wait(1)

def after_all(context: Context):
    # This will make sure at the end of a behave test all the drivers are closed
    context.driver.quit()
