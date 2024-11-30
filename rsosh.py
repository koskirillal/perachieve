from xml.etree.ElementPath import xpath_tokenizer
import requests
import pandas
from bs4 import BeautifulSoup
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



url = "https://rsr-olymp.ru/"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
rows = soup.find('table',class_='mainTableInfo').find('tbody').find_all('tr')

for row in rows:
    column = row.find_all('td')[1]

    name = column.find('a')

    if (name != None):

        name = str(name)
        name=name.split(' target="_blank">')
        print(name[1][:-4])

