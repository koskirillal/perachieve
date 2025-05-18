from xml.etree.ElementPath import xpath_tokenizer
import requests
import pandas
from bs4 import BeautifulSoup
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from basepract import esr, to_name


def rsosh():
    url = "https://rsr-olymp.ru/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find('table', class_='mainTableInfo').find('tbody').find_all('tr')
    spisok = list()
    for row in rows:
        column = row.find_all('td')[1]

        name = column.find('a')

        if (name != None):
            name = str(name)
            name = name.split(' target="_blank">')
            spisok.append(name[1][:-4])
    return spisok





def is_rsosh(olymp:str):
    a=rsosh()
    for i in a:
        if(i.upper().strip() == olymp.upper().strip()):
            return 1
    return 0

def rsosh2():
    url = "https://rsr-olymp.ru/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find('table', class_='mainTableInfo').find('tbody').find_all('tr')
    spisok = list()
    a = dict()
    s = ""
    for row in rows:
        rowy = row.find_all('td')
        if (len(rowy) == 5):
            s = str(rowy[1].find('a')).split(' target="_blank">')[1][:-4]

            a[s] = [[rowy[2].text , int(str(rowy[4].text))]]
        elif(len(rowy) == 3):
            a[s].append([rowy[0].text , int(str(rowy[2].text))])
    return a




def all_in_rsosh( spisok:str):
    a=rsosh()
    ans = list()
    for i in a:
        for j in spisok:
            if (i.upper().strip() == j.upper().strip()):
                ans.append(j.strip())
    return ans


def check_for_rsosh(rsosh:dict , spis:list):
    print('rsosh' , spis)
    ans = list()
    for i in spis:
        if (i[0] in rsosh):
            for j in rsosh[i[0]]:
                if (j[0] == i[1]):
                    ans.append([i[0] , j[0] , j[1]])
    return ans
