from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
import requests

class DownloadImages:
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
    
    def clickOnPhotoGallery(self):
        mediaElement = self.getElementByXPATH('//*[@id="nav"]/li[10]/a')
        self.actionChains.move_to_element(mediaElement).perform()
        self.getElementByXPATH('//*[@id="nav"]/li[10]/ul/li[2]/a').click()
        print("success: click on the photo gallery")
        sleep(3)
        
        
    def downloadPhoto(self):
        sleep(2)
        for i in range(1, 11):
            xpath = f'//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/table/tbody/tr[{i}]/td[1]/div[1]/div/img'
            url = self.getElementByXPATH(xpath).get_attribute("src")
        print("the URL of the image is", url) 
        response = requests.get(url)
        if response.status_code == 200:
         filePath = f"Image/image{i}.pmg"
         f = open(filePath, "wb")
         f.write(response.content)
         f.close()
         print("Image {i} is successfully downloaded")
        else:
         print("Error")
    
if __name__ == "__main__":
    obj = DownloadImages()
    obj.boot()
    obj.closePopUpBody()
    obj.clickOnPhotoGallery()
    obj.downloadPhoto()
    obj.quit()
    
        
    