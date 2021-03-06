#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# specify urls
urlPages = []

# Specify the sleep time
sleepTime = .1 

# Specify aimed data
outerAimedData = ['BIB','NAME','CATEGORY','RANK','GENDER PLACE']
innerAimedData = ['CITY','PROVINCE','COUNTRY']

# Specify data to be renamed
oldColumnName = ['CATEGORY']
newColumnName = ['AGE']

# Specify output folder
outputFolder = ''

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
from WebScrapping import CollectData,CollectTable,TableToData,CreateFinalFile,GUI,GUIKill,GUIChangeStatus,GUIChangeError,wait_clickability_element
import time
import re

def CollectInnerData(driver):
    import pandas as pd
    
    data = None
    innerXpath = "//div[@id='athlete-popup']"
    void = 0

    innerTableStyleOld = CollectTable(driver,innerXpath)[0].get_attribute('style')
    innerTableHTMLOld = CollectTable(driver,innerXpath)[0].get_attribute('innerHTML')
    wait_clickability_element(driver,"//tr[@role='row']//td[4]//a")
    namesHTML = driver.find_elements_by_xpath("//tr[@role='row']//td[4]//a")
    
    for i,nameHTML in enumerate(namesHTML):
        try:
            driver.execute_script("arguments[0].click();", nameHTML)
        except:
            if data is None:
                void += 1
            else:
                data = data.append(pd.Series(), ignore_index=True)
        else:
            initialTime = int(time.time())
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
                
                if int(time.time())-initialTime>100:
                    GUIChangeError('Runtime Error - 83')
                    driver.quit()
                    GUIKill()
            
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
    global outputFolder
        
    raceTitleHTML = driver.find_elements_by_xpath("//div[@id='main']//h1[1]")
    raceTitle = raceTitleHTML[0].text
    raceDateTypeHTML = driver.find_elements_by_xpath("//div[@id='main']//p[1]")
    
    try:
        [raceDate,raceType] = re.split(r"•", raceDateTypeHTML[0].text)
        fileString = raceTitle + "_" + raceDate + "_" + raceType
    except:
        fileString = raceTitle
        GUIChangeError("Procedure Error - 127")
        
    fileString = fileString.replace('/', '-')
    fileName = outputFolder + fileString + ".txt"
    
    heading = urlPage + '\n' + raceTitle + '\n' + raceDateTypeHTML[0].text + '\n\nline 1\nline 2\nline 3\nline 4\n'
    
    CreateFinalFile(fileName,data,heading)
            

def PageScrapping(driver,urlInfo,urlPage):
    driver = CollectData(driver,urlPage)
    data = None
    pageNumber=1
    
    # Loop to identify where should the script go for another page
    
    while (len(driver.find_elements_by_xpath("//tr[@role='row']//td[4]//a"))>0):
        
        GUIChangeStatus(urlInfo+' Page: '+str(pageNumber))
        
        viewbtnHTML = driver.find_elements_by_xpath("//tr[@role='row']//div[contains(@aria-expanded, 'true')]")
        for viewbtn in viewbtnHTML:
            driver.execute_script("arguments[0].click();", viewbtn)
            time.sleep(1)
        
        data = CollectContentPage(data,driver)
        firstLineHTMLOld = driver.find_elements_by_xpath("//div[@class='ui-datatable-tablewrapper']")[0].get_attribute('innerHTML')
        nxtbtnHTML = driver.find_elements_by_xpath("//div[@id='mainForm:pageNav']//a[contains(@class, 'fa-angle-right')]")
        if len(nxtbtnHTML)>0:
            driver.execute_script("arguments[0].click();", nxtbtnHTML[0])
            pageNumber += 1
            initialTime = int(time.time())
            while True:
                try:
                    firstLineHTML = driver.find_elements_by_xpath("//div[@class='ui-datatable-tablewrapper']")[0].get_attribute('innerHTML')
                except:
                    continue
                if firstLineHTMLOld != firstLineHTML:
                    time.sleep(1)
                    break
                
                if int(time.time())-initialTime>10:
                    GUIChangeError('Runtime Error - 170')
                    driver.quit()
                    GUIKill()
        else:
            break
    
    data = ProcessData(data)
        
    CreateFile(urlPage,data,driver)

def main():
    from selenium import webdriver
    
    global urlPages,outputFolder
    
    urlPages,settings = GUI('SportStats')
    
    outputFolder = settings['Path']
    
    lenurls = len(urlPages)
    if lenurls>0:
        driver = webdriver.Chrome()
        
    for i,urlPage in enumerate(urlPages):
        urlInfo = 'URL: '+urlPage
        initialTime = int(time.time())
        while True:
            try:
                PageScrapping(driver,urlInfo,urlPage)
                break
            except:
                if int(time.time())-initialTime>30:
                    GUIChangeError(urlInfo+'\n Runtime ALOK Error - 202')
                    driver.quit()
                    GUIKill()
            
            
        
    if lenurls>0:
        driver.quit()
        
    GUIKill()
    return

if __name__ == '__main__':
    main()
