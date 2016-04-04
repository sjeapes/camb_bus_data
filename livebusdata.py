# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 21:27:23 2014

@author: sjeapes
"""

import urllib2
from bs4 import BeautifulSoup

def parseBuses(ID):
    baseUrl = 'http://www.cambridgeshirebus.info//Popup_Content/WebDisplay/WebDisplay.aspx?stopRef='
    url = baseUrl + ID    
    response = urllib2.urlopen(url)
    html = response.read()

    soup = BeautifulSoup(html, "lxml")
    
    print soup.find("span", id="stopTitle").string
    
    rows = soup.find_all("tr")
    numBuses = len(rows)   
    
    buses = []    
    
    for i in range(2,numBuses):
        busData = dict()
        busData['Number'] = rows[i].find("td", class_="gridServiceItem").string
        busData['Destination'] = rows[i].find("td", class_="gridDestinationItem").string
        busData['ETA'] = rows[i].find("td", class_="gridTimeItem").string
        
        if busData['ETA'][2] == ':':
            timeMod = 'at'
        else:
            timeMod = 'in'
            
        buses.append(busData)
        print busData['Number'] + ' to ' + busData['Destination'] + ' is expected ' + timeMod + ' ' + busData['ETA']
    
    # print '\n'
    return buses


#stopIDs = ['0500CCITY008','0500CCITY496']
stopIDs = ['0500CCITY008']

busTimes = []
for code in stopIDs:
    busTimes.extend(parseBuses(code))
