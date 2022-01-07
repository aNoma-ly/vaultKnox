from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

'''
s = Service("/Users/massiveboi/Documents/ChromeDriver/chromedriver")

driver = webdriver.Chrome(service=s)

driver.get("https://www.accuweather.com/en/za/rosebank/301165/hourly-weather-forecast/301165")

hourList = []
timeList = []

try:
    for hour in range(0, 8):

        hourCard = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "hourlyCard" + str(hour))))

        hourCard.click()
        time.sleep(6)

        if (hour == 11):
            time.sleep(6)

        accordion1 = hourCard.find_element(By.CLASS_NAME, "accordion-item-header-container")
        nfl1 = accordion1.find_element(By.CLASS_NAME, "hourly-card-nfl-header")
        dateN = nfl1.find_element(By.CLASS_NAME, "date")
        timeN = dateN.find_element(By.TAG_NAME, "span")
        timeList.append(timeN.text)


        accordion = hourCard.find_element(By.CLASS_NAME, "accordion-item-content")
        nfl = accordion.find_element(By.CLASS_NAME, "hourly-card-nfl-content")
        content = nfl.find_element(By.CLASS_NAME, "hourly-content-container")
        outPTS = content.find_elements(By.TAG_NAME, "span")

        counter = 0
        UVIndex = ""
        for outPT in outPTS:
            if (counter == 1):
                UVIndex = outPT.text

                counter += 1
            else:
                counter += 1
        list(UVIndex)
        rating = ''.join([str(UVIndex[0]), str(UVIndex[1])])
        intRating = int(rating)
        if intRating > 11:
            break
        else:
            hourList.append(intRating)

finally:
    time = 11
    elemtime = 11
    hottest = 0
    timeI = 0
    timeF = 0
    for elem in hourList:

        if elem >= hottest:
            hottest = elem
            time = elemtime
            timeF = timeI
            elemtime += 1
            timeI += 1
        else:
            elemtime += 1
            timeI += 1

    start = "UV Index: " + str(hottest) + " Time: " + str(timeList[timeF]) + ":00"
    driver.quit()

now = datetime.now()
activities = ["Face wash, Moisturise", "Eat oats eggs honey", "Supplements", "Breathing", "Reading", "Work for an hour",
              "Netflix and stretch", "Work for an hour", "Youtube", "Work for an hour"]

minutes = [5, 30, 2, 15, 30, 60, 60, 60, 60, 60]'''