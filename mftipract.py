from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from basepract import check_exists_by_xpath
browser = webdriver.Chrome()
browser.get("https://pk.mipt.ru/bachelor/2023_olympiads/")



def pars_mfti_math():

    spisok = list()
    for i in range(2 ,  1000):
        xpath = f'''/html/body/div/div[3]/div[3]/div/div[2]/div[2]/div[1]/table[2]/tbody/tr[{str(i)}]'''
        if (check_exists_by_xpath(xpath , browser)):
            block = browser.find_element(By.XPATH , xpath)
            spisok.append(block.text)
        else:
            break
    return spisok
def pars_mfti_phys():

    spisok = list()
    for i in range(2 , 1000):
        xpath = f'''/html/body/div/div[3]/div[3]/div/div[2]/div[2]/div[1]/table[3]/tbody/tr[{str(i)}]/td[2]/p'''
        if (check_exists_by_xpath(xpath , browser)):
            block = browser.find_element(By.XPATH , xpath)
            spisok.append(block.text)
        else:
            break
    return spisok
def pars_mfti_ikt():
    '''ikt'''
    spisok = list()
    for i in range (2, 1000):
        xpath=f'''/html/body/div/div[3]/div[3]/div/div[2]/div[2]/div[1]/table[4]/tbody/tr[{str(i)}]/td[2]/p'''
        if(check_exists_by_xpath(xpath , browser)):
            block = browser.find_element(By.XPATH, xpath)
            spisok.append(block.text)
        else:
            break
    return spisok


a = pars_mfti_ikt()
for i in a:
    print(i)
