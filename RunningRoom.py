#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# specify urls
urlPages = ['http://www.events.runningroom.com/site/?raceId=5110&eventId=16937&vrindex=4','http://www.events.runningroom.com/site/?raceId=5110&eventId=16939&vrindex=4','http://www.events.runningroom.com/site/?raceId=5162&eventId=17063&vrindex=4','http://www.events.runningroom.com/site/?raceId=5162&eventId=17064&vrindex=4','http://www.events.runningroom.com/site/?raceId=5162&eventId=17065&vrindex=4','http://www.events.runningroom.com/site/?raceId=5162&eventId=17066&vrindex=4','http://www.events.runningroom.com/site/?raceId=5463&eventId=17964&vrindex=4','http://www.events.runningroom.com/site/?raceId=5463&eventId=17966&vrindex=4','http://www.events.runningroom.com/site/?raceId=5392&eventId=17782&vrindex=4','http://www.events.runningroom.com/site/?raceId=5392&eventId=17781&vrindex=4','http://www.events.runningroom.com/site/?raceId=5392&eventId=17783&vrindex=4','http://www.events.runningroom.com/site/?raceId=5392&eventId=17784&vrindex=4']

# Specify the sleep time
sleepTime = 1 

# Specify aimed data
outerAimedData = ['RANK','BIB','FIRST NAME','CITY','GENDER','DIVISION','GENDER','RANK','DIVISION RANK']

# Specify data to be renamed
oldColumnName = ['FIRST NAME']
newColumnName = ['Name']

# Specify output folder
outputFolder = "/home/setup/Documents/roadraceresults/Results/Unsent Results/RunningRoom/"

#===============================================================================================================================================
#
#                                                    DO NEVER CHANGE UNDER THIS SIGN, THANK YOU.
#
#================================================================================================================================================

"""
Created on Thu Mar  5 15:29:20 2020

@author: Pedro Salamoni
"""

# import libraries
from WebScrapping import CollectData,CollectTable,TableToData,CreateFinalFile
import time
import re

def CollectContentPage(data,driver):
    outerXpath = "//div[@class='event-table-container']"
    outerTableHTML = CollectTable(driver,outerXpath)
    outerData = TableToData(outerTableHTML[0].get_attribute('innerHTML'))[-1]
    
    if data is None:
        data = [outerData,None]
    else:
        data = [data[0].append(outerData),None]
    
    return data

def ProcessData(bulkData):
    
    bulkData[0]['First name'] = bulkData[0]['First name'] + ' ' + bulkData[0]['Last name']
    
    for column in bulkData[0].columns:
        if (column.upper() not in outerAimedData) and (re.match(r"\d+:\d+(:\d+)*(\.\d+)*", str(bulkData[0][column].iloc[1]))==None):
            bulkData[0] = bulkData[0].drop(columns=[column])
        if column.upper() in oldColumnName:
            bulkData[0] = bulkData[0].rename(columns={column: newColumnName[oldColumnName.index(column.upper())]})
            
    return bulkData

def CreateFile(urlPage,data,driver):    
    raceTitleHTML = driver.find_elements_by_xpath("//div[@id='results-content']//h1[@class='results-title']")
    raceTitle = raceTitleHTML[0].text
    #raceDate = driver.find_elements_by_xpath("//div[@class='event-banner']//time[1]")[0].text
        
    fileString = raceTitle #+ "_" + raceDate
    fileString = fileString.replace('/', '-')
    fileString = fileString.replace('\'', '')
    fileString = fileString.replace('\n', ' ')
    fileName = outputFolder + fileString + ".txt"
    
    heading = urlPage + '\n' + raceTitle + '\n\nline 1\nline 2\nline 3\nline 4\n'
    
    CreateFinalFile(fileName,data,heading)
            

def PageScrapping(urlPage):
    driver = CollectData(urlPage)
    data = None
    pageNumber=1
    
    # Loop to identify where should the script go for another page
    while True:
        print('Page:',pageNumber)
        time.sleep(2)
        data = CollectContentPage(data,driver)
        nxtbtnHTML = driver.find_elements_by_xpath("//span[@aria-label='Next page']/parent::a")
        try:
            nxtbtnHTML[-1].click()
            pageNumber += 1
        except:
            break
    
    data = ProcessData(data)
        
    CreateFile(urlPage,data,driver)
    
    driver.quit()

def main():
    for urlPage in urlPages:
        print(urlPage)
        PageScrapping(urlPage)
    return

main()
