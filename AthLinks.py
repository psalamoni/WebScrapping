#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# specify urls
urlPages = []

# Specify the sleep time
sleepTime = 2

# Specify aimed data
outerAimedData = ['BIB','NAME','AGE','OVERALL','GENDER','CITY','COUNTRY','DIVISION','PACE','TIME']

# Specify data to be renamed
oldColumnName = ['GENDER']
newColumnName = ['GENDER PLACE']

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
from selenium import webdriver
import time
import re
from WebScrapping import CollectData,CreateFinalFile,GUI,GUIKill,GUIChangeStatus,GUIChangeError,wait_visibility_element,wait_clickability_element

#import pandas as pd
#import urllib.request
#from bs4 import BeautifulSoup


def CollectHeader(driver):
    columnsHTML = driver.find_elements_by_xpath("//div[@class='row mx-0']/div")
    data = []
    for columnHTML in columnsHTML:
        column = []
        column.append(columnHTML.text)
        data.append(column)
    data.pop(0)
    data = [['']] + data + [['']]
        
    return data

def CollectContent(data,driver):
    results = driver.find_elements_by_xpath("//div[contains(@class,'link-to-irp')]/div")
    
    if data is None:
        data = CollectHeader(driver)
    num_columns = len(data)
    
    for i,result in enumerate(results):
        try:
            data[i%num_columns].append(result.text)
        except:
            GUIChangeError('Runtime Error - 67')
                
    return data

def CollectContentPage(data,driver):
    data = CollectContent(data,driver)
    return data

def ProcessData(bulkData):
    import pandas as pd
    
    data = []
    
    bulkData.pop()
    
    dataadd = [['NAME'],['AGE'],['BIB'],['CITY'],['COUNTRY']]
    
    for column in bulkData[0][1:]:
        if len(re.split('\n',column)) == 5:
            [bulk,name,age,bib,country] = re.split('\n',column)
        elif len(re.split('\n',column)) == 4:
            [bulk,name,age,country] = re.split('\n',column)
            bib = None
        else:
            [bulk,name,country] = re.split('\n',column)
            age = None
            bib = None
        country = re.split(', ',country)
        
        if len(country)>1 :
            city = country[0]
            country = country[1]
        else:
            city = ''
            country = country[0]
            
        dataadd[0].append(name)
        dataadd[1].append(age)
        dataadd[2].append(bib)
        dataadd[3].append(city)
        dataadd[4].append(country)
        
    bulkData.pop(0)
    bulkData = dataadd + bulkData
        
    for column in bulkData:
        if ((column[0] in outerAimedData) or (re.match(r"\d+:\d+:\d+(\.\d+)*", column[1]))):
            try:
                column[0] = newColumnName[oldColumnName.index(column[0])]
                data.append(column)
            except:
                data.append(column)
                
    data = pd.DataFrame(data).set_index(0).T
    data['BIB'] = data['BIB'].replace('Bib ','', regex=True)
    data['PACE'] = data['PACE'].replace('\nMIN/MI','', regex=True)
            
    return data

def CreateFile(urlPage,data,driver):
    global outputFolder
    
    raceTitleHTML = driver.find_elements_by_xpath("//h1[@id='master-event-name']")
    raceTitle = raceTitleHTML[0].text
    
    raceDateTypeHTML = driver.find_elements_by_xpath("//div[@id='total-results-string']/preceding-sibling::div[1]")
    raceDate = '_' + raceDateTypeHTML[0].text
    
    heading = urlPage + '\n' + raceTitle + '\n' + raceDate + '\nline 1\nline 2\nline 3\nline 4\n'
      
    fileName = outputFolder + raceTitle + raceDate + ".txt"
    
    CreateFinalFile(fileName,data,heading)
            

def PageScrapping(driver,urlInfo,urlPage):
    driver = CollectData(driver,urlPage)
    wait_visibility_element(driver,"//div[contains(@class,'link-to-irp')]/div")
    
    try:
        wait_clickability_element(driver,"//button[contains(text(), 'okay, got it')]")
        cookiesbtnHTML = driver.find_elements_by_xpath("//button[contains(text(), 'okay, got it')]")
        driver.execute_script("arguments[0].click();", cookiesbtnHTML[0])
    except:
        pass
    
    
    data = None
    pageNumber=1
    
    while True:
        
        GUIChangeStatus(urlInfo+' Page: '+str(pageNumber))
        
        wait_visibility_element(driver,"//div[contains(@class,'link-to-irp')]/div")
        data = CollectContentPage(data,driver)
        nxtbtnHTML = driver.find_elements_by_xpath("//div[@id='pager']//button[contains(text(), '>')]")
        if (len(nxtbtnHTML)<=0):
            break
        driver.execute_script("arguments[0].click();", nxtbtnHTML[0])
        pageNumber += 1
    
    data = ProcessData(data)
        
    CreateFile(urlPage,[data,None],driver)
    
    driver.quit()
    return

def main():
    
    global urlPages,outputFolder
    
    urlPages,settings = GUI('AthLinks')
    
    outputFolder = settings['Path']
    
    lenurls = len(urlPages)
    if lenurls>0:
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("headless")
        #chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--log-level=3')
        driver = webdriver.Chrome(options=chrome_options)
        driver.minimize_window()
    
    for i,urlPage in enumerate(urlPages):
        urlInfo = 'URL: '+urlPage
        initialTime = int(time.time())
        while True:
            try:
                PageScrapping(driver,urlInfo,urlPage)
                break
            except:
                if int(time.time())-initialTime>30:
                    GUIChangeError(urlInfo+'\n Runtime Error - 186')
                    driver.quit()
                    GUIKill()
        
    if lenurls>0:
        driver.quit()
  
    GUIKill()
    return
        
if __name__ == '__main__':
    main()
