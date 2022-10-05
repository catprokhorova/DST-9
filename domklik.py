import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

url = 'https://opendata.domclick.ru/offers/table/sankt-peterburg/last-30-days/'
driver = webdriver.Chrome()
driver.get(url)

all = driver.find_elements(By.CLASS_NAME, '_3Jl8x')
df = pd.DataFrame()
for el in all:
    data = {}
    el = el.text.split('\n')
    data['id'] = el[0]
    data['city'] = el[1]
    data['sale_all'] = el[2]
    data['sale_2'] = el[3]
    data['sale_1'] = el[4]
    data['avg_cost_2'] = el[5]
    data['avg_cost_1'] = el[6]
    data['avg_exp'] = el[7]
    df = pd.concat([df, pd.DataFrame([data])])
print(df)
