import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def esr(s1 , s2 , s3 , s4):
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
    block = table.find_element(By.XPATH , '//*[@id="results"]/table[1]')
    pblock = block.find_element(By.XPATH , '//*/tbody/tr/td[1]')
    print(pblock.text)


esr("Косолапов" , "Кирилл" , "Алексеевич" , "2008-04-07")



