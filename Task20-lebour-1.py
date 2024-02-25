from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
import requests

class Lebour:
    def __init__(self, url="https://labour.gov.in/"):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.actionChains = ActionChains(self.driver)
        
    def boot(self):
       self.driver.get(self.url)
       sleep(3)
       self.driver.maximize_window()
       sleep(2)
    
    def quit(self):
        sleep(3)
        self.driver.quit()
        
    def getElementByXPATH(self,xpath):
        return self.driver.find_element(by=By.XPATH, value=xpath)
    
    def closePopUpBody(self):
        self.getElementByXPATH('//*[@id="popup"]/div[2]/button').click()
        sleep(3)
        print("the pop up is closed")
    
    def clickOnMonthlyProgressReport(self):
        documentElement = self.getElementByXPATH('//*[@id="nav"]/li[7]/a')
        self.actionChains.move_to_element(documentElement).perform()
        self.getElementByXPATH('//*[@id="nav"]/li[7]/ul/li[2]/a').click()
        print("success: click on the monthly progress report")
        sleep(3)
    
    def openDocument(self):
        self.getElementByXPATH('//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/a').click()
        sleep(2)
        self.driver.switch_to.alert.accept()
        sleep(2)
        print("success: the document is opened")
        
        
    def downloadDocument(self):
        sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        url = self.driver.current_url
        print("the URL of the document is", url)
        
        response = requests.get(url)
        if response.status_code == 200:
         filePath = "monthlyProgressReport.pdf"
         f = open(filePath, "wb")
         f.write(response.content)
         f.close()
        else:
         print("Error")
    
if __name__ == "__main__":
    obj = Lebour()
    obj.boot()
    obj.closePopUpBody()
    obj.clickOnMonthlyProgressReport()
    obj.openDocument()
    obj.downloadDocument()
    obj.quit()
    
        
    