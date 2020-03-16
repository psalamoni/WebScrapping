#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# specify urls
urlPages = ['https://www.sportstats.ca/display-results.xhtml?raceid=103754']
urlPages1 = ['https://www.sportstats.ca/display-results.xhtml?raceid=11282','https://www.sportstats.ca/display-results.xhtml?raceid=11272','https://www.sportstats.ca/display-results.xhtml?raceid=11282','https://www.sportstats.ca/display-results.xhtml?raceid=11275','https://www.sportstats.ca/display-results.xhtml?raceid=11277','https://www.sportstats.ca/display-results.xhtml?raceid=11281','https://www.sportstats.ca/display-results.xhtml?raceid=8396','https://www.sportstats.ca/display-results.xhtml?raceid=8400','https://www.sportstats.ca/display-results.xhtml?raceid=8385','https://www.sportstats.ca/display-results.xhtml?raceid=8386','https://www.sportstats.ca/display-results.xhtml?raceid=8390','https://www.sportstats.ca/display-results.xhtml?raceid=8389','https://www.sportstats.ca/display-results.xhtml?raceid=8388','https://www.sportstats.ca/display-results.xhtml?raceid=8391','https://www.sportstats.ca/display-results.xhtml?raceid=8401','https://www.sportstats.ca/display-results.xhtml?raceid=16775','https://www.sportstats.ca/display-results.xhtml?raceid=30915','https://www.sportstats.ca/display-results.xhtml?raceid=30913','https://www.sportstats.ca/display-results.xhtml?raceid=30917','https://www.sportstats.ca/display-results.xhtml?raceid=13080','https://www.sportstats.ca/display-results.xhtml?raceid=13081','https://www.sportstats.ca/display-results.xhtml?raceid=13082','https://www.sportstats.ca/display-results.xhtml?raceid=13084','https://www.sportstats.ca/display-results.xhtml?raceid=13086','https://www.sportstats.ca/display-results.xhtml?raceid=13087','https://www.sportstats.ca/display-results.xhtml?raceid=2067','https://www.sportstats.ca/display-results.xhtml?raceid=20201','https://www.sportstats.ca/display-results.xhtml?raceid=15999','https://www.sportstats.ca/display-results.xhtml?raceid=16775','https://www.sportstats.ca/display-results.xhtml?raceid=16776','https://www.sportstats.ca/display-results.xhtml?raceid=16776','https://www.sportstats.ca/display-results.xhtml?raceid=20047','https://www.sportstats.ca/display-results.xhtml?raceid=20288','http://raceresults.sportstats.ca/display-results.xhtml?raceid=101937','http://raceresults.sportstats.ca/display-results.xhtml?raceid=101938','http://raceresults.sportstats.ca/display-results.xhtml?raceid=101935','https://www.sportstats.ca/display-results.xhtml?raceid=39476','https://www.sportstats.ca/display-results.xhtml?raceid=39667','https://www.sportstats.ca/display-results.xhtml?raceid=39668','https://www.sportstats.ca/display-results.xhtml?raceid=39669','https://www.sportstats.ca/display-results.xhtml?raceid=39670','https://www.sportstats.ca/display-results.xhtml?raceid=101645','https://www.sportstats.ca/display-results.xhtml?raceid=101481','https://www.sportstats.ca/display-results.xhtml?raceid=94160','https://www.sportstats.ca/display-results.xhtml?raceid=3564','https://www.sportstats.ca/display-results.xhtml?raceid=3565','https://www.sportstats.ca/display-results.xhtml?raceid=3563','https://www.sportstats.ca/display-results.xhtml?raceid=3349','https://www.sportstats.ca/display-results.xhtml?raceid=3347','https://www.sportstats.ca/display-results.xhtml?raceid=3348','https://www.sportstats.ca/display-results.xhtml?raceid=5623','https://www.sportstats.ca/display-results.xhtml?raceid=5625','https://www.sportstats.ca/display-results.xhtml?raceid=5626','https://www.sportstats.ca/display-results.xhtml?raceid=5624','https://www.sportstats.ca/display-results.xhtml?raceid=6101','https://www.sportstats.ca/display-results.xhtml?raceid=6102','https://www.sportstats.ca/display-results.xhtml?raceid=6104','https://www.sportstats.ca/display-results.xhtml?raceid=6106','https://www.sportstats.ca/display-results.xhtml?raceid=6065','https://www.sportstats.ca/display-results.xhtml?raceid=6066','https://www.sportstats.ca/display-results.xhtml?raceid=6069','https://www.sportstats.ca/display-results.xhtml?raceid=6071','https://www.sportstats.ca/display-results.xhtml?raceid=5131','https://www.sportstats.ca/display-results.xhtml?raceid=5132','https://www.sportstats.ca/display-results.xhtml?raceid=5133','https://www.sportstats.ca/display-results.xhtml?raceid=5134','https://www.sportstats.ca/display-results.xhtml?raceid=2470','https://www.sportstats.ca/display-results.xhtml?raceid=2473','https://www.sportstats.ca/display-results.xhtml?raceid=2424','https://www.sportstats.ca/display-results.xhtml?raceid=2456','https://www.sportstats.ca/display-results.xhtml?raceid=2457','https://www.sportstats.ca/display-results.xhtml?raceid=2459','https://www.sportstats.ca/display-results.xhtml?raceid=2462','https://www.sportstats.ca/display-results.xhtml?raceid=2436','https://www.sportstats.ca/display-results.xhtml?raceid=2437','https://www.sportstats.ca/display-results.xhtml?raceid=2439','https://www.sportstats.ca/display-results.xhtml?raceid=2442','https://www.sportstats.ca/display-results.xhtml?raceid=2419','https://www.sportstats.ca/display-results.xhtml?raceid=2422','https://www.sportstats.ca/display-results.xhtml?raceid=2420','https://www.sportstats.ca/display-results.xhtml?raceid=2424','https://www.sportstats.ca/display-results.xhtml?raceid=2764','https://www.sportstats.ca/display-results.xhtml?raceid=2767','https://www.sportstats.ca/display-results.xhtml?raceid=2770','https://www.sportstats.ca/display-results.xhtml?raceid=2765','https://www.sportstats.ca/display-results.xhtml?raceid=2757','https://www.sportstats.ca/display-results.xhtml?raceid=2758','https://www.sportstats.ca/display-results.xhtml?raceid=2760','https://www.sportstats.ca/display-results.xhtml?raceid=2740','https://www.sportstats.ca/display-results.xhtml?raceid=2741','https://www.sportstats.ca/display-results.xhtml?raceid=2742','https://www.sportstats.ca/display-results.xhtml?raceid=19536','https://www.sportstats.ca/display-results.xhtml?raceid=30964','https://www.sportstats.ca/display-results.xhtml?raceid=30965','https://www.sportstats.ca/display-results.xhtml?raceid=30966','https://www.sportstats.ca/display-results.xhtml?raceid=39166','https://www.sportstats.ca/display-results.xhtml?raceid=37053','https://www.sportstats.ca/display-results.xhtml?raceid=37055','https://www.sportstats.ca/display-results.xhtml?raceid=37060','https://www.sportstats.ca/display-results.xhtml?raceid=37058','https://www.sportstats.ca/display-results.xhtml?raceid=37062','https://www.sportstats.ca/display-results.xhtml?raceid=37045','https://www.sportstats.ca/display-results.xhtml?raceid=108456','https://www.sportstats.ca/display-results.xhtml?raceid=100477','https://www.sportstats.ca/display-results.xhtml?raceid=100478','https://www.sportstats.ca/display-results.xhtml?raceid=100480','https://www.sportstats.ca/display-results.xhtml?raceid=100479','https://www.sportstats.ca/display-results.xhtml?raceid=100481','https://www.sportstats.ca/display-results.xhtml?raceid=100482','https://www.sportstats.ca/display-results.xhtml?raceid=100483','https://www.sportstats.ca/display-results.xhtml?raceid=100484','https://www.sportstats.ca/display-results.xhtml?raceid=100485','https://www.sportstats.ca/display-results.xhtml?raceid=93033','https://www.sportstats.ca/display-results.xhtml?raceid=93034','https://www.sportstats.ca/display-results.xhtml?raceid=93036','https://www.sportstats.ca/display-results.xhtml?raceid=93035','https://www.sportstats.ca/display-results.xhtml?raceid=93037','https://www.sportstats.ca/display-results.xhtml?raceid=93038','https://www.sportstats.ca/display-results.xhtml?raceid=93039','https://www.sportstats.ca/display-results.xhtml?raceid=93040','https://www.sportstats.ca/display-results.xhtml?raceid=93041','https://www.sportstats.ca/display-results.xhtml?raceid=44193','https://www.sportstats.ca/display-results.xhtml?raceid=44191','https://www.sportstats.ca/display-results.xhtml?raceid=44190','https://www.sportstats.ca/display-results.xhtml?raceid=44192','https://www.sportstats.ca/display-results.xhtml?raceid=44194','https://www.sportstats.ca/display-results.xhtml?raceid=44195','https://www.sportstats.ca/display-results.xhtml?raceid=44196','https://www.sportstats.ca/display-results.xhtml?raceid=44197','https://www.sportstats.ca/display-results.xhtml?raceid=44198','https://www.sportstats.ca/display-results.xhtml?raceid=109569','https://www.sportstats.ca/display-results.xhtml?raceid=108710','https://www.sportstats.ca/display-results.xhtml?raceid=108709']

