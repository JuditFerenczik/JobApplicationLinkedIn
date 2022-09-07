from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from secrets import USERNAME,PASSWORD,PHONENUMBER

checkedIds = []
with open("output.txt", 'r') as out:
    checkedIds += out.readlines()
    checkedIds = [id.strip() for id in checkedIds]
    print(checkedIds)
    print(checkedIds[2])

service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=101884063&keywords=python%20developer&location=88441%2C%20Mittelbiberach%2C%20Baden-W%C3%BCrttemberg%2C%20Germany&refresh=true")
time.sleep(5)
try:
    #cookies = driver.find_element(By.LINK_TEXT,"Accept")
    #cookies.click()
    signIn = driver.find_element(By.LINK_TEXT,"Sign in")
    signIn.click()
except:
    print("No cookies to accept")
time.sleep(5)
cookies = driver.find_element(By.XPATH,"//*[@id='artdeco-global-alert-container']/div/section/div/div[2]/button[1]")
cookies.click()
time.sleep(2)
username = driver.find_element(By.ID,"username")
username.send_keys(USERNAME)
time.sleep(2)
password = driver.find_element(By.ID,"password")
password.send_keys(PASSWORD)
time.sleep(2)
signIn = driver.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button")
signIn.click()


## TODO put everything inside pagination -> put everything inside job lists on each pages
time.sleep(2)
pagesButton = driver.find_elements(By.CSS_SELECTOR, "ul.artdeco-pagination__pages button")
#pagesButton[2].click()
newIds = []
for i in range(0,len(pagesButton)):
    pagesButton = driver.find_elements(By.CSS_SELECTOR, "ul.artdeco-pagination__pages button")
    pagesButton[i].click()
    time.sleep(2)
    jobsContainer = driver.find_elements(By.CSS_SELECTOR, "#main ul.scaffold-layout__list-container li.jobs-search-results__list-item")
    # jobsContainer2 = driver.find_elements(By.CSS_SELECTOR,"#main ul.scaffold-layout__list-container li img")
    jobsId = [job.get_attribute("data-occludable-job-id") for job in jobsContainer]
    # jobsId = [job for job in jobsId if (job is  not None)]__list-item
    print(len(jobsContainer))
    print(jobsId)
    print(len(jobsId))
    for j in range(0, len(jobsId)):
        if not (jobsId[j] in checkedIds):
            jobsContainer[j].click()
            saveB = driver.find_element(By.CLASS_NAME, "jobs-save-button")
            saveB.click()
            newIds.append(jobsId[j])
            print(f"round {j}")

            # easyApply = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
            # easyApply.click()
            # inputText = driver.find_element(By.CSS_SELECTOR, "input")
            # inputText.send_keys(PHONENUMBER)
            # nextButton = driver.find_element(By.CSS_SELECTOR, "button")
            # nextButton.click()

    #jobsId.extend(tmpId)
print(newIds)

with open("output.txt", 'a') as out:
    for i in range(0,len(newIds)):
        out.write(newIds[i] + '\n')

