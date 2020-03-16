#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# specify urls
urlPages = ['https://www.athlinks.com/event/34627/results/Event/257173/Course/363224/Results','https://www.athlinks.com/event/207930/results/Event/176340/Course/1022122/Results','https://www.athlinks.com/event/207930/results/Event/176340/Course/1022117/Results','https://www.athlinks.com/event/207930/results/Event/176340/Course/1022116/Results ','https://www.athlinks.com/event/207930/results/Event/176340/Course/243690/Results','https://www.athlinks.com/event/213853/results/Event/668372/Course/1120242/Results','https://www.athlinks.com/event/213853/results/Event/668372/Course/1120051/Results','https://www.athlinks.com/event/213853/results/Event/751605/Course/1266989/Results','https://www.athlinks.com/event/213853/results/Event/751605/Course/1266986/Results','https://www.athlinks.com/event/213853/results/Event/870081/Course/1646240/Results','https://www.athlinks.com/event/213853/results/Event/870081/Course/1646210/Results']

# Specify the sleep time
sleepTime = 2

# Specify aimed data
outerAimedData = ['BIB','NAME','AGE','OVERALL','GENDER','CITY','COUNTRY','DIVISION','PACE','TIME']

# Specify data to be renamed
oldColumnName = ['GENDER']
newColumnName = ['GENDER PLACE']

# Specify output folder
outputFolder = "/home/setup/Documents/roadraceresults/Results/Unsent Results/AthLinks/"

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
from selenium.webdriver.chrome.options import Options
import time
import re

#import pandas as pd
#import urllib.request
#from bs4 import BeautifulSoup


def CollectData(urlpage):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(urlpage)
    time.sleep(6)
    
    cookiesbtnHTML = driver.find_elements_by_xpath("//button[contains(text(), 'okay, got it')]")
    cookiesbtnHTML[0].click()
    
    return driver

def CollectOuterHeader(driver):
    columnsHTML = driver.find_elements_by_xpath("//div[@class='row mx-0']/div")
    data = []
    for columnHTML in columnsHTML:
        column = []
        column.append(columnHTML.text)
        data.append(column)
    data.pop(0)
    data = [['']] + data + [['']]
        
    return data

def CollectOuterData(data,driver):
    results = driver.find_elements_by_xpath("//div[contains(@class,'link-to-irp')]/div")
    
    if data is None:
        data = CollectOuterHeader(driver)
    num_columns = len(data)
    
    for i,result in enumerate(results):
        try:
            data[i%num_columns].append(result.text)
        except:
            print("Something went wrong, contact Pedro Salamoni [1]")
                
    return data

def CollectContentPage(data,driver):
    outerData = CollectOuterData(data[0],driver)
    return [outerData,None]

def ProcessData(bulkData):
    data = [[],[]]
    
    bulkData.pop()
    
    dataadd = [['NAME'],['AGE'],['BIB'],['CITY'],['COUNTRY']]
    
    for column in bulkData[0][0][1:]:
        [bulk,name,age,bib,country] = re.split('\n',column)
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
        
    bulkData[0].pop(0)
    bulkData[0] = dataadd + bulkData[0]
        
    for column in bulkData[0]:
        if ((column[0] in outerAimedData) or (re.match(r"\d+:\d+:\d+(\.\d+)*", column[1]))):
            try:
                column[0] = newColumnName[oldColumnName.index(column[0])]
                data[0].append(column)
            except:
                data[0].append(column)
            
    return data

def CreateFile(urlPage,data,driver):
    raceTitleHTML = driver.find_elements_by_xpath("//h1[@id='master-event-name']")
    raceTitle = raceTitleHTML[0].text
    
    raceDateTypeHTML = driver.find_elements_by_xpath("//div[@id='total-results-string']/preceding-sibling::div[1]")
    raceDate = '_' + raceDateTypeHTML[0].text
    
    fileContent = urlPage + '\n' + raceTitle + '\nline 1\nline 2\nline 3\nline 4\n'
    maxlenout = []
    
    #Write equals
    for i in range(len(data[0])):
        maxlenout.append(len(max(data[0][i], key=len))) 
        fileContent += '='*maxlenout[i]
        fileContent += ' '
    
    fileContent += '\n'
    
    #Write Headings
    for i in range(len(data[0])):
        newContent = str(data[0][i].pop(0))
        fileContent += newContent
        fileContent += ' '*(maxlenout[i]-len(newContent))
        fileContent += ' '
        
    fileContent += '\n'
        
    #Write equals
    for i in range(len(data[0])):
        fileContent += '='*maxlenout[i]
        fileContent += ' '
    
    fileContent += '\n'
    
    #Write data
    for _ in range(len(data[0][0])):
        for i in range(len(data[0])):
            newContent = str(data[0][i].pop(0))
            newContent = newContent.replace('\n',' ')
            newContent = newContent.replace('Bib ','')
            newContent = newContent.replace(' min/mi','')
            fileContent += newContent
            fileContent += ' '*(maxlenout[i]-len(newContent))
            fileContent += ' '
            
        fileContent += '\n'
      
    fileName = outputFolder + raceTitle + raceDate + ".txt"
    
    file = open(fileName,"w")
    
    file.write(fileContent)
            

def PageScrapping(urlPage):
    driver = CollectData(urlPage)
    data = [None,None]
    pageNumber=1
    
    while True:
        print('Page:',pageNumber)
        data = CollectContentPage(data,driver)
        nxtbtnHTML = driver.find_elements_by_xpath("//div[@id='pager']//button[contains(text(), '>')]")
        if (len(nxtbtnHTML)<=0):
            break
        nxtbtnHTML[0].click()
        pageNumber += 1
        time.sleep(sleepTime)
    
    data = ProcessData(data)
        
    CreateFile(urlPage,data,driver)
    
    driver.quit()
    return

def main():
    for urlPage in urlPages:
        print(urlPage)
        PageScrapping(urlPage)
        
main()