# Specify the sleep time
sleepTime = 1.5 

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
from selenium import webdriver
import time
import re
#import pandas as pd
#import urllib.request
#from bs4 import BeautifulSoup


def CollectData(urlpage):
    driver = webdriver.Chrome()
    driver.get(urlpage)
    
    return driver

def CollectOuterHeader(driver):
    columnsHTML = driver.find_elements_by_xpath("//div[@id='main']//th[@role='columnheader']")
    data = []
    for columnHTML in columnsHTML:
        column = []
        column.append(columnHTML.text)
        data.append(column)
        
    return data

def CollectInnerHeader(driver):
    
    columnsHTML = driver.find_elements_by_xpath("//div[@id='athlete-content']//tr/td[1]")
    data = [['NAME']]
    for columnHTML in columnsHTML:
        column = []
        column.append(columnHTML.text)
        data.append(column)
        
    return data

def CollectOuterData(data,driver):
    results = driver.find_elements_by_xpath("//tr[@role='row']//td")
    if data is None:
        data = CollectOuterHeader(driver)
    num_columns = len(data)
    for i,result in enumerate(results):
        try:
            data[i%num_columns].append(result.text)
        except:
            print("Something went wrong, contact Pedro Salamoni [Index Name Error][1]")
    
    return data

def CollectInnerData(data,driver):
    namesHTML = driver.find_elements_by_xpath("//tr[@role='row']//td[4]//a")
    void = 0
    for i,nameHTML in enumerate(namesHTML):
        try:
            nameHTML.click()
            time.sleep(sleepTime)
        except:
            if data is None:
                void += 1
            else:
                data[0].append(nameHTML.text)
                num_columns = len(data)-1
                for i in range(num_columns):
                    data[i+1].append('')
        else:
            if data is None:
                data = CollectInnerHeader(driver)
                if void != 0:
                    for _ in range(void):
                        data[0].append('')
                        num_columns = len(data)-1
                        for i in range(num_columns):
                            data[i+1].append('')
                            
            data[0].append(nameHTML.text)
                
            results = driver.find_elements_by_xpath("//div[@id='athlete-content']//tr/td[2]")
            num_columns = len(data)-1
            
            for i,result in enumerate(results):
                try:
                    data[i%num_columns+1].append(result.text)
                except:
                    print("Something went wrong, contact Pedro Salamoni [Data Colect Error][2]")

    return data

