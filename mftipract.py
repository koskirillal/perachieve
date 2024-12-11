from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests
import pandas
from bs4 import BeautifulSoup

from another_try import strip_update, ultima_strip_update
from basepract import check_exists_by_xpath




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

            lis.append(s[1].strip())
    return lis




