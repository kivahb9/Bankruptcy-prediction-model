from selenium import webdriver
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

df_snp = pd.read_excel("export_dataframe.csv")
list_of_snp = df_snp["company_name"].tolist()

import time

# from bs4 import BeautifulSoup
driver = webdriver.Chrome(executable_path="C:/Users/bhavik.prajapati/chromedriver")
# /html/body/table/tbody/tr/td[2]/pre[2]/a
ciks = {}
import re

for i in list_of_snp:
    time.sleep(3)
    driver.get("https://www.sec.gov/edgar/searchedgar/cik.htm")
    name = driver.find_element_by_xpath('//*[@id="company"]')
    name.click()
    i = re.sub(r"[^a-zA-Z0-9]+", " ", i)
    #    i=i.lower().replace('inc','')
    name.send_keys(i.lower())
    submit = driver.find_element_by_xpath(
        '//*[@id="block-secgov-content"]/article/div[1]/div[2]/div[1]/div/div[1]/form/p[1]/input[2]'
    )
    submit.click()
    time.sleep(1)
    try:
        cik2 = driver.find_element_by_xpath(
            "/html/body/table/tbody/tr/td[2]/pre[2]/a[2]"
        )
        cik1 = driver.find_element_by_xpath(
            "/html/body/table/tbody/tr/td[2]/pre[2]/a[1]"
        )
        company_name1 = driver.find_element_by_xpath(
            "/html/body/table/tbody/tr/td[2]/pre[2]/text()[1]"
        )
        company_name2 = driver.find_element_by_xpath(
            "/html/body/table/tbody/tr/td[2]/pre[2]/text()[2]"
        )
        if fuzz.ratio(i, company_name1) > fuzz.ratio(i, company_name2):
            ciks[i] = cik1.text
        else:
            ciks[i] = cik2.text
    except:
        ciks[i] = "na"
    try:
        #        cik2=driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/pre[2]/a[2]')
        cik1 = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/pre[2]/a")
        company_name1 = driver.find_element_by_xpath(
            "/html/body/table/tbody/tr/td[2]/pre[2]/text()"
        )
        #        company_name2=driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/pre[2]/text()[2]')
        #        if fuzz.ratio(i,company_name1)>fuzz.ratio(i,company_name2):
        ciks[i] = cik1.text
    except:
        ciks[i] = "na"
#        else:
#            ciks[i]=cik2.text


df_company = pd.DataFrame(list(ciks.items()), columns=["company", "cik"])
df_company1 = df_company.sort_values(by=["company"])
df_company1.index = range(len(df_company))
df_company1.to_csv("test.csv")
# list_of_cik_avail=[]
# for key, value in ciks.items():
##    temp = [key,value]
#    list_of_cik_avail.append(key)
# list_of_cik_na=[]
# for i in list_name:
#    if i not in list_of_cik_avail:
#        list_of_cik_na.append(i)

#    cik1=driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/pre[2]/a[1]')
#    cik2=driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/pre[2]/a[2]')
#    time.sleep(0.5)
#    ciks.append(cik.text)
#    page = requests.get(driver.current_url)
#    soup = BeautifulSoup(page.text)
#    cik = soup.find_all('table')
#    print (cik)


import plotly.express as px

import pandas as pd

df = pd.read_excel(
    "C:\\Users\\bhavik.prajapati\\Desktop\\Creditpulse_indexing\\graph_plotting.xlsx"
)

fig = px.line(df, x="effective_date", y="credit_score")
fig.show()