def CollectContentPage(data,driver):
    outerData = CollectOuterData(data[0],driver)
    innerData = CollectInnerData(data[1],driver)
    return [outerData,innerData]

def ProcessData(bulkData):
    data = [[],[]]
    
    for column in bulkData[0]:
        if (column[0] in outerAimedData) or (re.match(r"\d+:\d+:\d+(\.\d+)*", column[1])):
            try:
                column[0] = newColumnName[oldColumnName.index(column[0])]
                data[0].append(column)
            except:
                data[0].append(column)
    
    for column in bulkData[1]:
        if column[0] in innerAimedData:
            try:
                column[0] = newColumnName[oldColumnName.index(column[0])]
                data[1].append(column)
            except:
                data[0].append(column)
            
    return data

def CreateFile(urlPage,data,driver):
    raceTitleHTML = driver.find_elements_by_xpath("//div[@id='main']//h1[1]")
    raceTitle = raceTitleHTML[0].text
    
    raceDateTypeHTML = driver.find_elements_by_xpath("//div[@id='main']//p[1]")
    try:
        [raceDate,raceType] = re.split(r"•", raceDateTypeHTML[0].text)
    except:
        print("Something went wrong, contact Pedro Salamoni [Descriptions Pattern Error][3]")
    
    fileContent = urlPage + '\n' + raceTitle + '\n' + raceDateTypeHTML[0].text + '\n\nline 1\nline 2\nline 3\nline 4\n'
    maxlenout = []
    maxlenin = []
    
    #Write equals
    for i in range(len(data[0])):
        maxlenout.append(len(max(data[0][i], key=len))) 
        fileContent += '='*maxlenout[i]
        fileContent += ' '
    
    for i in range(len(data[1])):
        maxlenin.append(len(max(data[1][i], key=len))) 
        fileContent += '='*maxlenin[i]
        fileContent += ' '
    
    fileContent += '\n'
    
    #Write Headings
    for i in range(len(data[0])):
        newContent = str(data[0][i].pop(0))
        fileContent += newContent
        fileContent += ' '*(maxlenout[i]-len(newContent))
        fileContent += ' '
        
    for i in range(len(data[1])):
        newContent = str(data[1][i].pop(0))
        fileContent += newContent
        fileContent += ' '*(maxlenin[i]-len(newContent))
        fileContent += ' '
        
    fileContent += '\n'
        
    #Write equals
    for i in range(len(data[0])):
        fileContent += '='*maxlenout[i]
        fileContent += ' '
        
    for i in range(len(data[1])):
        fileContent += '='*maxlenin[i]
        fileContent += ' '
    
    fileContent += '\n'
    
    #Write data
    for _ in range(len(data[0][0])):
        for i in range(len(data[0])):
            newContent = str(data[0][i].pop(0))
            fileContent += newContent
            fileContent += ' '*(maxlenout[i]-len(newContent))
            fileContent += ' '
    
        for i in range(len(data[1])):
            newContent = str(data[1][i].pop(0))
            fileContent += newContent
            fileContent += ' '*(maxlenin[i]-len(newContent))
            fileContent += ' '
            
        fileContent += '\n'
        
    fileString = raceTitle + "_" + raceDate + "_" + raceType
    fileString = fileString.replace('/', '-')
      
    fileName = outputFolder + fileString + ".txt"
    
    file = open(fileName,"w")
    
    file.write(fileContent)
            

def PageScrapping(urlPage):
    driver = CollectData(urlPage)
    data = [None,None]
    pageNumber=1
    
    # Loop to identify where should the script go for another page
    while (len(driver.find_elements_by_xpath("//tr[@role='row']//td[4]//a"))>0):
        print('Page:',pageNumber)
        data = CollectContentPage(data,driver)
        nxtbtnHTML = driver.find_elements_by_xpath("//div[@id='mainForm:pageNav']//a[contains(@class, 'fa-angle-right')]")
        if len(nxtbtnHTML)>0:
            nxtbtnHTML[0].click()
            pageNumber += 1
            time.sleep(1)
        else:
            break
    
    data = ProcessData(data)
        
    CreateFile(urlPage,data,driver)
    
    driver.quit()

def main():
    data = []
    for urlPage in urlPages:
        print(urlPage)
        data = PageScrapping(urlPage)
    return

main()
