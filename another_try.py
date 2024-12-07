from xml.etree.ElementPath import xpath_tokenizer
import requests
import pandas
from bs4 import BeautifulSoup
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def strip_update(s:str):
    s = s.strip()
    a=""
    f=1
    for i in s:
        if (i != '\n' and i!='\t'):
            a+=i
            f=1
        elif(f == 1):
            if (i == '\n'):
                a+='\n'
            else:
                a+=' '
            f=0

    return a

