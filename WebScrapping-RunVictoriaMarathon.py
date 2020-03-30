#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# specify urls
paths = ['/home/setup/Documents/roadraceresults/Trainning/1986-RVM-Results.pdf','/home/setup/Documents/roadraceresults/Trainning/1988-RVM-Results.pdf','/home/setup/Documents/roadraceresults/Trainning/1990-RVM-Results.pdf','/home/setup/Documents/roadraceresults/Trainning/Victoria-8K-1989-Results.pdf']
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
# =============================================================================
# from WebScrapping import CollectData,CollectTable,TableToData,CreateFinalFile
# import time
# import re
# 
# =============================================================================
def CollectText(path):
    import PyPDF2
    from tabula import read_pdf
    
    df = read_pdf(path)

    # Open the pdf file in read binary mode.
    fileObject = open(path, 'rb')

    # Create a pdf reader .
    pdfFileReader = PyPDF2.PdfFileReader(fileObject)

    # Get total pdf page number.
    totalPageNumber = pdfFileReader.numPages

    # Print pdf total page number.
    print('This pdf file contains totally ' + str(totalPageNumber) + ' pages.')

    currentPageNumber = 0
    text = ''

    # Loop in all the pdf pages.
    while(currentPageNumber < totalPageNumber ):

        # Get the specified pdf page object.
        pdfPage = pdfFileReader.getPage(currentPageNumber)

        # Get pdf page text.
        text = text + pdfPage.extractText()

        # Process next page.
        currentPageNumber += 1
    
    print (df)
    return df

def main():
    text = []
    #lenPaths = len(paths)
    for i,path in enumerate(paths):
        print(path)
        text.append(CollectText(path))
        
    return text

text = main()
