from pickletools import stringnl

import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests
from bs4 import BeautifulSoup

import PyPDF2
from another_try import strip_update, compare_strip


def check_exists_by_xpath(xpath , browser):
    try:
        browser.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


def check_exists_by_xpath_mephi(xpath , browsermephi):
    try:
        browsermephi.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


def esr(s1, s2, s3, s4):


    browser = webdriver.Chrome()
    browser.get("https://diploma.olimpiada.ru/full-diplomas")
    inputsur = browser.find_element(By.XPATH,
                                    '/html/body/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div[2]/input').send_keys(
        s1)
    iputname = browser.find_element(By.XPATH,
                                    '/html/body/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div[3]/input').send_keys(
        s2)
    inputot = browser.find_element(By.XPATH,
                                   '/html/body/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div[4]/input').send_keys(
        s3)
    inputd = browser.find_element(By.XPATH,
                                  '/html/body/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div[5]/input').send_keys(
        s4)
    button = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[1]/input').click()
    table = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
    spisok = list()
    '''/html/body/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/p/table[1]/tbody/tr/td[5]'''
    '''/html/body/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/p/table[2]/tbody/tr/td[5]'''
    '''/html/body/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/p/table[3]/tbody/tr/td[5]'''
    for i in range(1, 100):
        xpath = "/html/body/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/p/table[" + str(i) + "]"
        if (check_exists_by_xpath(xpath , browser)):
            block = (browser.find_element(By.XPATH, xpath))
            block2 = browser.find_element(By.XPATH , xpath + '''/tbody/tr/td[5]''')


            spisok.append(block.text)


    return spisok


def to_name_old_version(a: list):
    b = list()
    for i in range(len(a)):
        olymp = ""
        prof = ""
        f = 0
        ii = 0
        for j in range(len(a[i])):
            if (a[i][j] == '"'):
                f += 1
                continue
            if (f > 1):
                ii = j
                break
            if (f == 1):
                olymp += a[i][j]
        f = 0
        for j in range(ii, len(a[i])):
            if (a[i][j] == '('):
                f = 1
                continue
            elif (a[i][j] == ')'):
                f = 0
                break
            elif (f == 1):
                prof += a[i][j]
        b.append((olymp))
    i = 0
    n = len(b)
    while (i < n):
        if (b[i] == '' ):
            b.remove(b[i])
            i -= 1
            n -= 1
        i += 1
    return b





def pars_mephi():
    url = "https://admission.mephi.ru/admission/baccalaureate-and-specialty/specials/winners"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.find("div" , class_="field-item even").find("table").find("tbody").find_all("tr")


    names = list()
    for i in rows:
        s = i.text
        s = strip_update(s)
        s = s.split('\n')
        if (len(s) > 2):
            if (len(s[1]) > 5):
                if (s[1][:4].upper() == "ВСЕ," or s[1][0].isalpha() == 0):
                    continue
                else:
                    print(s)
                    names.append(s[1])
    return names


def check_for_mephi(list_mephi: list, newspisok: list):
    f = 0
    spis = list()
    for j in newspisok:
        if (list_mephi.count(j) > 0):
            print(j)
            spis.append(j)
            f = 1
    return spis

def chech_for_mephi2(mephi:dict , spis:list()):
    ans=list()
    print('chek' , spis)

    for i in spis:
        if(i[0] in mephi):
            for j in mephi[i[0]]:
                '''print('chek',j)
                print('chek_what' ,i)
                print('pizdec' , j[0] , i[1])'''
                if (i[1].upper() == j[0].upper() or i[1].upper() == j[4].upper()):
                    ans.append([i[0] , j[2] , i[1] , j[4]])


        print()
    return ans


def to_name(a: list):
    olymp = list()
    predmet = list()

    for i in a:
        k=i.split("скачать")
        for j in k:
            predlist = j.split('"')
            if(len(predlist)==5):

                for number in range (len(predlist)):

                    if (number == 1):
                        olymp.append(predlist[number])
                    elif (number == 3):
                        predmet.append(predlist[number])


    ans =[]
    for i in range(len(predmet)):
        ans.append([olymp[i] , predmet[i]])

    return ans

def pars_mephi2():
    url = "https://admission.mephi.ru/admission/baccalaureate-and-specialty/specials/winners"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.find("div", class_="field-item even").find("table").find("tbody").find_all("tr")
    a = dict()
    s=str()
    for row in rows:
        rowy = row.find_all('td')

        if (len(rowy) == 7):
             s = strip_update(rowy[1].text)
             a[s]=[[strip_update(rowy[5].text) ,str(rowy[2].text).count('I') , strip_update(rowy[3].text) , strip_update(rowy[4].text) ,strip_update(rowy[6].text)]]
        elif(len(rowy) == 5):
             a[s].append([strip_update(rowy[3].text) ,str(rowy[0].text).count('I') , strip_update(rowy[1].text) , strip_update(rowy[2].text)  , strip_update(rowy[4].text)])


    return a
