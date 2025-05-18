from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests
import pandas
from bs4 import BeautifulSoup

from another_try import strip_update, ultima_strip_update, strip_level
from basepract import check_exists_by_xpath, pars_mephi


def pars_mfti():
    url = "https://pk.mipt.ru/bachelor/2023_olympiads/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    block=soup.find_all("table" , class_="table table-responsive table-bordered table-hover")[1].find_all_next("tr")
    lis=list()
    for i in block:
        s = (i.text)
        s=ultima_strip_update(s)
        if len(s) > 3 and s[0].isdigit() == 1:
            s=s.split('  ')
            print(s[1].strip())
            lis.append([s[1].strip() ,"математика"])
    block = soup.find_all("table", class_="table table-responsive table-bordered table-hover")[2].find_all_next("tr")
    print()
    for i in block:
        s = (i.text)
        s=ultima_strip_update(s)
        if len(s) > 3 and s[0].isdigit() == 1:
            s=s.split('  ')
            print(s[1].strip())
            lis.append([s[1].strip(), "физика"])
    block = soup.find_all("table", class_="table table-responsive table-bordered table-hover")[3].find_all_next("tr")
    print()
    for i in block:
        s = (i.text)
        s=ultima_strip_update(s)
        if len(s) > 3 and s[0].isdigit() == 1:
            s=s.split('  ')
            print(s[1].strip())
            lis.append([s[1].strip(), "информатика"])
def pars_mfti2():
    url = "https://pk.mipt.ru/bachelor/2023_olympiads/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find_all("table", style="border-collapse: collapse;")[7].find_all('tr')
    a=dict()
    s=str()

    for row in rows:
        rowy = row.find_all('td')
        if (len(rowy) == 3):
            s=strip_level(rowy[0].text)
            ss2=strip_level(rowy[1].text)
            ss3=strip_level(rowy[2].text)
            a[s]=[['математика' , ss2 ,ss3]]
        elif(len(rowy)==2):

            a[s].append(['математика' , strip_level(rowy[0].text) , strip_level(rowy[1].text)])

    rows = soup.find_all("table", style="border-collapse: collapse;")[8].find_all('tr')

    s = str()

    for row in rows:
        rowy = row.find_all('td')
        if (len(rowy) == 3):
            s = strip_level(rowy[0].text)
            ss2 = strip_level(rowy[1].text)
            ss3 = strip_level(rowy[2].text)
            if (s in a ):
                a[s].append(['физика', ss2, ss3])

            else:
                a[s] = [['физика', ss2, ss3]]

        elif (len(rowy) == 2):
            s = strip_level(rowy[0].text)
            if (s in a):
                a[s].append(['физика', strip_level(rowy[1].text)])
            else:
                a[s]=[['физика', strip_level(rowy[1].text)]]
    rows = soup.find_all("table", style="border-collapse: collapse;")[10].find_all('tr')

    s = "Всероссийская олимпиада"

    for row in rows:
        rowy = row.find_all('td')
        if (len(rowy) == 3):
            s = strip_level(rowy[0].text)
            ss2 = strip_level(rowy[1].text)
            ss3 = strip_level(rowy[2].text)
            if (s in a):
                a[s].append(['информатика', ss2, ss3])

            else:
                a[s] = [['информатика', ss2, ss3]]

        elif (len(rowy) == 2):
            a[s].append(['информатика', strip_level(rowy[0].text), strip_level(rowy[1].text)])

    return a

def pars_mfti3():
    url = "https://pk.mipt.ru/bachelor/2023_olympiads/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find_all("table", style="border-collapse: collapse;")[7].find_all('tr')
    a=dict()
    s=str()
    schools=['ФРКТ',"ЛФИ","ФАКТ","ФЭФМ","ИНБИКТС","ФБВТ","ФПМИ"]
    for row in rows:
        rowy = row.find_all('td')
        if (len(rowy) == 3):
            s=strip_level(rowy[0].text)
            ss2=strip_level(rowy[1].text)
            ss3=strip_level(rowy[2].text)
            a[s]=[['математика']]
        elif(len(rowy)==2):
            ss=strip_level(rowy[0].text)
            f=0
            for i in schools:
                if(ss.count(i) >0):
                    f=1
            if (f == 0):
                a[ss] = [['математика']]

    rows = soup.find_all("table", style="border-collapse: collapse;")[8].find_all('tr')

    s = str()

    for row in rows:
        rowy = row.find_all('td')
        if (len(rowy) == 3):
            s = strip_level(rowy[0].text)
            ss2 = strip_level(rowy[1].text)
            ss3 = strip_level(rowy[2].text)
            if (s in a ):
                a[s].append(['физика'])

            else:
                a[s] = [['физика']]

        elif (len(rowy) == 2):
            ss = strip_level(rowy[0].text)
            f = 0
            for i in schools:
                if (ss.count(i) > 0):
                    f = 1
            if(f==0):
                if (ss in a):
                    a[ss].append(['физика'])
                else:
                    a[ss]=[['физика']]
    rows = soup.find_all("table", style="border-collapse: collapse;")[10].find_all('tr')

    s = "Всероссийская олимпиада"

    for row in rows:
        rowy = row.find_all('td')
        if (len(rowy) == 3):
            s = strip_level(rowy[0].text)
            ss2 = strip_level(rowy[1].text)
            ss3 = strip_level(rowy[2].text)
            if (s in a):
                a[s].append(['информатика'])

            else:
                a[s] = [['информатика']]

        elif (len(rowy) == 2):
            ss = strip_level(rowy[0].text)
            f = 0
            for i in schools:
                if (ss.count(i) > 0):
                    f = 1
            if(f==0):
                if (ss in a):
                    a[ss].append(['информатика'])
                else:
                    a[ss]=[['информатика']]

    return a





def check_for_mfti(mfti:dict , spis:list):
    print('mfti' , spis)
    ans = list()
    for i in spis:
        if (i[0] in mfti):
            for j in mfti[i[0]]:
                print('what' , i)
                print('with' , j)
                if (j[0] == i[1]):
                    ans.append([i[0] , j[0]])
    return ans




