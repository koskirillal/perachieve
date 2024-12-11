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
def all_in_rsosh( spisok:str):
    a=rsosh()
    ans = list()
    for i in a:
        for j in spisok:
            if (i.upper().strip() == j.upper().strip()):
                ans.append(j.strip())
    return ans
