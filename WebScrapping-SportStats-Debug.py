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
from WebScrapping import CollectData,CollectTable,TableToData,CreateFinalFile,GUI,GUIKill,GUIChangeStatus,GUIChangeError
from WebScrapping-SportStats import CollectInnerData, CollectContentPage, ProcessData, CreateFile, PageScrapping

def main():
    from selenium import webdriver
    
    global urlPages,outputFolder
    
    urlPages,settings = GUI('SportStats')
    
    outputFolder = settings['Path']
    
    lenurls = len(urlPages)
    if lenurls>0:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        chrome_options.add_argument('--log-level=3')
        driver = webdriver.Chrome(options=chrome_options)
    
    for i,urlPage in enumerate(urlPages):
        urlInfo = 'URL: '+urlPage
        PageScrapping(driver,urlInfo,urlPage)
        
    if lenurls>0:
        driver.quit()
        
    GUIKill()
    return

main()
