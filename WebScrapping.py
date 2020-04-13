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

urlPages = []
settings = {'Path':''}

window = None

frame = {}


currentButton = None
statusStatus = None
errorStatus = None

def GUIKill():
    import sys
    
    global window,statusStatus
    
    statusStatus['text'] = 'FINISHED'
    window.mainloop()
    sys.exit()

def GUIChangeStatus(status):
    global window,statusStatus
    
    statusStatus['text'] = status
    window.update_idletasks()
    window.update()
    
def GUIChangeError(error):
    global window,errorStatus
    
    errorStatus['text'] = error
    window.update_idletasks()
    window.update()

def GUISelectFolder(entryPath):
    import tkinter as tk
    from tkinter import filedialog
    
    global window
    
    window.directory = filedialog.askdirectory()
    window.directory = window.directory + '/'
    
    entryPath.delete(0, tk.END)
    entryPath.insert(0,window.directory)
    
    settings['Path'] = entryPath.get()


def GUIURLs(urlButton):
    import tkinter as tk
    
    global frame,currentButton
    
    frame['current'].pack_forget()
    frame['current'] = frame['url']
    frame['current'].pack()
    
    currentButton['state'] = tk.ACTIVE
    currentButton['relief'] = tk.RAISED
    currentButton = urlButton
    currentButton['state'] = tk.DISABLED
    currentButton['relief'] = tk.SUNKEN

def GUISettings(settingButton):
    import tkinter as tk
    
    global frame,currentButton
    
    frame['current'].pack_forget()
    frame['current'] = frame['setting']
    frame['current'].pack()
    
    currentButton['state'] = tk.ACTIVE
    currentButton['relief'] = tk.RAISED
    currentButton = settingButton
    currentButton['state'] = tk.DISABLED
    currentButton['relief'] = tk.SUNKEN

def GUIRun(entries,entryPath):
    from tkinter import messagebox
    
    global frame,urlPages,window
    
    settings['Path'] = entryPath.get()
    
    if settings['Path'] == '':
        messagebox.showwarning(title='Warning!', message='You have to select the output folder')
        return
    
    for entry in entries:
        if entry.get() == '':
            next
        else:
            urlPages.append(entry.get())
        
    frame['option'].pack_forget()
    frame['run'].pack_forget()
    frame['current'].pack_forget()
    frame['current'] = frame['status']
    frame['current'].pack()
    
    window.update_idletasks()
    window.update()    
    window.quit()
    
    return
    

def GUIAddEntry(row,entry,moreButton,i):
    import tkinter as tk
    
    global frame
            
    i += 1
    
    row.append(tk.Frame(frame['entry'], bd=2))
    row[i].pack()
    
    entry.append(tk.Entry(row[i], width=80))
    entry[i].pack(side=tk.LEFT)
    
    wEFSpace = tk.Label(row[i], text="", width=1)
    wEFSpace.pack(side=tk.LEFT)
    
    moreButton[i-1]['state'] = tk.DISABLED
    moreButton.append(tk.Button(row[i], text="+", command=lambda: GUIAddEntry(row,entry,moreButton,i)))
    moreButton[i].pack(side=tk.LEFT)
    
    if i > 8:
        moreButton[i]['state'] = tk.DISABLED
    
    return

