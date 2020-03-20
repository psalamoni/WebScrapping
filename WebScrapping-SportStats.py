#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# specify urls
urlPages = ['https://east.sportstats.ca/display-results.xhtml?raceid=13143']

# Specify the sleep time
sleepTime = .1 

# Specify aimed data
outerAimedData = ['BIB','NAME','CATEGORY','RANK','GENDER PLACE']
innerAimedData = ['CITY','PROVINCE','COUNTRY']

# Specify data to be renamed
oldColumnName = ['CATEGORY']
newColumnName = ['AGE']

# Specify output folder
outputFolder = "/home/setup/Documents/roadraceresults/Results/Unsent Results/SportStats/"

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

def CollectInnerData(driver):
    import pandas as pd
    
    data = None
    innerXpath = "//div[@id='athlete-popup']"
    void = 0

    innerTableStyleOld = CollectTable(driver,innerXpath)[0].get_attribute('style')
    innerTableHTMLOld = CollectTable(driver,innerXpath)[0].get_attribute('innerHTML')
    namesHTML = driver.find_elements_by_xpath("//tr[@role='row']//td[4]//a")
    
    for i,nameHTML in enumerate(namesHTML):
        try:
            nameHTML.click()
            #time.sleep(sleepTime)
        except:
            if data is None:
                void += 1
            else:
                data = data.append(pd.Series(), ignore_index=True)
        else:
            while True:
                try:
                    innerTableHTML = CollectTable(driver,innerXpath)[0].get_attribute('innerHTML')
                    innerTableStyle = CollectTable(driver,innerXpath)[0].get_attribute('style')
                except:
                    continue
                if (innerTableHTMLOld!=innerTableHTML) or (innerTableStyleOld!=innerTableStyle):
                    innerTableStyleOld = innerTableStyle
                    innerTableHTMLOld = innerTableHTML
                    innerDataRow = TableToData(innerTableHTML)[0].set_index(0).T
                    if data is None:
                        data = innerDataRow
                        if void != 0:
                            for _ in range(void):
                                data = data.append(pd.Series(), ignore_index=True)
                    else:                
                        data = data.append(innerDataRow)
                    break
            
    return data

def CollectContentPage(data,driver):
    outerXpath = "//div[@id='mainForm:result_table']"
    outerTableHTML = CollectTable(driver,outerXpath)
    outerData = TableToData(outerTableHTML[0].get_attribute('innerHTML'))[0]
    
    innerData = CollectInnerData(driver)
    
    if data is None:
        data = [outerData,innerData]
    else:
        data = [data[0].append(outerData),data[1].append(innerData)]
    
    return data

def ProcessData(bulkData):
    
    for column in bulkData[0].columns:
        if (column.upper() not in outerAimedData) and (re.match(r"\d+:\d+:\d+(\.\d+)*", str(bulkData[0][column].iloc[1]))==None):
            bulkData[0] = bulkData[0].drop(columns=[column])
    
    for column in bulkData[1].columns:
        if column.upper() not in innerAimedData:
            try:
                bulkData[1] = bulkData[1].drop(columns=[column])
            except:
                continue
            
    return bulkData

def CreateFile(urlPage,data,driver):    
    raceTitleHTML = driver.find_elements_by_xpath("//div[@id='main']//h1[1]")
    raceTitle = raceTitleHTML[0].text
    raceDateTypeHTML = driver.find_elements_by_xpath("//div[@id='main']//p[1]")
    
    try:
        [raceDate,raceType] = re.split(r"•", raceDateTypeHTML[0].text)
    except:
        print("Something went wrong, contact Pedro Salamoni [Descriptions Pattern Error][3]")
        
    fileString = raceTitle + "_" + raceDate + "_" + raceType
    fileString = fileString.replace('/', '-')
    fileName = outputFolder + fileString + ".txt"
    
    heading = urlPage + '\n' + raceTitle + '\n' + raceDateTypeHTML[0].text + '\n\nline 1\nline 2\nline 3\nline 4\n'
    
    CreateFinalFile(fileName,data,heading)
            

def PageScrapping(urlInfo,urlPage):
    driver = CollectData(urlPage)
    data = None
    pageNumber=1
    
    # Loop to identify where should the script go for another page
    while (len(driver.find_elements_by_xpath("//tr[@role='row']//td[4]//a"))>0):
        print(urlInfo,'Page:',pageNumber)
        
        viewbtnHTML = driver.find_elements_by_xpath("//tr[@role='row']//div[contains(@aria-expanded, 'true')]")
        for viewbtn in viewbtnHTML:
            viewbtn.click()
            time.sleep(1)
        
        data = CollectContentPage(data,driver)
        firstLineHTMLOld = driver.find_elements_by_xpath("//div[@class='ui-datatable-tablewrapper']")[0].get_attribute('innerHTML')
        nxtbtnHTML = driver.find_elements_by_xpath("//div[@id='mainForm:pageNav']//a[contains(@class, 'fa-angle-right')]")
        if len(nxtbtnHTML)>0:
            nxtbtnHTML[0].click()
            pageNumber += 1
            while True:
                try:
                    firstLineHTML = driver.find_elements_by_xpath("//div[@class='ui-datatable-tablewrapper']")[0].get_attribute('innerHTML')
                except:
                    continue
                if firstLineHTMLOld != firstLineHTML:
                    time.sleep(.5)
                    break
        else:
            break
    
    data = ProcessData(data)
        
    CreateFile(urlPage,data,driver)
    
    driver.quit()

def main():
    lenurls = len(urlPages)
    for i,urlPage in enumerate(urlPages):
        print(urlPage)
        urlInfo = 'URL: ' + str(i+1) + '/' + str(lenurls) 
        PageScrapping(urlInfo,urlPage)
    return

main()
