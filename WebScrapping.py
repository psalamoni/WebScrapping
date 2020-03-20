#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:17:07 2020

@author: setup
"""

"""
Created on Thu Mar  5 15:29:20 2020

@author: Pedro Salamoni
"""

# import libraries
from selenium import webdriver
import pandas as pd

def CollectData(urlpage):
    driver = webdriver.Chrome()
    driver.get(urlpage)
    
    return driver

def CollectTable(driver,xpath):
    tableHTML = driver.find_elements_by_xpath(xpath)
    
    return tableHTML

def TableToData(tableHTML):
    data = pd.read_html(tableHTML)
    
    return data

def CreateFinalFile(fileName,data,fileContent):
    import pandas as pd
    from tabulate import tabulate
    
    if data[1] is not None:
        data = pd.concat([data[0].reset_index().drop(columns=['index']),data[1].reset_index().drop(columns=['index'])], axis=1, sort=False)
    else:
        data = data[0]
    
    fileContent += tabulate(data, headers='keys', tablefmt='rst', showindex=False)
    fileContent = fileContent[:fileContent.rfind('\n')]
    
    file = open(fileName,"w")
    file.write(fileContent)