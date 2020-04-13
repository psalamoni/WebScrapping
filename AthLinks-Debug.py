#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:52:20 2020

@author: Pedro Salamoni
"""

from WebScrapping import GUI,GUIKill
from AthLinks import PageScrapping

def main():
    from selenium import webdriver
    
    global urlPages,outputFolder
    
    urlPages,settings = GUI('AthLinks')
    
    outputFolder = settings['Path']
    
    lenurls = len(urlPages)
    if lenurls>0:
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("headless")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument('--log-level=3')
        driver = webdriver.Chrome(options=chrome_options)
    
    for i,urlPage in enumerate(urlPages):
        urlInfo = 'URL: '+urlPage
        PageScrapping(driver,urlInfo,urlPage)
        
    if lenurls>0:
        driver.quit()
  
    GUIKill()
    return
        
if __name__ == '__main__':
    main()