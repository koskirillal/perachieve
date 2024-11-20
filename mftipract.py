from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
browser.get("https://pk.mipt.ru/bachelor/2023_olympiads/")


def check_exists_by_xpath(xpath , browser):
    try:
        browser.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

def pars_mfti():
    '''/html/body/div/div[3]/div[3]/div/div[2]/div[2]/div[1]/table[2]/tbody/tr[2]'''
    '''/html/body/div/div[3]/div[3]/div/div[2]/div[2]/div[1]/table[2]/tbody/tr[3]'''
    spisok = list()
    for i in range(2 ,  1000):
        xpath = f'''/html/body/div/div[3]/div[3]/div/div[2]/div[2]/div[1]/table[2]/tbody/tr[{str(i)}]'''
        if (check_exists_by_xpath(xpath , browser)):
            block = browser.find_element(By.XPATH , xpath)
            spisok.append(block.text)
        else:
            break
    return spisok

a = pars_mfti()
for i in a:
    print(i)