def GUI(siteName):
    import tkinter as tk
    
    global window,frame,currentButton,settings,statusStatus,errorStatus
    
    try:
        fset = open('settings',"r")
        settings = eval(fset.read())
        fset.close()
    except:
        pass
    
    window = tk.Tk()
    window.title("ScrapeIt")
    
    #Main Frames
    frame.update({'selected': tk.Frame(window, width=70, bd=4)})
    frame['selected'].pack()
    
    frame.update({'option': tk.Frame(window, bd=4)})
    frame['option'].pack()
    
    frame.update({'run': tk.Frame(window, bd=4)})
    frame['run'].pack()
    
    
    
    
    #Selected Frame
    frame.update({'url': tk.Frame(frame['selected'], bd=4)})
    frame['url'].pack()
    
    frame.update({'current': frame['url']})
    
    frame.update({'setting': tk.Frame(frame['selected'], bd=4)})
    
    frame.update({'status': tk.Frame(frame['selected'], bd=5)})
    
    #Option Frame
    urlButton = tk.Button(frame['option'], text="URLs", relief=tk.SUNKEN, state=tk.DISABLED, command=lambda: GUIURLs(urlButton))    
    urlButton.pack(side=tk.LEFT)
    
    currentButton = urlButton
    
    wOFSpace = tk.Label(frame['option'], text="", width=1)
    wOFSpace.pack(side=tk.LEFT)
    
    settingButton = tk.Button(frame['option'], text="Settings", command=lambda: GUISettings(settingButton))    
    settingButton.pack(side=tk.LEFT)
    
    #Run Frame
    runButton = tk.Button(frame['run'], text="Run!", command=lambda: GUIRun(entry,entryPath))    
    runButton.pack(side=tk.LEFT)
    
    
    
    
    #Url Frames
    frame.update({'title': tk.Frame(frame['url'], bd=4)})
    frame['title'].pack()
    
    frame.update({'entry': tk.Frame(frame['url'], bd=2)})
    frame['entry'].pack()
    
    #Settings Frame
    frame.update({'titleSetting': tk.Frame(frame['setting'], bd=4)})
    frame['titleSetting'].pack()
    
    frame.update({'entrySetting': tk.Frame(frame['setting'], bd=2)})
    frame['entrySetting'].pack()
    
    #Status Frame
    frame.update({'titleStatus': tk.Frame(frame['status'], bd=4)})
    frame['titleStatus'].pack()
    
    frame.update({'statusStatus': tk.Frame(frame['status'], bd=20)})
    frame['statusStatus'].pack()
        
    
    
    
    #frame['title']
    label = tk.Label(frame['title'], text=("Urls - "+siteName), width="75")
    label.pack()    
    
    #frame['entry']
    i=0
    row = []
    row.append(tk.Frame(frame['entry'], bd=2))
    row[i].pack()
    
    #Entry Row Frame
    entry = []
    entry.append(tk.Entry(row[i], width=80, bd=2))
    entry[i].pack(side=tk.LEFT)
    
    wEFSpace = tk.Label(row[i], text="", width=1)
    wEFSpace.pack(side=tk.LEFT)
    
    moreButton = []
    moreButton.append(tk.Button(row[i], text="+", command=lambda: GUIAddEntry(row,entry,moreButton,i)))
    moreButton[i].pack(side=tk.LEFT)
    
    
    
    #title Setting Frame
    labelSetting = tk.Label(frame['titleSetting'], text=("Settings - "+siteName), width="75")
    labelSetting.pack()
    
    #Entry Setting Frame
    labelEntry = tk.Label(frame['entrySetting'], text="Output Directory: ")
    labelEntry.pack(side=tk.LEFT)
    
    entryPath = tk.Entry(frame['entrySetting'], width=65, bd=2)
    entryPath.pack(side=tk.LEFT)
    entryPath.insert(0,settings['Path'])
    
    wEFSpace = tk.Label(frame['entrySetting'], text="", width=1)
    wEFSpace.pack(side=tk.LEFT)

    findButton = tk.Button(frame['entrySetting'], text="+", command=lambda: GUISelectFolder(entryPath))
    findButton.pack(side=tk.LEFT)
    
    
    
    
    #title Status Frame
    labelStatus = tk.Label(frame['titleStatus'], text=("STATUS - "+siteName), width="65")
    labelStatus.pack()
    
    #status Status Frame
    statusStatus = tk.Label(frame['statusStatus'], text="Initializing...")
    statusStatus.pack()
    
    #error Status Frame
    errorStatus = tk.Label(frame['statusStatus'], text="", fg="red")
    errorStatus.pack()
    
    
    window.mainloop()
    
    fset = open('settings',"w")
    fset.write(str(settings))
    fset.close()
    
    return urlPages,settings

def CollectData(driver,urlpage):
    driver.get(urlpage)
    
    return driver

def CollectTable(driver,xpath):
    tableHTML = driver.find_elements_by_xpath(xpath)
    
    return tableHTML

def TableToData(tableHTML):
    import pandas as pd
    
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
    
    fileContent = fileContent.replace('nan','   ')
    
    file = open(fileName,"w")
    file.write(fileContent)
    
def wait_clickability_element(driver,element_name):
    from selenium.webdriver.support import ui
    import selenium.webdriver.support.expected_conditions as EC
    from selenium.webdriver.common.by import By
    
    ui.WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, element_name)))
    
    
    