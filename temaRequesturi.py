import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/')

table = browser.find_element(By.XPATH, '//*[@id="post-25121"]/div/div/table[1]')
table_text = table.text
lista = table_text.split('\n')
first_column = []
second_column = []
third_column = []
fourth_column = []
fifth_column = []

for j in range(1, len(lista)):
    path1 = f'//*[@id="post-25121"]/div/div/table[1]/tbody/tr[{j + 1}]/td[1]'
    path2 = f'//*[@id="post-25121"]/div/div/table[1]/tbody/tr[{j + 1}]/td[2]'
    path3 = f'//*[@id="post-25121"]/div/div/table[1]/tbody/tr[{j + 1}]/td[3]'
    path4 = f'//*[@id="post-25121"]/div/div/table[1]/tbody/tr[{j + 1}]/td[4]'
    first_column.append(browser.find_element(By.XPATH, path1).text)
    second_column.append(browser.find_element(By.XPATH, path2).text)
    third_column.append(browser.find_element(By.XPATH, path3).text)
    fourth_column.append(browser.find_element(By.XPATH, path4).text)
for k in range(1, len(lista)-2):
    path5 = f'//*[@id="post-25121"]/div/div/table[1]/tbody/tr[{k + 1}]/td[5]'
    fifth_column.append(browser.find_element(By.XPATH, path5).text)

fifth_column.append(' ')
fifth_column.append(' ')

data = {'Nr. crt.': first_column, 'Județ': second_column, 'Număr de cazuri confirmate(total)': third_column, 'Număr de cazuri nou confirmate': fourth_column,
        'Incidența  înregistrată la 14 zile': fifth_column}

df = pd.DataFrame(data=data)
df.to_excel('temaRequesturi.xlsx', index=False)

time.sleep(10)
browser.close()

