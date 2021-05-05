from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import pandas as pd

# 1. Khai bao bien browser
browser = webdriver.Chrome(executable_path="./chromedriver")

from datetime import datetime, timedelta

current_date = datetime(2021,5,4)
data = []
# Read utl
idx = 0
while True:
    print("Process 300 days from {}-{}-{}".format(current_date.day, current_date.month, current_date.year))

    url = 'https://www.thantai.net/so-ket-qua'
    browser.get(url)

    # Set date
    end = browser.find_element_by_id("end")
    end.clear()
    end.send_keys("{}-{}-{}".format(current_date.day, current_date.month, current_date.year))

    btn = browser.find_element_by_xpath("/html/body/div[2]/main/div/form/div[2]/div/button[9]")
    btn.click()

    result = browser.find_elements_by_class_name("font-weight-bold.text-danger.col-12.d-block.p-1.m-0")
    for row in result:
        print(row.text)
        idx +=1
        data.append(row.text)

    current_date -= timedelta(days = 300)
    # sleep(1)
    if idx > 20*365:
        break

df = pd.DataFrame(data, columns=['KQ'])
df.to_csv("XSMB.csv", index=False)
browser.close()