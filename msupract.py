from http.client import responses

import requests
import pandas
from bs4 import BeautifulSoup

from another_try import strip_update, ultima_strip_update, strip_level
from basepract import check_exists_by_xpath, pars_mephi

def pars_msu():
    url = "https://pk.cs.msu.ru/privilege"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    block = soup.find_all('table' , style = "border-collapse:collapse")[0].find('tbody').find_all('tr')
    a=dict()
    s=str()
    for row in block:
        rowy = row.find_all('td')
        if(len(rowy)==6):
            s=rowy[1].text
            a[rowy[1].text]=[['математика' , rowy[3].text , rowy[4].text]]
        elif(len(rowy)==3):
            a[s].append(['математика' , rowy[0].text , rowy[1].text])

    block = soup.find_all('table', style="border-collapse:collapse")[1].find('tbody').find_all('tr')
    for row in block:
        rowy = row.find_all('td')
        if(len(rowy)==6):
            s=rowy[1].text
            if(s in a):
                a[s].append(['информатика' ,rowy[3].text , rowy[4].text])
            else:
                a[s]=[['информатика' ,rowy[3].text , rowy[4].text]]
        elif(len(rowy)==3):
            a[s].append(['информатика' ,rowy[0].text , rowy[1].text])
    block = soup.find_all('table', style="border-collapse:collapse")[2].find('tbody').find_all('tr')
    for row in block:
        rowy = row.find_all('td')
        if (len(rowy) == 6):
            s = rowy[1].text
            if (s in a):
                a[s].append(['физика', rowy[3].text, rowy[4].text])
            else:
                a[s] = [['физика', rowy[3].text, rowy[4].text]]
        elif (len(rowy) == 3):
            a[s].append(['физика', rowy[0].text, rowy[1].text])
    return a


def check_for_msu(msu:dict , spis:list):
    ans=list()
    print(spis)
    for i in spis:
        if (i[0] in msu):
            for j in msu[i[0]]:
                if(j[0] ==i[1]):
                    ans.append([i[0] , j[1] , j[2]])
    return ans
