#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# specify urls
urlPages = ['https://results.raceroster.com/results/hnn775vbx5n7gxxt']

# Specify the sleep time
sleepTime = 1 

# Specify aimed data
outerAimedData = ['OVERALL PLACE','BIB','NAME','DIVISION','DIVISION PLACE','GENDER','GENDER PLACE','CITY']

# Specify data to be renamed
oldColumnName = ['CATEGORY']
newColumnName = ['AGE']

# Specify output folder
outputFolder = "/home/setup/Documents/roadraceresults/Results/Unsent Results/ChipTimeResults/"

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
    outerXpath = "//div[@class='results-listing']"
    outerTableHTML = CollectTable(driver,outerXpath)
    outerData = TableToData(outerTableHTML[0].get_attribute('innerHTML'))[-1]
    
    if data is None:
        data = [outerData,None]
    else:
        data = [data[0].append(outerData),None]
    
    return data

def ProcessData(bulkData):
    
    for column in bulkData[0].columns:
        if (column.upper() not in outerAimedData) and (re.match(r"\d+:\d+(:\d+)*(\.\d+)*", str(bulkData[0][column].iloc[1]))==None):
            bulkData[0] = bulkData[0].drop(columns=[column])
            
    return bulkData

def CreateFile(urlPage,data,driver):    
    raceTitleHTML = driver.find_elements_by_xpath("//div[@class='event-banner']//h1[1]")
    raceTitle = raceTitleHTML[0].text.split(' - ')[0]
    raceDate = driver.find_elements_by_xpath("//div[@class='event-banner']//time[1]")[0].text
        
    fileString = raceTitle + "_" + raceDate
    fileString = fileString.replace('/', '-')
    fileName = outputFolder + fileString + ".txt"
    
    heading = urlPage + '\n' + raceTitle + '\n' + raceDate + '\n\nline 1\nline 2\nline 3\nline 4\n'
    
    CreateFinalFile(fileName,data,heading)
            

def PageScrapping(urlPage):
    driver = CollectData(urlPage)
    data = None
    pageNumber=1
    
    # Loop to identify where should the script go for another page
    while True:
        print('Page:',pageNumber)
        data = CollectContentPage(data,driver)
        nxtbtnHTML = driver.find_elements_by_xpath("//span[@aria-label='Next page']/parent::a")
        try:
            nxtbtnHTML[-1].click()
            pageNumber += 1
            time.sleep(1)
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
