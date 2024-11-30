import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException





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
            if (int(block2.text) >= 10):
                spisok.append(block.text)

    return spisok


def to_name(a: list):
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
        b.append((olymp, prof))
    i = 0
    n = len(b)
    while (i < n):
        if (b[i][0] == '' or b[i][1] == ''):
            b.remove(b[i])
            i -= 1
            n -= 1
        i += 1
    return b


def pars_mephi():
    browsermephi = webdriver.Chrome()
    browsermephi.get("https://admission.mephi.ru/admission/baccalaureate-and-specialty/specials/winners")
    table = browsermephi.find_element(By.XPATH,
                                      "/html/body/div[3]/div[4]/div/div[3]/div/div/div/div/div/div/div/div[1]")


    names = list()
    for i in range(2, 1000):
        xpath = f"/html/body/div[3]/div[4]/div/div[3]/div/div/div/div/div/div/div/div[1]/table/tbody/tr[{str(i)}]"
        if (check_exists_by_xpath_mephi(xpath , browsermephi)):
            xpath += "/td[2]"
            if (check_exists_by_xpath_mephi(xpath , browsermephi)):
                name = browsermephi.find_element(By.XPATH, xpath)

                names.append(name.text)
    return names


def check_for_mephi(list_mephi: list, newspisok: list):
    f = 0
    for j in newspisok:
        if (list_mephi.count(j[0]) > 0):
            print(j[0])
            f = 1
    return f


