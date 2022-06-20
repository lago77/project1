from util.driver_setup import setup_chrome_driver
from POM.google_images import GoogleImage
from util.download import get_response
from util.file_functions import save_image
from graphics.user_input_gui import Gui
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def main():

    # gui = Gui()
    # search_term = gui.input
    driver = setup_chrome_driver()

    driver.get("http://127.0.0.1:5000/loginpage")
    webpage = GoogleImage(driver)
    driver.find_element(By.ID, "username").send_keys("Omar")
    driver.find_element(By.ID, "password").send_keys("passo")
    driver.find_element(By.ID, "submit").click()
    print("my element")
    mytitle=driver.title
    print("my title is")
    print(mytitle)
    driver.find_element(By.ID, "description").send_keys("Omar")
    driver.find_element(By.ID, "amount").send_keys(555)
    driver.find_element(By.ID, "submitrequest").click()
    time.sleep(5000)
    # webpage.search(search_term)

    # urls = webpage.get_img_url(4)
    # counter = 0
    # for url in urls:
    #     response = get_response(url)
    #     if response:
    #         counter += 1
    #         save_image(response, f"{search_term}_{counter}.jpg")
    
    # driver.quit()

if __name__ == "__main__":
    main()