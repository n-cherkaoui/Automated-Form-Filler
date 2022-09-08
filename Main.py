# Nawfal Cherkaoui 6/4/22

# This script is a test of Python 3 and Selenium. It automatically opens and fills out a Google form with example data.

# Import Module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def main():
    data = ['First Last', '24', 'example@gmail.com','4078356743', 'Male'] # Example Data
    driver = webdriver.Chrome('chromedriver.exe') # Creates a driver object using the chrome driver
    driver.get('https://forms.gle/iG8Skgx2peg8HdoaA') # Opens example form URL
    count = 0 # Initializes count for loops

    listOfTextBoxes = locateTextBoxes(driver) 
    
    driver.implicitly_wait(1) # Waits until page is loaded or 1 second elapses

    fillTextBoxes(data, listOfTextBoxes,count)

    submit(driver)

    driver.close() # closes the window

# Returns a list of all textboxes on the form
def locateTextBoxes(driver):
    textBoxes = driver.find_elements(By.CLASS_NAME, "zHQkBf")
    return textBoxes

def fillTextBoxes(data, textBoxes, count):

    for value in textBoxes:
        value.send_keys(data[count])
        count+=1

# Clicks on submit button
def submit(driver): 
    
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()

if __name__ == "__main__":
    main()

