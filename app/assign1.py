from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import pytz
import re
import os
import pymongo
from selenium.webdriver.common.keys import Keys

store="mongodb+srv://root:admin123@99acres.zjfswgq.mongodb.net/"
client=pymongo.MongoClient(store)
mydb=client["store"]
mycol=mydb["plot"]

path = 'E:\Assignment\chromedriver-win64\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

def start(city):
    url = "https://www.99acres.com/"
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)
    a=driver.find_element(By.XPATH,'//*[@id="d_landmark_inPageSearchBox"]/div').click()
    time.sleep(1)
    a=driver.find_element(By.XPATH,'//*[@id="keyword2"]')
    a.send_keys(city)
    time.sleep(1)
    a.send_keys(Keys.ENTER)
    time.sleep(1)
    count = 1
    total=1
    while True:
        try:
            time.sleep(5)
            element = driver.find_element(By.XPATH, f'//*[@id="app"]/div/div/div[5]/div[3]/div[2]/section[{count}]')
            hell = element.find_element(By.XPATH, f'//*[@id="app"]/div/div/div[5]/div[3]/div[2]/section[{count}]/div/div/div/div[2]/div')
            entry = {}
            link = element.find_elements(By.XPATH, './/a[@href]')
            for a in link:
                entry['href'] = a.get_attribute('href')
                break
            try:
                name=hell.find_element(By.XPATH, './div/div').text
                entry["Name"] = name
            except:
                entry["Name"] = None
            
            try:
                cost=hell.find_element(By.XPATH, './div/div[4]/div[1]').text
                entry["Cost"] = cost
            except:
                entry["Cost"] = None
            
            try:
                store=hell.find_element(By.XPATH, './div/h2').text
                type = re.search(r'(.+?)\s+in', store)
                entry["Type"] = type.group(1)
            except:
                entry["Type"] = None
            
            try:
                area=hell.find_element(By.XPATH, '//*[@id="projectTupleData_398084"]/div[1]/div[4]/div[2]/div/div/div/div/div/div[2]').text
                entry["Area"] = area
            except:
                entry["Area"] = None
            try:
                area=hell.find_element(By.XPATH, '//*[@id="projectTupleData_375404"]/div[1]/div[4]/div[2]/div/div/div/div/div[1]/div[2]').text
                entry["Area1"] = area
            except:
                entry["Area1"] = None
            
            try:
                area=hell.find_element(By.XPATH, '//*[@id="projectTupleData_375404"]/div[1]/div[4]/div[2]/div/div/div/div/div[2]/div[2]').text
                entry["Area2"] = area
            except:
                entry["Area2"] = None
            
            try:
                text=hell.find_element(By.XPATH, './div/h2').text
                locality=re.search(r'in\s+(.+)', text)
                entry["Locality"] = locality.group(1)
            except:
                entry["Locality"] = None
            
            entry["city"]=city
            x = mycol.insert_one(entry)

            hell = driver.find_element(By.XPATH, f'//*[@id="app"]/div/div/div[5]/div[3]/div[2]/section[{count+1}]')
            time.sleep(2)
            driver.execute_script("arguments[0].scrollIntoView();", hell)
            print(count)
            count += 1
        except Exception as e:
            try:
                next_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[5]/div[3]/div[3]/div[3]/a')
                next_button.click()
                count = 1
                print(total)
                total+=1
                continue
            except NoSuchElementException:
                print("error")
                break

    driver.quit()



