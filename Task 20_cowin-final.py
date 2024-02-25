from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver import ActionChains


class Cowin:
    
    def __init__(self, url= "https://www.cowin.gov.in/" ):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
 
    def boot(self):
       self.driver.get(self.url)
       self.driver.maximize_window()
       sleep(2)
       
    def get_window_id(self):
        parent_window_handle = self.driver.current_window_handle
        print(parent_window_handle)
        all_window_handles = self.driver.window_handles
        print(all_window_handles)
        
    def close_window(self):
        second_window = self.driver.window_handles[2]
        self.driver.switch_to.window(second_window)
        self.driver.close()
        sleep(1)
        third_window = self.driver.window_handles[1]
        self.driver.switch_to.window(third_window)
        self.driver.close
        sleep(2)
        third_window = self.driver.window_handles[0]
        self.driver.switch_to.window(third_window)
        self.driver.close
        sleep(2)
        
    def FAQ(self):
        xpath = "/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a"
        self.driver.find_element(by=By.XPATH, value=xpath).click()
        sleep(5)
        
    def PARTNERS(self):
        xpath = "/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a"
        self.driver.find_element(by=By.XPATH, value=xpath).click()
        sleep(5)
        
    def quit(self):
        self.driver.quit()
        
obj = Cowin()
obj.boot()
obj.FAQ()
obj.PARTNERS()
obj.get_window_id()
obj.close_window()
obj.quit()

        