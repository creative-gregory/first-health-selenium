from selenium import webdriver
from selenium .webdriver.common.keys import Keys
from selenium .webdriver.common.by import By
from selenium .webdriver.support.ui import WebDriverWait
from selenium .webdriver.support import expected_conditions as EC
import time
import atexit

class Job:
    def __init__(self, title, facility, department, schedule):
        self.title = title
        self.facility =  facility
        self.department = department
        self.schedule = schedule
        
def getNumberOfPages():
    c = 0
    a = []
    numPages = browser.find_element_by_xpath('//*[@id="searchResultsForm"]/fieldset/div[4]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/ul').text

    for page in numPages:
        a.append(page)
        
    return int(max(a))

def writeListToFile(lst):
    f = open("jobs.txt", "+w")

    for item in lst:
        f.write("{0}\n{1}\n{2}\n{3}\n\n".format(item.title, item.facility, item.department, item.schedule))
        
    print("data written")
    
    f.close()
    
def getJobData():
    try:
        # does network call without the need for a timer/delay        
        panel = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "panel.panel-default"))
        )
            
    finally:
        for data in panel:
            position = data.find_element_by_tag_name("h4")
            details = data.find_elements_by_class_name("form-control-static")
    #         department = data.find_element_by_xpath('//label[@for="cDeptName"]')
            
            counter  = 0
            
            for detail in details:
                if counter == 0:
                     facility = str(detail.text)
                if counter == 1:
                    department= str(detail.text)
                if counter == 2:
                    schedule = str(detail.text)

                counter = counter + 1
                
            newJob = Job(str(position.text), facility, department, schedule)
            jobs.append(newJob)
            
        print("data collected")


path = "C:\Program Files (x86)\chromedriver.exe"

browser = webdriver.Chrome(path)
browser.get('https://www.healthcaresource.com/firsthealth/index.cfm?&ijobrowstart=1&ijobpostondaysold=&cjobattr1=All&search=Search&nkeywordsearch=&template=dsp_job_list.cfm&ifacilityid=&fuseaction=search.jobList&ckeywordsearchcategory=cdept%2C%20mdes&ijobcatid=109')
    
jobs = []
maxPages = getNumberOfPages()

if __name__ == "__main__":
    for x in range(0, maxPages):
        getJobData()
        
        if x < maxPages - 1:
            element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "fa.fa-caret-right"))
            )
            
            element.click()
                
    writeListToFile(jobs)

    browser.quit()
