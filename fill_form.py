# -----check README.md file for instructions-----
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
import time
# --------------load chrome driver for linux----------------
#chrome = webdriver.Chrome(service=Service("./chromedriver"))

# load chrome driver for windows.
chrome = webdriver.Chrome(service=Service("chromedriver.exe"))



# ---------google for url/link-----------------------------
link='https://docs.google.com/forms/d/e/1FAIpQLSe_lvJeF5eq0HVB3T55Am73Ayzq4Y5Hq0sfPEeVht9GfQLHYA/viewform'

# --------------load the form------------------------------
chrome.get(link)


def fields_fill(date,time_of_day,cow,milk_qty,status): #automation function

    text_box = chrome.find_elements(By.XPATH,"//input[@type='text']") # get the input field
    text_box=text_box[:-1] # remove submit input
    radio_field = chrome.find_elements(By.XPATH,"//*[@role='radio']") # get radio button field

    time.sleep(1) # delay for one second

    for radio in radio_field: # loop over the radio field
        # match data with existing radio fields
        if radio.get_attribute("data-value").upper()==time_of_day:
            radio.click()
        if radio.get_attribute("data-value")==cow:
            radio.click()
        if radio.get_attribute("data-value")==status:
            radio.click()

    inputs_lst=[date,milk_qty] # data required in input text form

    for i in range(len(text_box)): # loop over text field elements
        text_box[i].clear()
        text_box[i].send_keys(inputs_lst[i])
    # get the submit button
    submit = chrome.find_elements(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')


    submit[0].click() # submit the form 

    next = chrome.find_element(By.XPATH,
        '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')  # load the another response

    next.click() # submit another response

data= open("Data.csv") # load data nb: filename=Data.csv

read_data=csv.reader(data,delimiter=',') # load data nb: separated by comma

for row in read_data: # loop over data rows
    fields_fill(row[0],row[1],row[2],row[3],row[4]) # invoke automation function

print("===============================================")
print(" -------------Auto Completed--------------------")
print("================================================")